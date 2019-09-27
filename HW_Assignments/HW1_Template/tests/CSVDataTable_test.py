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

    print('Loaded table: \n', csv_tbl)

def test_match():
    row = {'cool': 'yes', 'db': 'no'}
    t = {'cool', 'yes'}
    result = CSVDataTable.matches_template(row, t)
    print(result)


def t_find_by_template():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }

    key_cols = ['playerID', 'teamID', 'yearID', 'stint']
    fields = ['playerID', 'teamID', 'yearID', 'AB', 'H', 'HR', 'RBI']
    tmp = {'teamID': 'BOS', 'yearID': '1960'}

    csv_tbl = CSVDataTable("batting", connect_info, key_columns=key_cols)
    res = csv_tbl.find_by_template(template=tmp, field_list=fields)
    # json.dump basically means saving files in json format.
    print('Query result = \n', json.dumps(res, indent=2))



def t_find_by_primary_key_and_template():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people",connect_info,key_columns=['playerID'])
    r = csv_tbl.find_by_primary_key(['willite01'], field_list=['playerID','nameLast','throws','bats','birthCountry'])
    print("Find by key returned = " + str(r))

    t = {"playerID":"willite01"}
    rr = csv_tbl.find_by_template(t, field_list=['playerID','nameLast','throws','bats','birthCountry'])
    print("Find by template returned = " + str(rr))

def t_insert():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }
    key_cols = ['playerID', 'teamID', 'yearID', 'stint']
    csv_tbl = CSVDataTable('batting', connect_info, key_columns=key_cols)
    new_row = {
        'playerID': 'willite01', 'teamID': 'BOS', 'yearID': '1960', 'stint': '2', 'H': '21', 'AB': '23'
    }
    return csv_tbl.insert(new_row)

# def t_delete_by_key():
#     connect_info = {
#         "directory": data_dir,
#         "file_name": "Batting.csv"
#     }
#
#     key_cols = ['playerID']
#     csv_tbl = CSVDataTable('batting', connect_info, key_columns=key_cols)
#     result = csv_tbl.delete_by_key(['willite01'])
#     print("The number of rows to delete by searching keys: {}".format(result))

def t_delete_by_key2():
    connect_info = {
        "directory": data_dir,
        "file_name": "shire.csv"
    }

    key_cols = ['last_name']
    csv_tbl = CSVDataTable('shire', connect_info, key_columns=key_cols)
    result = csv_tbl.delete_by_key(['Logan'])
    print("The number of rows to delete by searching keys: {}".format(result))
    print("The table now looks like: ", csv_tbl)

# def t_delete_by_template():
#     connect_info = {
#         "directory": data_dir,
#         "file_name": "Batting.csv"
#     }
#
#     tmp = {'playerID': 'willite01'}
#     csv_tbl = CSVDataTable('batting', connect_info, None)
#     result = csv_tbl.delete_by_template(tmp)
#     print("The number of rows to delete by searching template: {}".format(result))

def t_insert2():
    connect_info = {
        "directory": data_dir,
        "file_name": "shire.csv"
    }
    key_cols = ['last_name','first_name','email']
    csv_tbl = CSVDataTable('shire', connect_info, key_columns=key_cols)
    new_row = {
        'last_name': 'Logan', 'first_name': 'Vildred', 'email': 'lv@epic.edu'
    }
    csv_tbl.insert(new_row)

    print("The table now looks like: \n", csv_tbl)




def t_delete_by_template2():
    connect_info = {
        "directory": data_dir,
        "file_name": "shire.csv"
    }

    tmp = {'last_name': 'Logan'}
    csv_tbl = CSVDataTable('shire', connect_info, None)
    result = csv_tbl.delete_by_template(tmp)
    print("The number of rows to delete by searching template: {}".format(result))
    print("The table now looks like: \n", csv_tbl)


def t_duplicates():
    connect_info = {
        "directory": data_dir,
        "file_name": "Batting.csv"
    }

    key_cols = ['playerID', 'teamID', 'yearID', 'stint']
    csv_tbl = CSVDataTable('batting', connect_info, key_columns=key_cols)
    new_row = {
        'playerID': 'willite01', 'teamID': 'BOS', 'yearID': '1960', 'stint': '1', 'H': '21', 'AB': '22'
    }
    res = csv_tbl.insert(new_row)

    print(result)


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
    test = CSVDataTable.matches_template(r, tmp)
    print("Matches = ", test)

def t_update_by_key():
    connect_info = {
        "directory": data_dir,
        "file_name": "shire.csv"
    }
    key_cols = ['last_name']
    new_val = {'last_name': 'Cheros'}
    csv_tbl = CSVDataTable('shire', connect_info,key_cols)
    result = csv_tbl.update_by_key(['Baggins'], new_val)
    print("The number of rows updated: {}".format(result))
    print("This is what the table looks like now: ", csv_tbl)


def t_update_by_template():
    connect_info = {
        "directory": data_dir,
        "file_name": "shire.csv"
    }
    tmp = {'last_name' : 'Baggins'}
    new_val = 'Cheros'
    csv_tbl = CSVDataTable('shire', connect_info, key_columns=['last_name'])
    result = csv_tbl.update_by_template(tmp,new_val)
    print("The number of rows updated: {}".format(result))
    print("This is what the table looks like now: ", csv_tbl)

# t_load()
# t_find_by_primary_key_and_template()
# t_find_by_template()
# t_matches_template()


# t_delete_by_key2()
# t_insert2()
# t_delete_by_template2()

# t_update_by_key()
# t_update_by_template()

# t_duplicates()
# t_delete_by_key()
# t_insert()
# t_delete_by_key()
# t_delete_by_template()