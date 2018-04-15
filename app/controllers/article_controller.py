from app.models.article import Article
from app.models.user import User
from app.utils.common import get_current_time
import uuid


def add_article(args, result):
    title = args[0]
    author = args[1]
    content = args[2]
    label = args[3]
    article = Article(title=title, author=author, content=content, label=label)
    article.save()
    result['status'] = 'success'


def del_article(article_id, result):
    article = Article.objects(_id=article_id)
    if article:
        article.delete()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'article not exist'


def edit_article(args, result):
    article_id = args[0]
    edit_type = args[1]
    edit_content = args[2]
    article = Article.objects(_id=article_id).first()
    if article:
        article[edit_type] = edit_content
        article.save()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'article not exist'


def get_all_article():
    article_list = list()
    articles = Article.objects()
    for article in articles:
        single_article = dict()
        single_article['_id'] = str(article['_id'])
        single_article['title'] = article['title']
        single_article['author'] = article['author']
        single_article['content'] = article['content']
        single_article['point_praise_user_list'] = article['point_praise_user_list']
        single_article['comment_list'] = article['comment_list']
        single_article['label'] = article['label']
        article_list.append(single_article)
    return article_list


def get_likes_num(id):
    article = Article.objects(_id=id).first()
    if article:
        return len(article['point_praise_user_list'])
    else:
        raise Exception('article not exist')


def click_likes(args, result):
    id = args[0]
    phone_num = args[1]
    article = Article.objects(_id=id).first()
    if article:
        likes_list = article['point_praise_user_list']
        user = User.objects(phone_num=phone_num).first()
        if user:
            if phone_num in likes_list:
                likes_list.remove(phone_num)
            else:
                likes_list.append(phone_num)
            article.save()
            result['status'] = 'success'
        else:
            result['status'] = 'fail'
            result['msg'] = 'user not exist'
    else:
        result['status'] = 'fail'
        result['msg'] = 'article not exist'


def get_likes_status(args, result):
    id = args[0]
    phone_num = args[1]
    article = Article.objects(_id=id).first()
    if article:
        likes_list = article['point_praise_user_list']
        if phone_num in likes_list:
            result['is_like'] = True
    else:
        result['status'] = 'fail'
        result['msg'] = 'article not exist'


def add_comment(args, result):
    id = args[0]
    phone_num = args[1]
    comment = args[2]
    article = Article.objects(_id=id).first()
    user = User.objects(phone_num=phone_num).first()
    if article and user:
        tmp_comment = dict()
        tmp_comment['comment_id'] = str(uuid.uuid1()).replace('-', '')
        tmp_comment['account'] = user.account
        tmp_comment['comment'] = comment
        tmp_comment['time'] = get_current_time()
        comment_list = article.comment_list
        comment_list.append(tmp_comment)
        article.save()
        result['status'] = 'success'
    else:
        result['status'] = 'fail'
        result['msg'] = 'article or user not exist'


def get_comments(id):
    article = Article.objects(_id=id).first()
    if article:
        return article.comment_list
    else:
        raise Exception('article not exist')


def del_comment(args, result):
    comment_id = args[0]
    article_id = args[1]
    article = Article.objects(_id=article_id).first()
    if article:
        comment_list = article.comment_list
        for comment in comment_list:
            if comment['comment_id'] == comment_id:
                comment_list.remove(comment)
                article.save()
                result['status'] = 'success'
                break
        else:
            result['status'] = 'fail'
            result['msg'] = 'comment not exist'
    else:
        result['status'] = 'fail'
        result['msg'] = 'article not exist'


def search_articles_by_label(required_label):
    tmp_list = list()
    articles = Article.objects()
    for article in articles:
        # whether list has contains relationship
        if set(required_label) <= set(article.label):
            tmp_list.append(article)
    return tmp_list
