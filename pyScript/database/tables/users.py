from werkzeug.security import generate_password_hash, check_password_hash
from pyScript.database.manager_db import manager_db
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from datetime import datetime


class User(manager_db.Model, UserMixin, SerializerMixin):
    id = manager_db.Column(manager_db.Integer, primary_key=True, autoincrement=True, nullable=False)

    email = manager_db.Column(manager_db.String(32), unique=True, index=True, nullable=False)
    password = manager_db.Column(manager_db.String(128), nullable=False)

    permissions = manager_db.Column(manager_db.Integer, default=0, nullable=False)

    balance = manager_db.Column(manager_db.Integer, default=0, nullable=False)
    date_registered = manager_db.Column(manager_db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self, email: str, password: str, balance: int = None, permissions: int = None):
        # TODO add validators

        self.email = email
        self.password = generate_password_hash(password)

        if permissions is not None:
            self.permissions = permissions

        if balance is not None:
            self.balance = balance

    def check_password(self, other_password: str, need_hash: bool = True) -> bool:
        if need_hash:
            other_password = generate_password_hash(other_password)

        return check_password_hash(self.password, other_password)


