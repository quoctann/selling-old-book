from sqlalchemy import Column, Integer, String, Boolean
from selling_old_book import db
from flask_login import UserMixin


class AuthIndentityBase(db.Model, UserMixin):
    __abstract__ = True
    username = Column(String(20), nullable=False)
    password = Column(String(40), nullable=False)

    def __str__(self):
        return self.name


class BookStorage(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    img_path = Column(String(255), nullable=False)
    condition = Column(String(100), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    like = Column(Integer, nullable=False, default=0)


class User(AuthIndentityBase):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(60), nullable=False)


if __name__ == "__main__":
    db.create_all()
