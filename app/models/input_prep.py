"""
Read and transform data.
"""
import csv
from datetime import datetime
from app.models.validator import Validator


def read_csv(path: str) -> []:
    """
    read the input csv
    """

    output = []

    with open(path, newline='', encoding='utf8') as csvfile:
        input_data = csv.reader(csvfile, delimiter=",")
        next(input_data)  # skips header row

        for row in input_data:
            output.append(row)  # transform data into list

    return output


def validate_data(raw_data):
    """
    Validates that raw input data are in the correct format. If error here, check the delimiter.
    :type raw_data: list
    :rtype list
    """

    for row in raw_data:
        link = Validator(row[1])
        if not link.is_link():
            raise TypeError(row[1] + ' is not a link')

        date = Validator(row[4])
        if not date.is_date():
            raise TypeError(row[4] + ' is not a date')

    return raw_data


def articles(input_data):
    """
    create a dictionary from list of articles.
    :type input_data: list
    :rtype list of dictionaries. each dictionary represents one article.
    """

    articles_details = []

    for row in input_data:
        article_details = {
            'title': row[0],
            'link': row[1],
            'source': row[2],
            'summary': row[3],
            'date': datetime.strptime(row[4][3:], '%m.%Y').strftime("%Y-%m")
        }
        articles_details.append(article_details)

    return articles_details


def pages(input_articles):
    """
    create a dictionary with months and years as key with all corresponding articles.
    :type articles: list of dictionary of articles
    :rtype dictionary (page) of list of dictionaries (articles)
    """

    pages_per_months = {}
    for article in input_articles:
        date = article['date']
        if date not in pages_per_months:
            pages_per_months[date] = [article]
        else:
            pages_per_months[date].append(article)

    return pages_per_months


def combine_world_czech_articles(world, czech):
    """
    combine the world articles and czech articles to create one dictionary.
    :type world: dict
    :type czech: dict
    :rtype {page name {world or czech dict [list of articles]}}
    """
    combined_articles = {}

    for page_world in world:
        combined_articles[page_world] = {
            'world': world[page_world],
            'czech': [],
        }

    for page_czech in czech:
        if page_czech not in combined_articles:
            combined_articles[page_czech] = {
                'world': [],
                'czech': [],
            }
        combined_articles[page_czech]['czech'] = czech[page_czech]

    return combined_articles
