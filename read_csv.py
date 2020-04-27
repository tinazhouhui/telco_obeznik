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
                'Title': row[0],
                'Link': row[1],
                'Source': row[2],
                'Summary': row[3],
                'Date': row[4]
            }
            output.append(body_dict)
        return output

def convert_date_to_month(dict_input):
    """
    Convert date to month
    """
    for i in range(len(dict_input)):
        format_str = '%d.%m.%Y'
        date = datetime.strptime(dict_input[i]['Date'], format_str)
        dict_input[i]['Date'] = date
        print(date)
    return dict_input

input_data = read_csv_create_dict('./inputs/data_dec19.csv')
print(convert_date_to_month(input_data))
