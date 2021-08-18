import st_data
import st_login

def get_notice():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    return user_data[user]["notice"]