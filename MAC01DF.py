import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from .BaseDF import BaseDF


class MAC01DF(BaseDF):
    @staticmethod
    def __relative_time_to_absolute(start_timestamp, relative_time_str):
        rel_lst = relative_time_str.split(".")[0].split(":")
        seconds = int(rel_lst[0]) * 3600 + int(rel_lst[1]) * 60 + int(rel_lst[2])
        return datetime.fromtimestamp(start_timestamp + seconds)

    def show_plot(self):
        self.plot(x='date_time',y='value', color="black", grid=True)
        plt.show()

    def __init__(self, file_path, remove_zeros):
        with open(file_path, "r") as file:
            content = file.readlines()
            start_date_time = content[2].strip() + " " + content[4].strip()
            start_timestamp = datetime.strptime(start_date_time, "%d.%m.%Y %H:%M:%S").timestamp()
            data = {
                'date_time': [],
                'value': [],
                'polarity': []
            }
            for row_index in range(7, len(content)-1):
                sample = content[row_index].split("   ")
                value = int(sample[0])
                if remove_zeros and value >= 0: # todo >= for negative polarity only
                    continue
                data['value'].append(abs(value))
                data['date_time'].append(MAC01DF.__relative_time_to_absolute(start_timestamp, sample[1]))
                data['polarity'].append(sample[2].strip())
            super().__init__(data)
