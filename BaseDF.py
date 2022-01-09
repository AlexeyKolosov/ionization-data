from abc import ABC, abstractmethod
from openpyxl import load_workbook
import pandas
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from datetime import datetime
pandas.options.mode.chained_assignment = None
get_ipython().run_line_magic('matplotlib', 'notebook')


class BaseDF(ABC, pandas.DataFrame):

    def print_table(self):
        with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self)
            
    def truncate_df(self, start_date_time, end_date_time):
        return self[(self['date_time'] >= start_date_time) & (self['date_time'] <= end_date_time)]

    ''' date_time_ckpts includes last date_time but NOT first'''
    def average_between_ckpts(self, column, date_time_ckpts):
        averaged_df = pandas.DataFrame({})
        start = self['date_time'][0]
        for ckpt in date_time_ckpts:
            truncated = truncate_df(self, start, ckpt)
            mean_value = truncated[column].mean()
            truncated[column] = [mean_value]*len(truncated[column])
            averaged_df = pandas.concat([averaged_df, truncated])
            start = ckpt
        return averaged_df
    
    @staticmethod
    def unite_dfs(dfs):
        return pandas.concat(dfs)
    
    ''' plot  name: (xs, ys, y_interval)'''
    @staticmethod
    def align_plots(plots, suptitle, major_minutes_interval=20, minor_minutes_interval=5)
        fig = plt.figure(figsize=(10, 4*len(plots)), dpi=80) # plot size
        fig.suptitle(suptitle, fontsize=16)
        gs = gridspec.GridSpec(len(plots), 1)
        index = 0
        sharex = None
        for plot_title, data in plots.items():
            ax = plt.subplot(gs[index], sharex = sharex)
            ax.plot(data[0], data[1], color='black')
            ax.set_title(plot_title, loc='right', fontsize=8)
            ax.yaxis.set_major_locator(ticker.MultipleLocator(data[2]))
            ax.grid(which='major', alpha=0.8)
            ax.grid(which='minor', alpha=0.8) 
            if sharex is None:
                sharex = ax
            index+=1
        plt.subplots_adjust(hspace=0.2)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=major_minutes_interval))
        plt.gca().xaxis.set_minor_locator(mdates.MinuteLocator(interval=minor_minutes_interval))
        plt.gcf().autofmt_xdate(rotation=0)
        plt.show()
    
     
    @abstractmethod
    def show_plot(self):
        pass
