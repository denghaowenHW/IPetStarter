from app.models.goods import Goods


def add_goods(args, result):
    name = args[0]
    price = float(args[1])
    label = args[2]
    goods = Goods(name=name, price=price, label=label)
    goods.save()
    result['status'] = 'success'


def del_goods(goods_id, result):
    goods = Goods.objects(_id=goods_id)
    if goods:
        goods.delete()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'goods not exist'


def edit_goods(args, result):
    goods_id = args[0]
    edit_type = args[1]
    edit_content = args[2]
    goods = Goods.objects(_id=goods_id).first()
    if goods:
        if edit_type == 'price':
            goods[edit_type] = float(edit_content)
        else:
            goods[edit_type] = edit_content
        goods.save()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'goods not exist'


def get_all_goods():
    goods_list = list()
    all_goods = Goods.objects()
    for goods in all_goods:
        single_goods = dict()
        single_goods['_id'] = str(goods['_id'])
        single_goods['name'] = goods['name']
        single_goods['price'] = goods['price']
        single_goods['label'] = goods['label']
        goods_list.append(single_goods)
    return goods_list


def search_goods_by_label(required_label):
    tmp_list = list()
    all_goods = Goods.objects()
    for goods in all_goods:
        # whether list has contains relationship
        if set(required_label) <= set(goods.label):
            tmp_list.append(goods)
    return tmp_list
