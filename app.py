from flask import Flask, render_template, session, redirect
from flask.globals import request
import st_login
import st_data
import st_signup
import score_resister

app = Flask(__name__)
app.secret_key = 'Rjr7GwR3hkq1h'

@app.route('/')
def index():
    if not st_login.is_login():
        return redirect('/login')
    return render_template('index.html')

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
    st_signup.try_signup(user, pw)
    return redirect('/')
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
    #スコア登録した後に以下のデータを読み込み...
    #EXスコアデータ
    #譜面IDデータ
    #逆参照譜面IDデータ
    #ユーザデータ
    return render_template('resister.html')

@app.route('/resister/hiscore', methods=['POST'])
def hiscore():
    if not st_login.is_login():
        return redirect('/login')
    if 'score' in request.form:
        score_txt_data = str(request.form['score'])
        user = "id00000"
        score_resister.update_score(user, score_txt_data)
    user_data = st_data.load_user_data()

    return render_template('hiscore.html',
                            hi_score_list=user_data[user]["hi-score"][0:],
                            data_num=len(user_data[user]["hi-score"][0:]))

@app.route('/notice')
def notice():
    if not st_login.is_login():
        return redirect('/login')
    #ユーザデータ
    return render_template('notice.html')

@app.route('/rival')
def rival():
    if not st_login.is_login():
        return redirect('/login')
    #ユーザデータ
    #ユーザIDを乱数にするべき(4桁-4桁)
    return render_template('rival.html')
#改良する必要がある

@app.route('/rival/follow')
def rival_follow():
    if not st_login.is_login():
        return redirect('/login')
    return render_template('rival-list.html')

@app.route('/rival/follower')
def rival_follower():
    if not st_login.is_login():
        return redirect('/login')
    return render_template('rival-list.html')

@app.route('/rival/search')
def rival_search():
    if not st_login.is_login():
        return redirect('/login')
    return render_template('rival-search.html')

@app.route('/settings')
def settings():
    if not st_login.is_login():
        return redirect('/login')
    #ユーザデータ
    return render_template('settings.html')

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0')

#http://localhost:5000