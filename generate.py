"""
Generator of all functions.
"""
from app.input_prep import validate_data, read_csv, articles, pages

#CSV_FILE = read_csv('./inputs/data_dec19.csv')
#VALIDATED_DATA = validate_data(CSV_FILE)
#ARTICLES = articles(VALIDATED_DATA)
#print(pages(ARTICLES))

PIPELINE = [read_csv, validate_data, articles, pages]
OUTPUT = './inputs/data_dec19.csv'

for function in PIPELINE:
    OUTPUT = function(OUTPUT)

def create_pages(input):
    for page in input:
        filename = page.lower().replace(" 20", "")+".html"
        print(filename)
        generated_file = open(r"C:\Users\tzhouhui\Documents\Telko Oběžník\Pages\{}".format(filename),"w+")
        for article in input[page]:
            generated_file.write(article['title']+"<br>\n")
        generated_file.close()

create_pages(OUTPUT)
