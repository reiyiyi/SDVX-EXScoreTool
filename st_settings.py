import st_data
import st_login

def score_settings_change(new_user_name, score_setting):
    user = st_login.get_user_id()
    user_data = st_data.load_user_data()
    user_data[user]["user-name"] = new_user_name
    user_data[user]["score-setting"] = score_setting
    st_data.save_user_data(user_data)

def get_settings():
    user = st_login.get_user_id()
    user_data = st_data.load_user_data()
    user_name = user_data[user]["user-name"]
    score_setting = user_data[user]["score-setting"]
    return user_name, score_setting