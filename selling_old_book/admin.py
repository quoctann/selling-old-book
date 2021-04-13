from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask import redirect, session
from selling_old_book import admin, db
from selling_old_book.models import BookStorage, User
from flask_login import current_user, logout_user


class AuthenticatedView(BaseView):
    __abstract__ = True

    def is_accessible(self):
        return current_user.is_authenticated


class ModelAuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(AuthenticatedView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect("/admin")


admin.add_view(ModelAuthenticatedView(BookStorage, db.session))
admin.add_view(LogoutView(name="Đăng xuất"))
