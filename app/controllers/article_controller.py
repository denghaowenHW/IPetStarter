from app.models.article import Article


def add_article(args, result):
    title = args[0]
    author = args[1]
    content = args[2]
    article = Article(title=title, author=author, content=content)
    article.save()
    result['status'] = 'success'


def del_article(article_id, result):
    Article.objects.filter(_id=article_id).delete()
    result['status'] = 'success'







