from flask import Flask, render_template, session, redirect
from flask.globals import request
import os
import st_login
import st_data
import st_signup
import st_settings
import st_notice
import score_resister
import rival_resister

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

@app.route('/')
def index():
    if not st_login.is_login():
        return redirect('/login')
    user = st_login.get_user_name()
    return render_template('index.html',
                            user=user)

@app.route('/manual')
def manual():
    return render_template('manual.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/try', methods=['POST'])
def try_login():
    user = request.form.get('user', '')
    pw = request.form.get('pw', '')
    if st_login.try_login(user, pw):
        return redirect('/')
    return redirect('/login')
    #ユーザデータ

@app.route('/login/signup')
def signup():
    #ユーザデータ
    return render_template('form.html')

@app.route('/login/signup/try', methods=['POST'])
def try_signup():
    user = request.form.get('user', '')
    pw = request.form.get('pw', '')
    mode = st_signup.try_signup(user, pw)
    if mode == '成功':
        return redirect('/login')
    return render_template('form_error.html',
                            mode=mode)
    #ユーザデータ

@app.route('/logout')
def logout():
    if not st_login.is_login():
        return redirect('/login')
    return render_template('logout.html')

@app.route('/logout/try', methods=['GET'])
def try_logout():
    if not st_login.is_login():
        return redirect('/login')
    st_login.try_logout()
    return redirect('/login')
    #ユーザデータ

@app.route('/resister')
def resister():
    if not st_login.is_login():
        return redirect('/login')
    return render_template('resister.html')

@app.route('/resister/hiscore', methods=['POST'])
def hiscore():
    if not st_login.is_login():
        return redirect('/login')
    hi_score_data = []
    if 'score' in request.form:
        score_txt_data = str(request.form['score'])
        hi_score_data = score_resister.update_score(score_txt_data)
    return render_template('hiscore.html',
                            hi_score_list=hi_score_data,
                            data_num=len(hi_score_data),
                            mode='今回')

@app.route('/hiscore')
def recently_hiscore():
    if not st_login.is_login():
        return redirect('/login')
    hi_score_data = score_resister.get_hi_score_data()
    return render_template('hiscore.html',
                            hi_score_list=hi_score_data,
                            data_num=len(hi_score_data),
                            mode='直近')

@app.route('/notice')
def notice():
    if not st_login.is_login():
        return redirect('/login')
    notice_list = st_notice.get_notice()
    return render_template('notice.html',
                            notice_list=notice_list[0:],
                            data_num=len(notice_list))

@app.route('/rival')
def rival():
    if not st_login.is_login():
        return redirect('/login')
    return render_template('rival.html')

@app.route('/rival/follow')
def rival_follow():
    if not st_login.is_login():
        return redirect('/login')
    rival_data = rival_resister.get_rival()
    return render_template('rival-list.html',
                            current="好敵手",
                            rival_data=rival_data)

@app.route('/rival/follower')
def rival_follower():
    if not st_login.is_login():
        return redirect('/login')
    rev_rival_data = rival_resister.get_rev_rival()
    return render_template('rival-list.html',
                            current="逆好敵手",
                            rival_data=rev_rival_data)

@app.route('/rival/search')
def rival_search():
    if not st_login.is_login():
        return redirect('/login')
    rival_resister.cancel()
    return render_template('rival-search.html')

@app.route('/rival/search/follow', methods=['POST'])
def follow_rival():
    if not st_login.is_login():
        return redirect('/login')
    search_id = request.form.get('search-id')
    if not rival_resister.is_exist(search_id):
        return redirect('/rival/search')
    rival_name = rival_resister.get_rival_name(search_id)
    text_data = 'を好敵手に登録'
    if rival_resister.is_resistered():
        text_data = 'の好敵手設定を解除'
    return render_template('rival-resister.html',
                            rival_name=rival_name,
                            text_data=text_data)

@app.route('/rival/search/follow/try', methods=['GET'])
def try_follow_rival():
    if not st_login.is_login():
        return redirect('/login')
    if rival_resister.is_resistered():
        rival_resister.remove_rival()
        return redirect('/rival/search')
    rival_resister.follow_rival()
    return redirect('/rival/search')

@app.route('/settings')
def settings():
    if not st_login.is_login():
        return redirect('/login')
    user_name, score_setting = st_settings.get_settings()
    true_checked = ""
    false_checked = ""
    if score_setting:
        true_checked = "checked"
    else:
        false_checked = "checked"
    return render_template('settings.html',
                            user_name=user_name,
                            true_checked=true_checked,
                            false_checked=false_checked)

@app.route('/settings/change', methods=['POST'])
def chenge():
    if not st_login.is_login():
        return redirect('/login')
    new_user_name = request.form.get('new-user-name')
    score_setting = request.form.get('score-setting')
    if score_setting == 'yes':
        score_setting = True
    else:
        score_setting = False
    mode = st_settings.score_settings_change(new_user_name, score_setting)
    if mode == '成功':
        return redirect('/')
    return render_template('settings_error.html',
                            mode=mode)

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0')

#http://localhost:5000