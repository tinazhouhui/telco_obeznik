# read csv file
# replace value in template

from read_csv import read_csv, articles, pages

CSV_FILE = read_csv('./inputs/data_dec19.csv')
ARTICLES = articles(CSV_FILE)
print(pages(ARTICLES))
