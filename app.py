from flask import Flask, render_template, request, json
from flaskext.mysql  import MySQL
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ginobili00'
app.config['MYSQL_DATABASE_DB'] = 'list'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn=mysql.connect()


@app.route("/")

def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signup',methods=['POST'])
def signup():
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    # validate the received values
    if _name and _email and _password:
        
        add_utente=("INSERT INTO utenti (nome, username, password) values (%s, %s, %s)")
        dati=(_name, _email, _password)
        cursor=conn.cursor()
        cursor.execute(add_utente, dati)
        conn.commit()
        cursor.close()
        conn.close()
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__=="__main__":
    app.run(debug=True)
