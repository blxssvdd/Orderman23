from flask_wtf import FlaskForm
import wtforms


class ProductForm(FlaskForm):
    name = wtforms.StringField("Введіть своє ім'я")
    products = wtforms.SelectMultipleField("Виберіть піццу")
    submit = wtforms.SubmitField("Замовити")


class ReviewForm(FlaskForm):
    name = wtforms.StringField("Введіть своє ім'я")
    grades = wtforms.SelectField("Виберіть оцінку")
    review = wtforms.TextAreaField("Напишіть свій відгук")
    submit = wtforms.SubmitField("Відправити відгук")