from app.models.user import User
from app.models.goods import Goods
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


def create_user(args, result):
    phone_num = args[0]
    account = args[1]
    password = args[2]
    # password: add salt and hash
    password = generate_password_hash(password)
    # check account and phone_num unique
    # register user
    user = User(account=account, password=password, phone_num=phone_num)
    user.save()
    result['status'] = 'success'


def check_password(args, result):
    phone_num = args[0]
    input_pwd = args[1]
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


def change_balance(args, result):
    phone_num = args[0]
    money = args[1]
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


def create_pet(args, result):
    phone_num = args[0]
    pet_name = args[1]
    pet_age = args[2]
    pet_type = args[3]
    user = User.objects(phone_num=phone_num).first()
    if user:
        pet_info = dict()
        pet_info['pet_id'] = str(uuid.uuid1()).replace('-', '')
        pet_info['pet_name'] = pet_name
        pet_info['pet_age'] = pet_age
        pet_info['pet_type'] = pet_type
        pet_info['notice'] = dict()
        user.pets_list.append(pet_info)
        user.save()
        result['status'] = 'success'
        return result
    else:
        result['status'] = 'fail'
        result['msg'] = 'user phone_num not exist'


def remove_pets(args, result):
    phone_num = args[0]
    pet_id_list = args[1]
    user = User.objects(phone_num=phone_num).first()
    if user:
        pets_list = user.pets_list
        for pet_id in pet_id_list:
            for pet in pets_list:
                if pet['pet_id'] == pet_id:
                    user.pets_list.remove(pet)
        user.save()
        result['status'] = 'success'
        return result
    else:
        result['status'] = 'fail'
        result['msg'] = 'user phone_num not exist'


def add_notice(args, result):
    phone_num = args[0]
    pet_id = args[1]
    notice_content = args[2]
    time = args[3]
    user = User.objects(phone_num=phone_num).first()
    if user:
        for pet in user.pets_list:
            if pet['pet_id'] == pet_id:
                pet['notice'][time] = notice_content
                break
        else:
            result['status'] = 'fail'
            result['msg'] = 'pet not exist'
        user.save()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'user phone num not exist'


def del_notice(args, result):
    phone_num = args[0]
    pet_id = args[1]
    time = args[2]
    user = User.objects(phone_num=phone_num).first()
    if user:
        for pet in user.pets_list:
            if pet['pet_id'] == pet_id:
                pet['notice'].pop(time)
                break
        else:
            result['status'] = 'fail'
            result['msg'] = 'pet not exist'
        user.save()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'user phone num not exist'


def get_user_info(phone_num, info_type):
    user = User.objects(phone_num=phone_num).first()
    if user:
        if info_type == 'base':
            tmp_user = dict()
            tmp_user['account'] = user.account
            tmp_user['balance'] = user.balance
            return tmp_user
        elif info_type == 'pets':
            return user.pets_list
        elif info_type == 'cart':
            return user.cart
    else:
        raise Exception('user not exist')


def del_cart(args, result):
    goods_id = args[0]
    phone_num = args[1]
    user = User.objects(phone_num=phone_num).first()
    if user:
        for one in user.cart:
            print one['goods_id']
            if one['goods_id'] in goods_id:
                user.cart.remove(one)
        user.save()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'user not exist'


def put_cart(args, result):
    goods_id = args[0]
    phone_num = args[1]
    goods_num = args[2]
    user = User.objects(phone_num=phone_num).first()
    goods = Goods.objects(_id=goods_id).first()
    if user and goods:
        for cart in user.cart:
            if cart['goods_id'] == goods_id:
                cart['good_num'] = goods_num
                cart['goods_price'] = float(goods.price) * int(goods_num)
                break
        else:
            goods_info = dict()
            goods_info['goods_id'] = goods_id
            goods_info['goods_name'] = goods.name
            goods_info['goods_price'] = float(goods.price) * int(goods_num)
            goods_info['good_num'] = goods_num
            user.cart.append(goods_info)
        user.save()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'user or goods not exist'
