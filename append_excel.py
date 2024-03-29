"""
Syncs with mettler_read application
to write output balance data to .csv
file
"""

import os
from datetime import datetime
import pandas as pd


class ToCSV:
    def __init__(self, _file):
        self.data_list = []
        self.header = ['Date/Time', 'Weight (g)']
        self.file_name = "{}.csv".format(_file)
        if self.file_name in os.listdir():
            raise FileExistsError('CSV file already exists - choose another name.')
        self.mkdir_chdir_date()

    def mkdir_chdir_date(self):
        date_today = "{}-{}-{}".format(
            datetime.now().year,
            datetime.now().month,
            datetime.now().day
        )
        if date_today not in os.listdir():
            os.mkdir(date_today)
        os.chdir("{}/{}".format(os.getcwd(), date_today))

    def write_csv(self, weight_value):
        data_val = [datetime.now(), weight_value]
        pd_header = pd.DataFrame(columns=[i for i in self.header])
        self.data_list.append(data_val)
        for data in self.data_list:
            pd_header.loc[len(pd_header)] = data
        
        pd_header.to_csv(self.file_name, sep=',', index=False)
