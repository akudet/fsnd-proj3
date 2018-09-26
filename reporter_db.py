import psycopg2

DBNAME = "news"


def fetch_all(query, params):
    """
    execute a query and fetch all result from it
    :param query: the query to execute
    :param params: parameters of the query
    :return: result of this query
    """
    # it's kind time consuming every time we open and close a connection
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query, params)
    ret = c.fetchall()
    db.close()
    return ret


def article_views(cnt=None):
    """
    statistics about article views, article is consider a view if exists
    a http request for the article path with GET method and 200 status code
    :param cnt: int, optional
        max number of articles
    :return:
        list of (article name, view_cnt) pair ordered by views in desc order
    """
    query = """
    select title, view_cnt
    from articles, view_stat
    where concat('/article/', slug) = path
    order by view_cnt desc
    """
    if cnt is not None:
        query += "limit (%s)"
        params = (cnt,)
    else:
        params = ()
    return fetch_all(query, params)


def author_views(cnt=None):
    """
    statistics about author's all articles views
    :param cnt: int, optional
        max number of authors
    :return:
        list of (author name, view_cnt) pair ordered by views in desc order
    """
    query = """
    select name, sum(view_cnt) as view_cnt
    from articles, view_stat, authors
    where concat('/article/', slug) = path
      and articles.author = authors.id
    group by authors.id
    order by view_cnt desc
    """
    if cnt is not None:
        query += "limit (%s)"
        params = (cnt,)
    else:
        params = ()
    return fetch_all(query, params)


def error_stat(threshold):
    """
    error rate stat by day, error rate is defined as total number of failed
    requests(status is not 200) divided by the total number of requests a day.
    if a day don't have any requests it will be ignored
    :param threshold: double
        error rate bigger or equal threshold will be returned
    :return: list of (date, error rate)
    """
    query = """
    select date(time) as stat_date,
        sum(cast(status != '200 OK' as integer))
        / cast(count(*) as real) as error_rate
    from log
    group by stat_date
    having
        sum(cast(status != '200 OK' as integer))
        / cast(count(*) as real) >= (%s);
    """
    return fetch_all(query, (threshold,))
