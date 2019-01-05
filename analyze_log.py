#!/usr/bin/env python3

import analyze_logdb

def popular_articles():
    print "1) What are the most popular three articles of all time?\n"
    rows = analyze_logdb.articles()
    for row in rows:
        print ("\t" + u'\u2022' + "%s -- %d views" % (row[0], row[1]))

def popular_authors():
    print "2) Who are the most popular article authors of all time?\n"
    rows = analyze_logdb.authors()
    for row in rows:
        print ("\t" + u'\u2022' + "%s -- %d views" % (row[0], row[1]))

def error_days():
    print "3) On which days did more than 1% of requests lead to errors?\n"
    rows = analyze_logdb.errors()
    for row in rows:
        print ("\t" + u'\u2022' + "%s -- %s errors" % (row[0], row[1]))

if __name__ == '__main__':
    print ("\n")
    print ("****News Logs Analyzer Tool****")
    print ("\n")
    popular_articles()
    print ("\n")
    popular_authors()
    print ("\n")
    error_days()
    print ("\n")
