from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash


def create_user(account, password, phone_num, result):
    # password: add salt and hash
    password = generate_password_hash(password)
    # check account and phone_num unique
    # register user
    user = User(account=account, password=password, phone_num=phone_num)
    user.save()
    result['status'] = 'success'


def check_password(phone_num, input_pwd, result):
    user = User.objects(phone_num=phone_num).first()
    if user:
        password = user.password
        if check_password_hash(password, input_pwd):
            result['status'] = 'success'
        else:
            result['status'] = 'fail'
            result['msg'] = 'password incorrect'
    else:
        result['status'] = 'fail'
        result['msg'] = 'user phone_num not exist'


def change_balance(phone_num, money, result):
    user = User.objects(phone_num=phone_num).first()
    if user:
        balance = user.balance + float(money)
        if balance <= 0:
            result['status'] = 'fail'
            result['msg'] = 'balance not enough'
        else:
            user.balance = balance
            user.save()
            result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'user phone_num not exist'
