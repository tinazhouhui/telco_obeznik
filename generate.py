"""
Generator of all functions.
"""

# import pprint
from app.input_prep import validate_data, read_csv, articles, pages, combine_world_czech_articles
from app.articles_controller import ArticlesController
from app.index_controller import page_title, filename


PIPELINE = [read_csv, validate_data, articles, pages]
OUTPUT_CZECH = './inputs/data_dec19.csv'
OUTPUT_WORLD = './inputs/data_world.csv'

for function in PIPELINE:
    OUTPUT_CZECH = function(OUTPUT_CZECH)
    OUTPUT_WORLD = function(OUTPUT_WORLD)

OUTPUT = combine_world_czech_articles(OUTPUT_WORLD, OUTPUT_CZECH)
# printer = pprint.PrettyPrinter(indent=4)
# printer.pprint(combine_world_czech_articles(OUTPUT_WORLD, OUTPUT_CZECH))


def create_pages(article_groups: dict):
    """
    Create article pages with correct html formatting.
    """
    print(sorted(article_groups, reverse=True))
    for year_month in article_groups:
        articles_in_group = article_groups[year_month]
        generated_file = open(r".\www\{}".format(filename(year_month)), "w+")
        article_list = ArticlesController(articles_in_group, page_title(year_month))
        generated_file.write(article_list.to_html())
        generated_file.close()


create_pages(OUTPUT)
