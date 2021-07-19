from flask import session, redirect
import st_data

USER_LIST = st_data.load_user_data()

def is_login():
    return 'login' in session

def try_login(user_id, password):
    if user_id in USER_LIST:
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