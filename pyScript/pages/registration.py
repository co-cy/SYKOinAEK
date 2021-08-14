from pyScript.database.manager_db import manager_db
from flask import Blueprint, jsonify, current_app
from pyScript.forms.forms import RegistrationForm
from pyScript.database.tables.users import User
from flask_login import login_user


blueprint = Blueprint('register', __name__)


# TODO: Сделать типизацию нормально
def check_valid_data_from_form(form: RegistrationForm):
    user = User.query.filter_by(email=form.email.data).first()

    if user:
        form.email.errors.append('Пользователь с такой почтой уже зарегистрирован')
        return False

    if form.password != form.repeat_password:
        form.email.errors.append('Пароли не совпадают')
        return False

    return user


@blueprint.route('/reg', methods=['POST'])
@blueprint.route('/register', methods=['POST'])
@blueprint.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():

        result = check_valid_data_from_form(form)
        if result:
            # Добавление в базу данных пользователя
            with current_app.app_context():
                user = User(form.email.data, form.password.data)
                manager_db.session.add(user)
                manager_db.session.commit()
            # Авторизация пользователя

            # TODO fix login_user (error in login) when use login_user(user) + register_page
            login_user(User.query.filter_by(email=form.email.data).first(), remember=True)
            return jsonify({"status": "OK"})

    return jsonify({"status": "NOT"})
