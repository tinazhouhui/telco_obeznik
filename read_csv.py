"""
Read and transform data.
"""
import csv
from datetime import datetime

def read_csv_create_dict(path):
    """
    read the input csv and create a dictionary
    :type path: path to the csvfile
    :rtype dict
    """
    with open(path, newline='') as csvfile:
        input_data = csv.reader(csvfile, delimiter=";")
        output = []
        next(csvfile) #skips header row
        for row in input_data:
            body_dict = {
                'title': row[0],
                'link': row[1],
                'source': row[2],
                'summary': row[3],
                'date': datetime.strptime(row[4][3:], '%m.%Y').strftime("%B %Y")
            }
            output.append(body_dict)

        return output

def pages(dict_articles):
    """
    create a unique list of months and years. This will be the titles of pages.
    :type dict_articles: dictionary of articles defined by read_csv_create_dict function
    :rtype list of 'Month YEAR'
    """
    dict_months = {}
    for article in dict_articles:
        date = article['date']
        if date not in dict_months:
            dict_months[date] = [article]
        else:
            dict_months[date].append(article)


    return dict_months

DICT_INPUT = read_csv_create_dict('./inputs/data_dec19.csv')
print(pages(DICT_INPUT))
