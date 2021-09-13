import st_data
import st_login

def get_strengths():
    user = st_login.get_user_id()
    strengths_data = st_data.load_strengths_data()
    rev_effect_id_data = st_data.load_rev_effect_id_data()
    exscore_data = st_data.load_exscore_data()

    sort_data = list(strengths_data[user])
    for i in range(len(sort_data)):
        sort_data[i] = {
            "上位%":sort_data[i],
            "ID":i
        }
    sort_data.sort(key=lambda x: x["上位%"])
    sort_data = sort_data[:300]

    return_data = [dict() for _ in range(len(sort_data))]
    for i in range(len(sort_data)):
        return_data[i] = {
            "ID":sort_data[i]["ID"],
            "楽曲名":rev_effect_id_data.loc[sort_data[i]["ID"], "楽曲名"],
            "難易度":rev_effect_id_data.loc[sort_data[i]["ID"], "難易度"],
            "レベル":rev_effect_id_data.loc[sort_data[i]["ID"], "レベル"],
            "EXスコア":exscore_data.loc[sort_data[i]["ID"], user],
            "上位%":'{:.2f}'.format(round(sort_data[i]["上位%"], 2))
        }
        if rev_effect_id_data.loc[sort_data[i]["ID"], "MAX"] >= 0:
            return_data[i]["MAX-"] = rev_effect_id_data.loc[sort_data[i]["ID"], "MAX"] - exscore_data.loc[sort_data[i]["ID"], user]
        else:
            return_data[i]["MAX-"] = "?"
            
        if sort_data[i]["上位%"] > 200:
            return_data[i]["上位%"] = '---'

    return return_data