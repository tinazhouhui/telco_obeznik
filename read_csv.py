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
        month_year = []
        output = []
        next(csvfile) #skips header row
        for row in input_data:
            body_dict = {
                'Title': row[0],
                'Link': row[1],
                'Source': row[2],
                'Summary': row[3],
                'Date': datetime.strptime(row[4][3:], '%m.%Y').strftime("%B %Y")
            }
            output.append(body_dict)

            print(type(body_dict['Date'])) #this is a string
            #create a list of all months and years available in dictionary
            if body_dict['Date'] not in month_year:
                month_year.append(body_dict['Date'])

        return output, month_year

print(read_csv_create_dict('./inputs/data_dec19.csv'))
