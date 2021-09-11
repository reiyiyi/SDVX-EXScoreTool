import st_data
import st_login

def get_my_score_data(level):
    user = st_login.get_user_id()
    rev_effect_id_data = st_data.load_rev_effect_id_data()
    exscore_data = st_data.load_exscore_data()
    return_data = []

    for i in range(rev_effect_id_data.shape[0]):
        if rev_effect_id_data.loc[i, "レベル"] != level:
            continue
        add_data = {
            "楽曲名":rev_effect_id_data.loc[i, "楽曲名"],
            "難易度":rev_effect_id_data.loc[i, "難易度"],
            "EXスコア":exscore_data.loc[i, user],
            "MAX-":"?",
            "effect_id":i
        }
        if rev_effect_id_data.loc[i, "MAX"] >= 0:
            add_data["MAX-"] = rev_effect_id_data.loc[i, "MAX"] - exscore_data.loc[i, user]
        return_data.append(add_data)
    return_data.reverse()

    return return_data

def get_ranking_data(effect_id):
    user_data = st_data.load_user_data()
    ranking_data = st_data.load_ranking_data()
    old_exscore_data = st_data.load_old_exscore_data()
    rev_effect_id_data = st_data.load_rev_effect_id_data()
    if effect_id < 0 or effect_id >= ranking_data.shape[0]:
        return False, False

    return_effect_data = {
        "楽曲名":rev_effect_id_data.loc[effect_id, "楽曲名"],
        "難易度":rev_effect_id_data.loc[effect_id, "難易度"],
        "レベル":rev_effect_id_data.loc[effect_id, "レベル"]
    }
    return_ranking_data = [{
        "ユーザーID":"---",
        "ユーザー名":"---",
        "EXスコア":"---",
        "MAX-":"?"
    } for _ in range(100)]

    for user in ranking_data.columns:
        if ranking_data.loc[effect_id, user] <= 0 or ranking_data.loc[effect_id, user] > 100:
            continue
        user_rank = ranking_data.loc[effect_id, user]
        if user_data[user]["score-setting"]:
            return_ranking_data[user_rank - 1]["ユーザーID"] = user
            return_ranking_data[user_rank - 1]["ユーザー名"] = user_data[user]["user-name"]
        else:
            return_ranking_data[user_rank - 1]["ユーザーID"] = "[SECRET]"
            return_ranking_data[user_rank - 1]["ユーザー名"] = "[SECRET]"
        return_ranking_data[user_rank - 1]["EXスコア"] = old_exscore_data.loc[effect_id, user]
        if rev_effect_id_data.loc[effect_id, "MAX"] >= 0:
            return_ranking_data[user_rank - 1]["MAX-"] = rev_effect_id_data.loc[effect_id, "MAX"] - old_exscore_data.loc[effect_id, user]

    return return_effect_data, return_ranking_data

def get_spuc_data(user):
    rev_effect_id_data = st_data.load_rev_effect_id_data()
    exscore_data = st_data.load_exscore_data()

    return_spuc_data = [0] * 20
    return_num_data = [0] * 20
    for i in range(rev_effect_id_data.shape[0]):
        if rev_effect_id_data.loc[i, "難易度"] in ["NOVICE", "ADVANCED"]:
            continue
        if exscore_data.loc[i, user] == rev_effect_id_data.loc[i, "MAX"]:
            return_spuc_data[rev_effect_id_data.loc[i, "レベル"] - 1] += 1
        return_num_data[rev_effect_id_data.loc[i, "レベル"] - 1] += 1
            
    return return_spuc_data, return_num_data