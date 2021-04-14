from selling_old_book import app, db, login
from flask import Flask, render_template, request, url_for, session, jsonify
import json, csv, hashlib
from flask_login import login_user, logout_user, current_user
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
    # Parse String to List
    for item in product_list:
        # eval() to delete '' at two ends of String
        item.img_path = eval(item.img_path)
        # Separate each element in the String into a List
        # parser = csv.reader(item.img_path)
        print(item.img_path)
    return render_template('common_view/index.html', product_list=product_list)


@app.route("/login-admin", methods=["GET", "POST"])
# Called from admin/login.html
def login_admin():
    if request.method == "POST":
        # Get data from form
        username = request.form.get("loginUsername")
        password = request.form.get("loginPassword")
        # Password hashes using the MD5 algorithm, strip() to delete white space two ends of pswrd
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.username == username,
                                 User.password == password).first()
        # Return None if don't have a valid user
        if user:
            login_user(user=user)

    # Redirect to admin/index.html
    return redirect("/admin")


# API Increase likes
@app.route("/api/like", methods=["POST"])
def add_like():
    data = json.loads(request.data)
    like_count = int(data.get("likeCount"))
    product_id = int(data.get("id"))
    product = BookStorage.query.filter_by(id=product_id).first()
    product.like += like_count
    db.session.commit()
    return jsonify({
        'likeCount': product.like
    })


if __name__ == "__main__":
    app.run(debug=True)
