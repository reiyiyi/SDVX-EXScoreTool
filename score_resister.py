import pandas as pd
from io import StringIO
import queue
import st_data

def update_score(user, score_txt_data):
    score_txt_data = StringIO(score_txt_data)
    score_data = pd.read_csv(score_txt_data, sep=",")

    effect_id_data = st_data.load_effect_id_data()
    rev_effect_id_data = st_data.load_rev_effect_id_data()
    user_data = st_data.load_user_data()
    exscore_data = st_data.load_exscore_data()
    hi_score_list = user_data[user]["hi-score"][0:]

    for i in range(score_data.shape[0]):
        tune_name = score_data.loc[i, "          楽曲名"]
        diff = score_data.loc[i, "難易度"]
        level = score_data.loc[i, "楽曲レベル"]
        if exscore_data.loc[effect_id_data[tune_name][diff], user] < score_data.loc[i, "EXスコア"] and exscore_data.loc[effect_id_data[tune_name][diff], user] > 0:
            before_score = exscore_data.loc[effect_id_data[tune_name][diff], user]
            after_score = score_data.loc[i, "EXスコア"]
            add_data = {
                "楽曲名":tune_name,
                "難易度":diff,
                "レベル":level,
                "更新前スコア":before_score,
                "更新後スコア":after_score
            }
            if len(hi_score_list) == 100:
                hi_score_list = hi_score_list[1:]
            hi_score_list.append(add_data)

        exscore_data.loc[effect_id_data[tune_name][diff], user] = score_data.loc[i, "EXスコア"]
    user_data[user]["hi-score"] = hi_score_list[0:]

    st_data.save_user_data(user_data)
    st_data.save_exscore_data(exscore_data)

