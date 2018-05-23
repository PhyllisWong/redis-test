import json
from flask import Flask, request
from models import db


app = Flask(__name__)
# app config
db.init_app(app)


POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/person')
def person_route():
    person = {'name': 'Phyllis', 'age': 100}
    json_person = json.dumps(person)
    return (json_person, 200, None)


if __name__ == '__main__':
    app.run()
    app.config['DEBUG'] = True
