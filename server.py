import os
from flask_app import db

from flask_app.__init__ import createApp

os.environ['FLASK_ENV_TYPE'] = 'Development'

if os.environ['FLASK_ENV_TYPE'] == 'Development':
    from config.development import Development as Config
elif os.environ['FLASK_ENV_TYPE'] == 'Production':
    from config.production import Production as Config
else:
    raise Exception('Not proper FLASK_ENV_TYPE set.')


app = createApp(Config)



@app.route('/')
def hello():
    db.create_all()
    return "Hello :D"
