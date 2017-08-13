from flask import Flask,render_template,request,redirect,jsonify
from flask_login import LoginManager, login_required, login_user, logout_user,current_user
app = Flask(__name__)
from db.User import User
from tools.dbtools import Session
import re

app.config.update(
    DEBUG = True,
    TEMPLATES_AUTO_RELOAD = True,
    SECRET_KEY = 'SECRET_KEY',
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route('/')
@login_required
def home():
    '''session = Session()
    session.expire_on_commit = False

    new_user = User()
    new_user.Email = '4@m.com'
    new_user.Name = 'Alvaro Jpse'
    new_user.Password = '123'
    session.add(new_user)
    try:
        session.commit()
        session.close()
        return 'Registro Grabado: %i' % new_user.id
    except Exception as e:
        session.rollback()
        session.close()
        return str(e)

    session = Session()
    records = session.query(User)
    l = []
    for record in records:
        l.append(record.Email)
    return str(l) '''
    return render_template('index.html',username=current_user.Name)

# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username: username = username.replace(" ", "")
        user = User.getUserIdByEmail(username)
        password = request.form['password']
        if username or password:
            if not password or not username:
                return render_template('login.html',error_msg='Debe Ingresar Usuario y Password',signUp=False)
            if not user:
                return render_template('login.html',error_msg='Usuario no Registrado',signUp=False)
            if (user.Password == password):
                if login_user(user):
                    return redirect('/')
        return render_template('login.html',error_msg='Datos Incorrectos',signIn=False)
    else:
        return render_template('login.html',signUp=False)

# somewhere to login
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        username1 = request.form['username1']
        username2 = request.form['username2']
        if username1: username1 = username1.replace(" ", "")
        if username2: username2 = username2.replace(" ", "")
        password1 = request.form['password1']
        password2 = request.form['password2']
        name = request.form['name']
        if password1 or password2 or username1 or username2:
            if not username1 or not username2:
                return render_template('login.html', error_msg='Debe Ingresar Email',signUp=True)
            if username1 != username2:
                return render_template('login.html', error_msg='Los Email no coinciden')
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', username1)
            if not match:
                return render_template('login.html',error_msg='Debe ingresar un correo válido')
            user = User.getUserIdByEmail(username1)
            if user:
                return render_template('login.html',error_msg='Usuario ya registrado: %s' % username1, signUp=True)
            if password1 != password2:
                return render_template('login.html', error_msg='Los Password no coinciden',signUp=True)
            new_user = User.addNewUser(username1, password1, name)
            if new_user:
                login_user(new_user)
                return redirect('/')
            else:
                return render_template('login.html', error_msg=new_user, signUp=True)
        return render_template('login.html', error_msg='Datos Incorrectos', signIn=False)

    else:
        return render_template('login.html', signUp=False)


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('login.html',signUp=False)
    #return Response('<p>Logged out</p>')

# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

@app.route("/_get_users_list")
@login_required
def get_users_list():
    session = Session()
    records = session.query(User)
    l = []
    for record in records:
        user_json = record.toJSON()
        l.append(user_json)
    return jsonify(result=l)

@app.route("/users")
@login_required
def users():
    return render_template('users.html', username=current_user.Name)


if __name__ == "__main__":
    app.run(host= '0.0.0.0')

