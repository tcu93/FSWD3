import psycopg2

DBNAME = "news"

QUERY_ARTICLES = """
        SELECT
	        title,count(*) as num
	    FROM articles, log
        WHERE log.path = '/article/' || articles.slug
        GROUP BY title
        ORDER BY num desc
        LIMIT 3;
        """

QUERY_AUTHORS = """
        SELECT
	        authors.name,count(*) as num
	    FROM articles,log,authors
        WHERE authors.id=articles.author AND path
            = '/article/' || slug
	    GROUP BY authors.name
        ORDER BY num desc;
        """

QUERY_ERRORS = """
        SELECT
            to_char(err_by_day.date,'FMMonth DD, YYYY') as date,
            to_char(((err_by_day.count::decimal
                    /req_by_day.count::decimal)*100)
                    ,'9.99') || '%' as percentage
        FROM
            (SELECT date(time),count(*) FROM log
                        GROUP BY date(time)) as req_by_day,
            (SELECT date(time),count(*) FROM log WHERE status = '404 NOT FOUND'
                        GROUP BY date(time)) as err_by_day
        WHERE
            req_by_day.date = err_by_day.date
            AND ((err_by_day.count::decimal
                    /req_by_day.count::decimal)*100) > 1;
        """

"""Define single DB query method"""
def get_query(query):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

def articles():
    return get_query(QUERY_ARTICLES)

def authors():
    return get_query(QUERY_AUTHORS)

def errors():
    return get_query(QUERY_ERRORS)
