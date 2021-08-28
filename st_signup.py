import st_data

def id_check(user):
    mask = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for ch in user:
        if ch not in mask:
            return False
    return True

def try_signup(user, pw):
    user_data = st_data.load_user_data()

    if user in user_data:
        return 'このユーザーIDは既に使われています'
    if not id_check(user):
        return 'ユーザーIDに使用することのできない文字が含まれています'
    if len(user) > 16 or len(user) < 1:
        return 'ユーザーIDは1文字以上16文字以下にしてください'
    if len(pw) < 4:
        return 'パスワードは4文字以上にしてください'

    exscore_data = st_data.load_exscore_data()
    strengths_data = st_data.load_strengths_data()
    ranking_data = st_data.load_ranking_data()

    user_data[user] = {
        "user-name": user,
        "password": pw,
        "search-rival": "",
        "rival": {},
        "rev-rival": {},
        "notice": [],
        "hi-score": [],
        "score-setting": True
    }
    exscore_data[user] = 0
    strengths_data[user] = 999
    ranking_data[user] = -1

    st_data.save_user_data(user_data)
    st_data.save_exscore_data(exscore_data)
    st_data.save_strengths_data(strengths_data)
    st_data.save_ranking_data(ranking_data)
    return '成功'