from main import db
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    @property
    def user_name(self):
        return self._user_name

    @property
    def key(self):
        return self._key

    __tablename__ = 'users'
    __id = db.Column('id', db.Integer, primary_key=True)
    __user_name = db.Column('user_name', db.String(50), nullable=False, unique=True)
    __email = db.Column('email', db.String(50), nullable=False, unique=True, index=True)
    __key = db.Column('key', db.String(120), nullable=False, unique=True)

    def __int__(self, user_name, email, key):
        self.__user_name = user_name
        self.__email = email
        self.__key = key

    def __repr__(self):
        return f'{self.__id}, {self.__user_name}, {self.__email},{self.__key}'

    @hybrid_property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @hybrid_property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    @user_name.deleter
    def user_name(self):
        del self.__user_name

    @hybrid_property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email

    @hybrid_property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @key.deleter
    def key(self):
        del self.__key
