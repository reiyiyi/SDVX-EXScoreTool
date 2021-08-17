import st_data

def try_signup(user, pw):
    user_data = st_data.load_user_data()
    exscore_data = st_data.load_exscore_data()
    user_data[user] = {
        "user-name": user,
        "password": pw,
        "rival": {},
        "rev-rival": {},
        "notice": [],
        "hi-score": [],
        "score-setting": True
    }
    exscore_data[user] = 0

    st_data.save_user_data(user_data)
    st_data.save_exscore_data(exscore_data)