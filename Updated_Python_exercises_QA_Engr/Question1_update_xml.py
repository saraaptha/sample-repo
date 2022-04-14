import os
import xml.etree.ElementTree as ET
import datetime
from datetime import timedelta

dir = "C:/Users/saraa/Updated_Python_exercises_QA_Engr/"
os.chdir(dir)
os.getcwd()
os.listdir()

def update_values(x, y):
    x = str(x).strip()
    y = str(y).strip()
    if (x.isdigit() and y.isdigit() == True):
        mytree = ET.parse('test_payload1.xml')
        myroot = mytree.getroot()
        for i in myroot.iter('DEPART'):
            new_depart = datetime.datetime.now() + timedelta(days=int(x))
            updated_depart = new_depart.date()
            i.text = str(updated_depart)
            print("new depart val:", i.text)
        for j in myroot.iter('RETURN'):
            new_return = datetime.datetime.now() + timedelta(days=int(y))
            updated_return = new_return.date()
            j.text = str(updated_return)
            print("new return val:", j.text)
        mytree.write(dir + "\output1.xml")
    else:
        print("Please pass valid numbers as arguments")
update_values(5,10)

#sample output
# new depart val: 2022-04-19
# new return val: 2022-04-24