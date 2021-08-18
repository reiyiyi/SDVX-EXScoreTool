import st_data
import st_login

def is_exist(rival):
    user_data = st_data.load_user_data()
    if rival not in user_data:
        return False
    return True

def follow_rival():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    rival = user_data[user]["search-rival"]
    user_data[user]["search-rival"] = ""
    user_data[user]["rival"][rival] = user_data[rival]["user-name"]
    user_data[rival]["rev-rival"][user] = user_data[user]["user-name"]
    st_data.save_user_data(user_data)

def remove_rival(rival):
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    user_data[user]["rival"].pop(rival)
    user_data[rival]["rev-rival"].pop(user)
    st_data.save_user_data(user_data)

def get_rival():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    return user_data[user]["rival"]

def get_rev_rival():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    return user_data[user]["rev-rival"]

def get_rival_name(rival):
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    user_data[user]["search-rival"] = rival
    st_data.save_user_data(user_data)
    return user_data[rival]["user-name"]

def cancel():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    user_data[user]["search-rival"] = ""
    st_data.save_user_data(user_data)