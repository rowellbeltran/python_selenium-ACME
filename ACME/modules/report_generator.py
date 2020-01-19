import xml.etree.ElementTree as ET
from openpyxl import load_workbook
import os, glob, shutil
from datetime import datetime

user = os.environ['USERNAME']
dt_string = datetime.now().strftime("%m%d%Y%H%M")
destination = f'C:/Users/{user}/Selenium/ACME/Tests/acceptance/reports/Test Report_{dt_string}/'
source = f'C:/Users/{user}/Selenium/ACME/Tests/acceptance/reports/'

def move_report_files():
    if not os.path.exists(destination):
        os.makedirs(destination)   # only if it does not yet exist
    for f in os.listdir(source):
        if f.endswith(".xml"):
            shutil.copy(source + f, destination)
    os.chdir(destination)


def create_report():
    move_report_files()
    template = load_workbook(f'{source}Test_Results_template.xlsx')
    sheet = template['Results']

    #add header
    sheet.append(['Filename', 'Scenario', 'Steps', 'Status', 'Runtime', 'Failure Type', 'Failure Message'])

    #Read jUnit XMLs
    for file in glob.glob("*.xml"):
        tree = ET.parse(file)
        for test_case in tree.iterfind("testcase"):
            scenario = test_case.get("name")
            runtime = test_case.get("time")
            status = test_case.get("status").upper()
            fail_type = ""
            fail_message = ""

            # Get failure details
            if status != 'PASSED':
                for fail in test_case.iterfind("failure"):
                    fail_type = fail.get("type")
                    fail_message = fail.text

            #remove start and begin statements
            steps = ''
            cdata = test_case[0].text.replace('-', '').splitlines()
            for t in range(len(cdata)):
                if t in range(4, len(cdata[t])-5):
                    steps += f'{cdata[t]}\n'

            sheet.append([file, scenario, steps, status, runtime, fail_type, fail_message])

    template.save(f'{destination}Test Report.xlsx')


create_report()


