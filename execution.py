'''Python program which reads multiple csv files and merges into single output file
Python version: 3.10
Author: Jeevitha Chandrappa'''

import csv
import os
import sys

#column which identifies each row uniquely
unique_identifier = 'ID'

rows_dict = {}

#function which takes input files and path for the output file as params
def merge_csv(file_names, output_path):
    for file in file_names:
        file = os.path.join(output_path,file)
        #check for similar file patters, could use regex as well
        if file.endswith(".csv"):
            with open(file, "r") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    id = row[unique_identifier]
                    #reading each row from csv files as dict
                    if id not in rows_dict:
                        rows_dict[id] = {}
                    for header, value in row.items():
                        if header != unique_identifier:
                            rows_dict[id][header] = value

    #write to output from the rows_dict
    with open(output_path + "/output_file.csv", "w", newline="") as f:
        # getting the unique headers list
        headers = [unique_identifier]
        for id in rows_dict:
            row = rows_dict[id]
            for header in row.keys():
                if header not in headers:
                    headers.append(header)

        csv_writer = csv.DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        #writing back to the csv from dict
        for id in rows_dict:
            row = rows_dict[id]
            row[unique_identifier] = id
            csv_writer.writerow(row)

# if __name__ == '__main__':

    # method1: passing filenames as system arguments
    # file_names = sys.argv[1:]
    # if not file_names:
    #     print("Please provide at least one file name as a command line argument")
    #     sys.exit(1)
    # for file_name in file_names:
    #     if not os.path.isfile(file_name):
    #         print(f"{file_name} is not a file")
    #         sys.exit(1)

    # method2: passing the filenames as a list
    # file_names = os.listdir(".")
    # output_path = os.getcwd()
    # merge_csv(file_names, output_path)
