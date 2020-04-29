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
        format_str = '%d.%m.%Y'
        for row in input_data:
            body_dict = {
                'Title': row[0],
                'Link': row[1],
                'Source': row[2],
                'Summary': row[3],
                'Date': datetime.strptime(row[4], format_str)
            }
            output.append(body_dict)
        return output

print(read_csv_create_dict('./inputs/data_dec19.csv'))
