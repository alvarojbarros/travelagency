from flask import Flask,render_template,request,redirect
from flask_login import LoginManager, login_required, login_user, logout_user,current_user
app = Flask(__name__)
from db.User import User
from tools.dbtools import Session

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
    return '<a href="/logout">LOGIUT</a>'

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


if __name__ == "__main__":
    app.run(host= '0.0.0.0')

