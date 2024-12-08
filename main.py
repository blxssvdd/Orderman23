from flask import Flask, render_template, redirect, url_for, request

from app.db.base import Session, create_db
from app.db import models
from app.forms import forms


app = Flask(__name__)
app.secret_key = "123"


@app.route("/", methods=["GET", "POST"])
def index():
    with Session() as session:
        products = session.query(models.Product).all()
        product_form = forms.ProductForm()
        product_form.products.choices = []

        for product in products:
            product_form.products.choices.append((product.name, product.name))

        if request.method == "POST":
            name = product_form.name.data
            products = product_form.products.data
            products_db = []

            for product in products:
                product_db = session.query(models.Product).where(models.Product.name == product).first()
                products_db.append(product_db)

            shop_list = models.ShopList(name=name, products=products_db)
            session.add(shop_list)
            session.commit()

        return render_template("index.html", form=product_form)


@app.route("/review/", methods=["GET", "POST"])
def review():
    with Session() as session:
        review_form = forms.ReviewForm()
        review_form.grades.choices = [(1, 1), (2, 2), (3, 3)]
        grades = session.query(models.Grade).all()

        for grade in grades:
            review_form.grades.choices.append((grade.grade, grade.grade))

        if request.method == "POST":
            name = review_form.name.data
            grade = review_form.grades.data
            grade_db = session.query(models.Grade).where(models.Grade.grade == grade).first()
            text = review_form.review.data

            review_db = models.Review(name=name, grade=grade_db, text=text)
            session.add(review_db)
            session.commit()

        return render_template("review.html", form=review_form)



if __name__ == "__main__":
    create_db()
    app.run(debug=True)