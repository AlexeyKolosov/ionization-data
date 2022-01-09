import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from .BaseDF import BaseDF


class BoltekDF(BaseDF):
    
    def __init__(self, file_path, date, lim_field):
        with open(file_path, "r") as file:
            data = {
                'date_time': [],
                'value': []
            }
            content = file.readlines()
            for line in content:
                raw_sample = line.split(",")
                data['date_time'].append(datetime.strptime(raw_sample[0], "%H:%M:%S").replace(day=date[0], month=date[1], year=date[2]))
                field = float(raw_sample[1])*1000
                if abs(field) > abs(lim_field): field = lim_field
                data['value'].append(field) # V/m
            super().__init__(data)

    def show_plot(self):
        self.plot(x='date_time',y='value', color="black", grid=True)
        plt.show()
