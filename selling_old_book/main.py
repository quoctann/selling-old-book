from selling_old_book import app, db, login
from flask import Flask, render_template, request, redirect, url_for, session
import hashlib, os, json, csv
from flask_login import login_user, logout_user, login_required, current_user
from selling_old_book.admin import *


def get_book():
    books = BookStorage.query
    return books.all()


@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    product_list = get_book()
    # Chuyển string sang list
    for item in product_list:
        # eval() bỏ dấu nháy đơn sring khi vừa get từ db về
        item.img_path = eval(item.img_path)
        # tách ra thành từng phần riêng trong list
        parser = csv.reader(item.img_path)
    return render_template('common_view/index.html', product_list=product_list)


@app.route("/login-admin", methods=["GET", "POST"])
# Phương thức này được gọi từ login.html
def login_admin():
    # Reset bộ nhớ tạm của admin
    if request.method == "POST":
        # Lấy dữ liệu từ form (thông qua request)
        username = request.form.get("loginUsername")
        password = request.form.get("loginPassword")
        # Dùng thuật toán MD5 băm mã ra dưới dạng hexa
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        # Strip() dùng để bỏ khoảng trắng ở hai đầu chuỗi ký tự
        user = User.query.filter(User.username == username,
                                 User.password == password).first()
        # Nếu không giá trị thì trả về null
        if user:
            login_user(user=user)

    # Thực tế là chuyển đến trang admin -> index.html
    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)
