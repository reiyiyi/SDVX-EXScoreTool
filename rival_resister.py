import st_data
import st_login

def is_exist(rival):
    user_data = st_data.load_user_data()
    if rival not in user_data:
        return False
    return True

def follow_rival(rival):
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    user_data[user]["rival"][rival] = user_data[rival]["user-name"]
    user_data[rival]["rev-rival"][user] = user_data[user]["user-name"]
    st_data.save_user_data(user_data)

def remove_rival(rival):
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    user_data[user]["rival"].pop(rival)
    user_data[rival]["rev-rival"].pop(user)
    st_data.save_user_data(user_data)