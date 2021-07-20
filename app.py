from flask import Flask, render_template, session
import st_login
import st_data

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/try')
def try_login():
    #ユーザデータ
    return render_template('form.html')

@app.route('/login/signup')
def signup():
    #ユーザデータ
    return render_template('form.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/resister')
def resister():
    #スコア登録した後に以下のデータを読み込み...
    #EXスコアデータ
    #譜面IDデータ
    #逆参照譜面IDデータ
    #ユーザデータ
    return render_template('resister.html')

@app.route('/notice')
def notice():
    #ユーザデータ
    return render_template('notice.html')

@app.route('/rival')
def rival():
    #ユーザデータ
    #ユーザIDを乱数にするべき(4桁-4桁)
    return render_template('rival.html')
#改良する必要がある

@app.route('/rival/follow')
def rival_follow():
    return render_template('rival-list.html')

@app.route('/rival/follower')
def rival_follower():
    return render_template('rival-list.html')

@app.route('/rival/search')
def rival_search():
    return render_template('rival-search.html')

@app.route('/settings')
def settings():
    #ユーザデータ
    return render_template('settings.html')

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0')

#http://localhost:5000