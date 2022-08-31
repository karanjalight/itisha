from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#database connection
database_path = 'postgresql://postgres:postgres@localhost:5432/itisha'

db = SQLAlchemy()



#setup_db(app)========= binds a flask application and a SQLAlchemy service

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    db.app = app
    migrate = Migrate(app)


class Question(db.Model):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    







def hello():
    print('hello world!')
    return f'hello world'

print('what more can I do')
print(hello)