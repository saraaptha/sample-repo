import os
import json

dir = "C:/Users/saraa/Updated_Python_exercises_QA_Engr/"
os.chdir(dir)
os.getcwd()
os.listdir()

updated_dict = dict()
file_path = (os.path.join(dir, "test_payload.json"))
with open(file_path, 'r') as data_file:
    json_data = (json.load(data_file))
    new_dict = json_data.copy()


def remove_element(new_dict,element):
    if element in new_dict:
        del new_dict[element]
    for key, value in new_dict.items():
        if isinstance(value, dict):
            remove_specific_element(value,element)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    remove_element(item,element)
    return (new_dict)


import os
import datetime
from datetime import timedelta, date
import json

dir = "C:/Users/saraa/Updated_Python_exercises_QA_Engr/"
os.chdir(dir)
os.getcwd()
os.listdir()

updated_dict = dict()
file_path = (os.path.join(dir, "test_payload.json"))
with open(file_path, 'r') as data_file:
    json_data = (json.load(data_file))
    new_dict = json_data.copy()


def remove_element(new_dict, element):
    if element in new_dict:
        del new_dict[element]
    for key, value in new_dict.items():
        if isinstance(value, dict):
            remove_specific_element(value, element)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    remove_element(item, element)
    return (new_dict)


# To delete specific keys(elements) please change element passed in the method call
updated_dict = remove_element(new_dict, 'appdate')
print("*****Updated dictionary after deletion is:\n", updated_dict)

# updated_dict= remove_element(new_dict,'outParams')
# print("*****Updated dictionary after deletion is:\n",updated_dict)

#write to json file
for key, values in updated_dict.items():
    json_str = json.dumps(updated_dict, indent=4) + '\n'

with open("modified_payload.json", "w") as outfile:
    outfile.write(json_str)

# sample Output
# *****Updated dictionary after deletion is:
#  {'spreadsheetName': 'ABC.xls', 'inParams': {'planselect_1': 'test11', 'retdt': '2019-04-10', 'statecode': 'CA', 'deptdt': '2019-04-09'}, 'outParams': ['dateeff', 'dateterm', 'coverageresult', 'calcdescr', 'errorchk', 'planresult', 'covgsummary', 'prem'], 'sessionId': None}
# {'planselect_1': 'test11', 'retdt': '2019-04-10', 'statecode': 'CA', 'deptdt': '2019-04-09'}

# *****Updated dictionary after deletion is:
#  {'spreadsheetName': 'ABC.xls', 'inParams': {'planselect_1': 'test11', 'retdt': '2019-04-10', 'statecode': 'CA', 'deptdt': '2019-04-09'}, 'sessionId': None}