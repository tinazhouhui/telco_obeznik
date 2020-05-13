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

#render pages
#create a sablona - test it
#output is dictionary where key is name of the file and variable is what should go to write.

def create_pages(input):
    for page in input:
        filename = page.lower().replace(" 20", "")+".html"
        print(filename)
        generated_file = open(r".\www\{}".format(filename),"w+")
        for article in input[page]:
            generated_file.write(article['title']+"<br>\n")
        generated_file.close()

create_pages(OUTPUT)
