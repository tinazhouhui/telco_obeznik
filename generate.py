"""
Generator of all functions.
"""
# import pprint
from app.models.input_prep import (
    validate_data,
    read_csv,
    articles,
    pages,
    combine_world_czech_articles,
)
from app.router import router

PIPELINE = [read_csv, validate_data, articles, pages]
OUTPUT_CZECH = './inputs/data_dec19.csv'
OUTPUT_WORLD = './inputs/data_world.csv'

for function in PIPELINE:
    OUTPUT_CZECH = function(OUTPUT_CZECH)
    OUTPUT_WORLD = function(OUTPUT_WORLD)

OUTPUT = combine_world_czech_articles(OUTPUT_WORLD, OUTPUT_CZECH)
# printer = pprint.PrettyPrinter(indent=4)
# printer.pprint(combine_world_czech_articles(OUTPUT_WORLD, OUTPUT_CZECH))


def save_files(all_pages: dict):
    """
    generate and save files in correct directory.
    """
    for file in all_pages:
        generated_file = open(r".\www\{}".format(file), "w+")
        generated_file.write(all_pages[file])
        generated_file.close()


PAGES = router(OUTPUT)
save_files(PAGES)
