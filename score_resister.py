import pandas as pd
import numpy as np
from io import StringIO
import st_data
import st_login

def update_score(score_txt_data):
    return_data = []
    return_error_data = []
    resister_error_data = st_data.load_resister_error_data()
    user = st_login.get_user_id()

    idx = score_txt_data.index('楽')
    score_txt_data = score_txt_data[idx:]
    score_txt_data = StringIO(score_txt_data)
    score_data = pd.read_csv(score_txt_data, sep=",")

    if (score_data.columns == ['楽曲名', '難易度', '楽曲レベル', 'クリアランク', 'スコアグレード', 'ハイスコア', 'EXスコア', 'プレー回数',
       'クリア回数', 'ULTIMATE CHAIN', 'PERFECT']).sum() != 11:
        return False
    if score_data.isnull().values.sum() > 0:
        return False

    effect_id_data = st_data.load_effect_id_data()
    rev_effect_id_data = st_data.load_rev_effect_id_data()
    user_data = st_data.load_user_data()
    exscore_data = st_data.load_exscore_data()
    hi_score_list = user_data[user]["hi-score"][0:]

    for i in range(score_data.shape[0]):
        tune_name = score_data.loc[i, "楽曲名"]
        diff = score_data.loc[i, "難易度"]
        level = score_data.loc[i, "楽曲レベル"]

        if tune_name not in effect_id_data:
            add_error_data = {
                "楽曲名":tune_name,
                "難易度":diff,
                "ユーザー名":user,
                "原因":"楽曲名"
            }
            if len(return_error_data) >= 100:
                return_error_data = return_error_data[-99:]
            if len(resister_error_data) >= 1000:
                resister_error_data = resister_error_data[-999:]
            return_error_data.append(add_error_data)
            resister_error_data.append(add_error_data)
            continue
        
        if diff not in effect_id_data[tune_name]:
            add_error_data = {
                "楽曲名":tune_name,
                "難易度":diff,
                "ユーザー名":user,
                "原因":"難易度"
            }
            if len(return_error_data) >= 100:
                return_error_data = return_error_data[-99:]
            if len(resister_error_data) >= 1000:
                resister_error_data = resister_error_data[-999:]
            return_error_data.append(add_error_data)
            resister_error_data.append(add_error_data)
            continue

        before_score = int(exscore_data.loc[effect_id_data[tune_name][diff]["id"], user])
        after_score = int(score_data.loc[i, "EXスコア"])
        max_score = rev_effect_id_data.loc[effect_id_data[tune_name][diff]["id"], "MAX"]
        exscore_data.loc[effect_id_data[tune_name][diff]["id"], user] = int(score_data.loc[i, "EXスコア"])

        if before_score < after_score and before_score > 0:
            add_data = {
                "楽曲名":tune_name,
                "難易度":diff,
                "レベル":level.item(),
                "更新前スコア":before_score,
                "更新後スコア":after_score
            }
            if max_score >= 0:
                add_data["MAX"] = max_score.item()
            if len(hi_score_list) == 100:
                hi_score_list = hi_score_list[1:]
            hi_score_list.append(add_data)

            if len(return_data) == 100:
                return_data = return_data[1:]
            return_data.append(add_data)

        if user_data[user]["score-setting"] == False:
            continue

        if before_score < after_score:
            for rival in user_data[user]["rev-rival"]:
                if before_score <= exscore_data.loc[effect_id_data[tune_name][diff]["id"], rival] and \
                    before_score > 0 and \
                    after_score >= exscore_data.loc[effect_id_data[tune_name][diff]["id"], rival] and \
                    exscore_data.loc[effect_id_data[tune_name][diff]["id"], rival] > 0:
                    notice_data = {
                        "楽曲名":tune_name,
                        "難易度":diff,
                        "レベル":level.item(),
                        "好敵手名":user_data[user]["user-name"],
                        "スコア":exscore_data.loc[effect_id_data[tune_name][diff]["id"], rival].item(),
                        "好敵手更新前スコア":before_score,
                        "好敵手更新後スコア":after_score
                    }
                    if max_score >= 0:
                        notice_data["MAX"] = max_score.item()
                    if len(user_data[rival]["notice"]) == 100:
                        user_data[rival]["notice"] = user_data[rival]["notice"][1:]
                    user_data[rival]["notice"].append(notice_data)

    user_data[user]["hi-score"] = hi_score_list[0:]

    st_data.save_user_data(user_data)
    st_data.save_exscore_data(exscore_data)
    st_data.save_resister_error_data(resister_error_data)

    return return_data, return_error_data

def get_hi_score_data():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    return user_data[user]["hi-score"]