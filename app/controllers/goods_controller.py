from app.models.goods import Goods


def add_goods(args, result):
    name = args[0]
    price = float(args[1])
    goods = Goods(name=name, price=price)
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




