from flask import Flask, render_template, session, redirect
from flask.globals import request
import os
import st_login
import st_data
import st_signup
import st_strengths
import score_check
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
    user = st_login.get_user_id()
    return redirect('/user/' + user)

@app.route('/user/<user>')
def user_page(user):
    if not st_login.is_login():
        return redirect('/login')
    if st_login.is_resistered(user):
        user_name = st_login.get_rival_user_name(user)
        spuc_data, num_data = score_check.get_spuc_data(user)
        if user == st_login.get_user_id():
            return render_template('index.html',
                            user=user,
                            user_name=user_name,
                            spuc_data=spuc_data[6:],
                            num_data=num_data[6:])
        else:
            if not st_settings.get_rival_settings(user):
                spuc_data = ["---"] * 20
            return render_template('user_page.html',
                            user=user,
                            user_name=user_name,
                            is_resistered=rival_resister.is_resistered(user),
                            spuc_data=spuc_data[6:],
                            num_data=num_data[6:])
    return redirect('/')

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
    return render_template('signup.html')

@app.route('/login/signup/try', methods=['POST'])
def try_signup():
    user = request.form.get('user', '')
    pw = request.form.get('pw', '')
    mode = st_signup.try_signup(user, pw)
    if mode == '成功':
        return redirect('/login')
    return render_template('signup_error.html',
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
        hi_score_data, resister_error_data = score_resister.update_score(score_txt_data)
        if type(hi_score_data) == type(False):
            return render_template('resister.html')
    return render_template('hiscore.html',
                            hi_score_list=hi_score_data,
                            data_num=len(hi_score_data),
                            resister_error_list=resister_error_data,
                            mode='今回')

@app.route('/hiscore')
def recently_hiscore():
    if not st_login.is_login():
        return redirect('/login')
    hi_score_data = score_resister.get_hi_score_data()
    return render_template('hiscore.html',
                            hi_score_list=hi_score_data,
                            data_num=len(hi_score_data),
                            resister_error_list=[],
                            mode='直近')

@app.route('/myscore')
def myscore():
    if not st_login.is_login():
        return redirect('/login')
    return render_template('myscore.html')

@app.route('/myscore/<level>')
def level_myscore(level):
    if not st_login.is_login():
        return redirect('/login')
    level = int(level)
    if level < 1 or level > 20:
        return redirect('/')
    my_score_data = score_check.get_my_score_data(level)
    return render_template('level_myscore.html',
                            level=level,
                            my_score_list=my_score_data)

@app.route('/ranking/<effect_id>')
def ranking(effect_id):
    if not st_login.is_login():
        return redirect('/login')
    effect_id = int(effect_id)
    effect_data, ranking_data = score_check.get_ranking_data(effect_id)
    if type(ranking_data) == type(False):
        return redirect('/')
    return render_template('ranking.html',
                            effect_data=effect_data,
                            ranking_list=ranking_data)

@app.route('/strengths')
def strengths():
    if not st_login.is_login():
        return redirect('/login')
    strengths_list = st_strengths.get_strengths()
    return render_template('strengths.html',
                            strengths_list=strengths_list,
                            data_num=len(strengths_list))

@app.route('/notice')
def notice():
    if not st_login.is_login():
        return redirect('/login')
    notice_list = st_notice.get_notice()
    return render_template('notice.html',
                            notice_list=notice_list,
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
    return render_template('rival-search.html')

@app.route('/rival/search/try', methods=['POST'])
def follow_rival():
    if not st_login.is_login():
        return redirect('/login')
    search_id = request.form.get('search-id')
    if not rival_resister.is_exist(search_id):
        return redirect('/rival/search')
    return redirect('/user/' + search_id)

@app.route('/rival/resister/<rival>')
def try_follow_rival(rival):
    if not st_login.is_login():
        return redirect('/login')
    if not rival_resister.is_exist(rival):
        return redirect('/')
    if rival == st_login.get_user_id():
        return redirect('/')
    if rival_resister.is_resistered(rival):
        rival_resister.remove_rival(rival)
        return redirect('/user/' + rival)
    rival_resister.follow_rival(rival)
    return redirect('/user/' + rival)

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