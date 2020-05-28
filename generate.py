"""
Generator of all functions.
"""

# import pprint
from app.controllers.index import IndexController
from app.models.input_prep import validate_data, read_csv, articles, pages, combine_world_czech_articles
from app.controllers.articles import ArticlesController
from app.models.date_parsing import page_title, file_name


PIPELINE = [read_csv, validate_data, articles, pages]
OUTPUT_CZECH = './inputs/data_dec19.csv'
OUTPUT_WORLD = './inputs/data_world.csv'

for function in PIPELINE:
    OUTPUT_CZECH = function(OUTPUT_CZECH)
    OUTPUT_WORLD = function(OUTPUT_WORLD)

OUTPUT = combine_world_czech_articles(OUTPUT_WORLD, OUTPUT_CZECH)
# printer = pprint.PrettyPrinter(indent=4)
# printer.pprint(combine_world_czech_articles(OUTPUT_WORLD, OUTPUT_CZECH))


def create_pages(article_groups: dict) -> dict:
    """
    Create article pages with correct html formatting.
    """
    print(sorted(article_groups, reverse=True))
    index_page = IndexController('Vítejte na Telco oběžníku!')

    pages_to_files = {
        'index.html': index_page.to_html(),
        #'archive.html': archive_page.to_html(),
    }

    for year_month in article_groups:
        articles_in_group = article_groups[year_month]
        article_list = ArticlesController(page_title(year_month), articles_in_group)
        pages_to_files[file_name(year_month)] = article_list.to_html()

    return pages_to_files

def save_files(pages: dict):
    for file in pages:
        generated_file = open(r".\www\{}".format(file), "w+")
        generated_file.write(pages[file])
        generated_file.close()


PAGES = create_pages(OUTPUT)
save_files(PAGES)
