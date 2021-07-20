from flask import Flask, render_template
import st_login
import st_data

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello."

@app.route('/login')
def login():
    return "Hello."

@app.route('/try_login')
def try_login():
    return "Hello."

@app.route('/logout')
def logout():
    return "Hello."

@app.route('/resister')
def resister():
    return "Hello."

@app.route('/notice')
def notice():
    return "Hello."

@app.route('/rival')
def rival():
    return "Hello."
#改良する必要がある

@app.route('/setting')
def setting():
    return "Hello."

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0')

#http://localhost:5000