#!/usr/bin/env python3

from reporter_db import article_views, author_views, error_stat


def print_views(views):
    for view in views:
        print("{} - {} views".format(view[0], view[1]))


def print_error_stat(error_stats):
    for date, rate in error_stats:
        print("{} -- {:.2%} errors".format(date.strftime("%b %d, %Y"), rate))


if __name__ == "__main__":
    print("1. What are the most popular three articles of all time?")
    print_views(article_views())
    print("")
    print("2. Who are the most popular article authors of all time?")
    print_views(author_views())
    print("")
    print("3. On which days did more than 1% of requests lead to errors?")
    print_error_stat(error_stat(0.01))
