from app.models.article import Article


def add_article(args, result):
    title = args[0]
    author = args[1]
    content = args[2]
    article = Article(title=title, author=author, content=content)
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
        article_list.append(single_article)
    return article_list



