from datetime import *
import datetime
#from numpy import true_divide

class Date_:
    def __init__(self,date):
        self.date=date
    def find_month(self,month):
        if month=='January':
            return 1
        if month=='February':
            return 2
        if month=='March':
            return 3
        if month=='April':
            return 4
        if month=='May':
            return 5
        if month=='June':
            return 6
        if month=='July':
            return 7
        if month=='August':
            return 8
        if month=='September':
            return 9
        if month=='October':
            return 10
        if month=='November':
            return 11
        if month=='December':
            return 12
    def convert_date_in_numbers(self):
        month=self.date.split(' ',1)[0]
        self.month=self.find_month(month)
        temp=self.date.split(', ',1)
        self.day=int(temp[0].split(' ')[1])
        self.year=int(temp[1].split(' ')[0])
    def match_date(self):
        today = str(date.today())
        #print(today)
        datem = datetime.datetime.strptime(today, "%Y-%m-%d")
        #print(type(datem.day))
        if datem.day==self.day and datem.month==self.month and datem.year==self.year:
            return True
        else:
            return False 
        