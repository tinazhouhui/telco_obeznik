"""
Read and transform data.
"""
import csv
from datetime import datetime

def read_csv(path):
    """
    read the input csv
    :type path: path to the csvfile
    :rtype csv.reader object
    """
    output = []

    with open(path, newline='') as csvfile:
        input_data = csv.reader(csvfile, delimiter=";")
        next(input_data) #skips header row

        for row in input_data:
            output.append(row) #transform data into list

    return output

def articles(input_data):
    """
    create a dictionary from list of articles.
    :type input_data: list
    :rtype list
    """
    articles_details = []

    for row in input_data:
        article_details = {
            'title': row[0],
            'link': row[1],
            'source': row[2],
            'summary': row[3],
            'date': datetime.strptime(row[4][3:], '%m.%Y').strftime("%B %Y")
        }
        articles_details.append(article_details)

    return articles_details

def pages(input_articles):
    """
    create a dictionary with months and years as key with all corresponding articles.
    :type articles: dictionary of articles defined by read_csv_create_dict function
    :rtype dictionary
    """
    pages_per_months = {}
    for article in input_articles:
        date = input_articles['date']
        if date not in pages_per_months:
            pages_per_months[date] = [article]
        else:
            pages_per_months[date].append(article)

    return pages_per_months
