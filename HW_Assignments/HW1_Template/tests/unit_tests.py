# I write and test methods one at a time.
# This file contains unit tests of individual methods.

from src.CSVDataTable import CSVDataTable
import logging
import os
import json


# The logging level to use should be an environment variable, not hard coded.
logging.basicConfig(level=logging.DEBUG)

# Also, the 'name' of the logger to use should be an environment variable.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# This should also be an environment variable.
# Also not the using '/' is OS dependent, and windows might need `\\`
data_dir = os.path.abspath("../Data/Baseball")


def t_load():

    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)

    print("Created table = " + str(csv_tbl))



def test_match():

    row = {'cool': 'yes','db':'no'}
    t = {'cool','yes'}
    result = CSVDataTable.matches_template(row,t)
    print(result)


def t_find_by_template():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }

    key_cols = ['playerID','teamID','yearID','stint']
    fields = ['playerID','teamID','yearID','AB','H','HR','RBI']
    tmp = {'teamID':'BOS','yearID':'1960'}

    csv_tbl = CSVDataTable("batting", connect_info, key_columns=key_cols)
    res = csv_tbl.find_by_template(template=tmp, field_list=fields)
    # json.dump basically means saving files in json format.
    print('Query result = \n', json.dumps(res, indent=2))

# def t_find_by_primary_key_and_template(tests/unit_tests.py:72):
#     connect_info = {
#         "directory": data_dir,
#         "file_name": "Batting.csv"
#     }
#
#     csv_tbl = CSVDataTable("people", connect_info, key_columns=['playerID'])
#

def t_duplicates():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }

    key_cols = ['playerID','teamID','yearID','stint']
    csv_tbl = CSVDataTable('batting',connect_info,key_columns=key_cols)
    new_row = {
        'playerID': 'willite01', 'teamID': 'BOS', 'yearID':'1960', 'stint':'1', 'H':'21','AB':'22'
    }
    res =


def t_matches_template():
    r = {
    "playerID": "worthal01",
    "teamID": "BOS",
    "yearID": "1960",
    "AB": "1",
    "H": "0",
    "HR": "0",
    "RBI": "0"
  }
    tmp = {"playerID": "willite01"}
    test = CSVDataTable.matches_template(r,tmp)
    print("Matches = ", test)

# t_load()

# t_find_by_template()
# t_matches_template()
