from flask import Flask
app = Flask(__name__)
from db.User import User
from tools.dbtools import Session

app.config.update(
    DEBUG = True,
    TEMPLATES_AUTO_RELOAD = True,
    SECRET_KEY = 'SECRET_KEY',
)

@app.route('/')
#@login_required
def home():
    session = Session()
    session.expire_on_commit = False

    '''new_user = User()
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
        return str(e) '''
    session = Session()
    records = session.query(User)
    l = []
    for record in records:
        l.append(record.Email)
    return str(l)




if __name__ == "__main__":
    app.run(host= '0.0.0.0')

