from flask import*
import secrets
import mysql.connector

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

mydb = Flask(__name__)
app.secret_key = secrets.token_hex(16)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="projectx",
    password=""
)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('home.html')

@app.route('/aksi_login', methods =["POST", "GET"])
def aksi_login():
    cursor = mydb.cursor()
    query = ("select * from user where username = %s and password = %s")
    data = (request.form['username'], request.form['password'],)
    cursor.execute( query, data )
    value = cursor.fetchone()
    
    username = request.form['username']
    if value:
        session["user"] = username
        return f"BERHASIL LOGIN...."
    else:
        return f"salah !!!"
    

if __name__ == "__main__":
    app.run(debug=True)












# @app.route('/admin')
# def admin():
#     if session.get("user"):
#         return render_template("admin.html")
#     else:
#         return redirect(url_for("home"))
        

# @app.route('/anggota')
# def anggota():
#     return render_template("anggota.html")

# @app.route('/login', methods=["POST", "GET"])
# def login():
#     username = request.form['username']
#     password = request.form['password']
#     if username == userAdmin["username"] and password == userAdmin["password"]:
#         session["user"] = username
#         return redirect(url_for('admin'))
#     elif username == userAnggota["username"] and password == userAnggota["password"]:
#         session["user"] = username
#         return redirect(url_for('anggota'))
#     else:
#         return f"salah...."

# @app.route('/logout')
# def logout():
#     session.pop("user", None)
#     return redirect(url_for("home"))

# if __name__ == "__main__":
#     app.run(debug=True)