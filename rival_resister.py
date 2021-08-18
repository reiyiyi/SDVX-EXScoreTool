import st_data
import st_login
import copy

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
    user_data[user]["rival"][rival] = False
    user_data[rival]["rev-rival"][user] = False
    if rival in user_data[user]["rev-rival"]:
        user_data[user]["rival"][rival] = True
        user_data[rival]["rev-rival"][user] = True
        user_data[user]["rev-rival"][rival] = True
        user_data[rival]["rival"][user] = True
    st_data.save_user_data(user_data)

def remove_rival():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    rival = user_data[user]["search-rival"]
    user_data[user]["rival"].pop(rival)
    user_data[rival]["rev-rival"].pop(user)
    if rival in user_data[user]["rev-rival"]:
        user_data[user]["rev-rival"][rival] = False
        user_data[rival]["rival"][user] = False
    st_data.save_user_data(user_data)

def get_rival():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    return_data = user_data[user]["rival"].copy()
    for rival in return_data:
        return_data[rival] = user_data[rival]["user-name"]
    return return_data

def get_rev_rival():
    user_data = st_data.load_user_data()
    user = st_login.get_user_id()
    return_data = user_data[user]["rev-rival"].copy()
    for rival in return_data:
        return_data[rival] = user_data[rival]["user-name"]
    return return_data

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