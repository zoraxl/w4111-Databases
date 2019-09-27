# I write and test methods one at a time.
# This file contains unit tests of Individual methods

from src.CSVDataTable import CSVDataTable
import logging
import os
import json

# The logging level to use should be an environment variable, not hard coded
logging.basicConfig(level=logging.DEBUG)

# Also, the 'name' of the logger to use should be environment variable
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# This should also be an environment variable
# Also not the using '/' is OS dependent, and windows might need '\\'

data_dir = os.path.abspath("../Data/Baseball")


def test_init():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)

    print('Loaded table: \n', csv_tbl)


def test_match_all():
    tmp = {'nameLast': 'Aardsma', 'birthCity': 'Denver'}

    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)
    field_list = ["nameFirst", "nameLast", "birthCity", "playerID"]
    result = csv_tbl.find_by_template(tmp, field_list=field_list)
    print(json.dumps(result, indent=2))

# def test_k():
#     connect_info = {
#         "directory": data_dir,
#         "file_name": "People.csv"
#     }
#     csv_tbl = CSVDataTable("People", connect_info,key_columns=['playerID'])
#     k = csv_tbl.


# test_init()
# test_match_all()
