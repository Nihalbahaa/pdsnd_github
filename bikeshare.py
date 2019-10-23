
import pandas as pd
import numpy as np
import datetime 
import statistics

def excel(city):
    while True:
        
        if city=='washington':
            gg=pd.read_csv('./washington.csv')
            break
        elif city=='chicago':
            gg=pd.read_csv('./chicago.csv')
            break
        elif city=='new_york' :
            gg=pd.read_csv('./new_york_city.csv') 
            break
        else:
            print ('sorry please enter the city name again')    
    return (gg)



def get_filters(gg):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    f=input("do you want filter by month, day ,both or none?")
    if f=='both':
        while True:
            try:
                m=int(input("which month do you want filter with, please inter integer value "))
                break
            except:
                print("\n that\'s not a valid number! please try again \n ")
        while True:        
            if m<=6:

                break
            else:
                
                m=int(input("please enter a correct month number from 1 to 6"))
                
        gg['month'] = pd.DatetimeIndex(gg['Start Time']).month
        records = gg.loc[gg['month'] == m]
        while True:
                                                     
            try:
                                    
                d=int(input("please inter the day that you want filter \n "))
                break
            except:
                                   
                print("\n that\'s not a valid number! please try again number should be from 1 to 6 ")
        while True:
            
            if d<=6:
                
                
                break
            else:
                
                d=int(input("please inter the day that you want filter notice it is from 1 to 6  "))
        records['day'] = pd.DatetimeIndex(records['Start Time']).day
        data = records.loc[records['day'] == d]    
    elif f=='month':
        while True:
            try:
                m=int(input("which month do you want filter with, please inter integer value "))
                break
            except:
                print("\n that\'s not a valid number! please try again \n ")
        while True:
            if m<=6:
                break
            else:
                m=int(input("which month do you want filter with, please inter integer value from 1 to 6 "))
            
        gg['month'] = pd.DatetimeIndex(gg['Start Time']).month
        data = gg.loc[gg['month'] == m]
    elif f=='day':
        
        while True:
            try:
                d=int(input("please inter the day that you want filter \n "))
                break
            except:
                print("\n that\'s not a valid number! please try again \n ")
        while True:
            if d<=6:
                break
            else:
                d=int(input("please inter the day that you want filternotice it is number from 1 to 6 "))
                
        gg['day'] = pd.DatetimeIndex(gg['Start Time']).day
        data = gg.loc[gg['day'] == d]
    else :
        data=gg
        
    return (data)
  
def stat(data):
    #calculate some important statisticals
    print("here is some usefull statistical about bikeshare system ")    
    print(data.describe())


def stations_trip(data):
    #find the most commen start station
    #find the most commen End station
    #find the  the most commen trip 
    print("the most commen start station is :",statistics.mode(data['Start Station']),"\n  the most commen End station is :",statistics.mode(data['End Station'])," \n  the most commen trip is the one between ", data.groupby(['Start Station','End Station']).size().idxmax())
     
        
def trip_duration(data):
    
    #calculate total travel time
    #calculate average travel time
    print("total travel time is:",data['Trip Duration'].sum(),"\n average travel time is:",statistics.mean(data['Trip Duration']))
     

def User_info(data):
    #count each user type
    #count of each gender
    print("the counts of each user type: ",data.groupby(['User Type'])['Unnamed: 0'].count(),"\n  the counts of each gender: ",data.groupby(['Gender'])['Unnamed: 0'].count(),"\n  the most common year of birth",statistics.mode(data['Birth Year']))
   
def main():
    # the main program under a wile loop to repeat using it many times
    while True:
        city=input("which city you want get information about (washington, chicago or new_york) ").lower()
        gg=excel(city)
        data=get_filters(gg)
        a=input("do you want see five lines of raw data about some usiful statistical Enter yes or no.\n").lower()
        if a=='yes': 
            stat(data)
            b=input("\n do you want seeanother five lines of raw data about stations and trip Enter yes or no.\n").lower()
            if b=='yes': 
                stations_trip(data)
                c=input("\ndo you want see another five lines of raw data about trip duration Enter yes or no.\n").lower()
                if c=='yes': 
                    trip_duration(data)
                    if city=='chicago':
                           d=input("do you want see another five lines of raw data about user info. Enter yes or no.\n").lower()
                           if d=='yes':
                               User_info(data)
                    if city=='new_york':
                           d=input("do you want see another five lines of raw data about user info. Enter yes or no.\n").lower()
                           if d=='yes':
                               User_info(data)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()