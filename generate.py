"""
Generator of all functions.
"""

import pprint
from app.input_prep import validate_data, read_csv, articles, pages
from app.article_list_render import ArticleListRender

# CSV_FILE = read_csv('./inputs/data_dec19.csv')
# VALIDATED_DATA = validate_data(CSV_FILE)
# ARTICLES = articles(VALIDATED_DATA)
# print(pages(ARTICLES))

PIPELINE = [read_csv, validate_data, articles, pages]
OUTPUT_CZECH = './inputs/data_dec19.csv'
OUTPUT_WORLD = './inputs/data_world.csv'

for function in PIPELINE:
    OUTPUT_CZECH = function(OUTPUT_CZECH)
    OUTPUT_WORLD = function(OUTPUT_WORLD)

OUTPUT = {}

for page_world in OUTPUT_WORLD:
    OUTPUT[page_world] = {
        'world': OUTPUT_WORLD[page_world],
        'czech': [],
    }

for page_czech in OUTPUT_CZECH:
    if page_czech not in OUTPUT:
        OUTPUT[page_czech] = {
            'world': [],
            'czech': [],
        }

    OUTPUT[page_czech]['czech'] = OUTPUT_CZECH[page_czech]

# printer = pprint.PrettyPrinter(indent=4)
# printer.pprint(OUTPUT)

# render pages
# create a sablona - test it
# output is dictionary where key is name of the file and variable is what should go to write.


def create_pages(article_groups):
    """
    Create article pages with correct html formatting.
    """

    for page_name in article_groups:
        articles_in_group = article_groups[page_name]
        filename = page_name.lower().replace(" 20", "") + ".html"
        generated_file = open(r".\www\{}".format(filename), "w+")
        article_list = ArticleListRender(articles_in_group)
        generated_file.write(article_list.to_html())
        generated_file.close()

create_pages(OUTPUT)
