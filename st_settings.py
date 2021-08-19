import st_data
import st_login

def id_check(user):
    mask = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    for ch in user:
        if ch not in mask:
            return False
    return True

def score_settings_change(new_user_name, score_setting):
    if not id_check(new_user_name):
        return 'ユーザー名に使用することのできない文字が含まれています'
    if len(new_user_name) > 16 or len(new_user_name) < 1:
        return 'ユーザー名は1文字以上16文字以下にしてください'
    user = st_login.get_user_id()
    user_data = st_data.load_user_data()
    user_data[user]["user-name"] = new_user_name
    user_data[user]["score-setting"] = score_setting
    st_data.save_user_data(user_data)
    return '成功'

def get_settings():
    user = st_login.get_user_id()
    user_data = st_data.load_user_data()
    user_name = user_data[user]["user-name"]
    score_setting = user_data[user]["score-setting"]
    return user_name, score_setting