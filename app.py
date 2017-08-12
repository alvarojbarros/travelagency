from flask import Flask
app = Flask(__name__)

app.config.update(
    DEBUG = True,
    TEMPLATES_AUTO_RELOAD = True,
    SECRET_KEY = 'SECRET_KEY',
)

@app.route('/')
#@login_required
def home():
    return 'HOLA MUNDO'


if __name__ == "__main__":
    app.run(host= '0.0.0.0')

