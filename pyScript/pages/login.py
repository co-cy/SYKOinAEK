from pyScript.database.tables.users import User
from pyScript.forms.forms import LoginForm
from flask import Blueprint, jsonify

blueprint = Blueprint('login', __name__)


# TODO: Сделать типизацию нормально
def check_valid_data_from_form(form: LoginForm):
    user = User.query.filter_by(email=form.email.data).first()

    if not user:
        form.email.errors.append('Пользователь с такой почтой не найден')
        return False

    if user.check_password():
        form.email.errors.append('Пароли не совпадают')
        return False

    return user


@blueprint.route('/l', methods=['POST'])
@blueprint.route('/login', methods=['POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        result = check_valid_data_from_form(form)
        if result:
            return jsonify({"status": "OK"})

    return jsonify({"status": "NOT OK"})
