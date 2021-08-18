import pandas as pd
import numpy as np
from io import StringIO
import st_data

def update_score(user, score_txt_data):
    score_txt_data = StringIO(score_txt_data)
    score_data = pd.read_csv(score_txt_data, sep=",")

    effect_id_data = st_data.load_effect_id_data()
    user_data = st_data.load_user_data()
    exscore_data = st_data.load_exscore_data()
    hi_score_list = user_data[user]["hi-score"][0:]

    for i in range(score_data.shape[0]):
        tune_name = score_data.loc[i, "          楽曲名"]
        diff = score_data.loc[i, "難易度"]
        level = score_data.loc[i, "楽曲レベル"]
        if exscore_data.loc[effect_id_data[tune_name][diff]["id"], user] < score_data.loc[i, "EXスコア"] and exscore_data.loc[effect_id_data[tune_name][diff]["id"], user] > 0:
            before_score = exscore_data.loc[effect_id_data[tune_name][diff]["id"], user]
            after_score = score_data.loc[i, "EXスコア"]
            add_data = {
                "楽曲名":tune_name,
                "難易度":diff,
                "レベル":level.item(),
                "更新前スコア":before_score.item(),
                "更新後スコア":after_score.item()
            }
            if len(hi_score_list) == 100:
                hi_score_list = hi_score_list[1:]
            hi_score_list.append(add_data)
            exscore_data.loc[effect_id_data[tune_name][diff]["id"], user] = score_data.loc[i, "EXスコア"]

            if user_data[user]["score-setting"] == False:
                continue

            for rival in user_data[user]["rev-rival"]:
                if before_score <= exscore_data.loc[effect_id_data[tune_name][diff]["id"], rival] and \
                    after_score >= exscore_data.loc[effect_id_data[tune_name][diff]["id"], rival]:
                    notice_data = {
                        "楽曲名":tune_name,
                        "難易度":diff,
                        "レベル":level.item(),
                        "好敵手名":user_data[user]["user-name"],
                        "スコア":exscore_data.loc[effect_id_data[tune_name][diff]["id"], rival].item(),
                        "好敵手更新前スコア":before_score.item(),
                        "好敵手更新後スコア":after_score.item()
                    }
                    if len(user_data[rival]["notice"]) == 100:
                        user_data[rival]["notice"] = user_data[rival]["notice"][1:]
                    user_data[rival]["notice"].append(notice_data)

    user_data[user]["hi-score"] = hi_score_list[0:]

    st_data.save_user_data(user_data)
    st_data.save_exscore_data(exscore_data)