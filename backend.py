import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


ENGINE = sqlalchemy.create_engine("mariadb+mariadbconnector://admin:admin@localhost/pyqt_phonebook")
BASE = declarative_base()


class User(BASE):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String(length=100), unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(length=100))
    date = sqlalchemy.Column(sqlalchemy.Date())
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    remember_session = sqlalchemy.Column(sqlalchemy.Boolean, default=False)


class Phonebook(BASE):
    __tablename__ = 'phonebook'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=100))
    phone = sqlalchemy.Column(sqlalchemy.String(length=20), unique=True)
    date = sqlalchemy.Column(sqlalchemy.Date())


def setup_db():
    BASE.metadata.create_all(ENGINE)
    session = sqlalchemy.orm.sessionmaker()
    session.configure(bind=ENGINE)
    session = session()
    return session
