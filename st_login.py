from rival_resister import is_resistered
from flask import session, redirect
import st_data

def is_login():
    return 'login' in session

def try_login(user_id, password):
    USER_LIST = st_data.load_user_data()
    if user_id not in USER_LIST:
        return False
    if password != USER_LIST[user_id]['password']:
        return False
    session['login'] = user_id
    return True

def try_logout():
    session.pop('login', None)
    return True

def get_user_id():
    if is_login():
        return session['login']
    return 'not login'

def get_user_name():
    user_data = st_data.load_user_data()
    if is_login():
        return user_data[session['login']]["user-name"]
    return 'not login'

def get_rival_user_name(user):
    user_data = st_data.load_user_data()
    if is_resistered(user):
        return user_data[user]["user-name"]
    else:
        return 'no data'

def is_resistered(user):
    user_data = st_data.load_user_data()
    return user in user_data