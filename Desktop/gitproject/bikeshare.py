# This comment for Git project 
import time
import pandas as pd
import numpy as np


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\n Choose City: \n1- new york city 2- chicago  3- washington?\n").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Please Try again!")
        continue
      else:
        break

    # TO DO: get user input for month 

    while True:
      month = input("\n Choose Month: \n1- January 2- February 3- March 4- April 5- May 6- June or all \n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Please Try again!")
        continue
      else:
        break

    # TO DO: get user input for day of week

    while True:
      day = input("\n Choose Day: \n1- Sunday 2- Monday 3- Tuesday 4- Wednesday 5- Thursday 6- Friday 7- Saturday or all\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Please Try again!")
        continue
      else:
        break

    print('-'*40)
    return city, month, day
 # ------------------------------------------------LOAD DATA FUNCATION START -----------------------------------


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], infer_datetime_format=True)

    # extract month and day of week
    
    df['month'] = df['Start Time'].dt.month
    df['DayOfWeek'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month 
    if month != 'all':
   	 	
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month e
        df = df[df['month'] == month]

        # filter by day 
    if day != 'all':
        
        df = df[df['DayOfWeek'] == day.title()]

    return df

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == 'yes'):
       print(df.iloc[start_loc:start_loc + 5])
       start_loc += 5
       view_data = input("Do you wish to continue?: Enter yes or no \n").lower()
    
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    
    if common_month == 1:

        mon = 'January' 

    elif common_month == 2:

      mon = 'February' 

       
    elif common_month == 3:

        mon = 'March' 

    elif common_month == 4:

         mon = 'April' 

    elif common_month == 5:

        mon = 'May' 

    elif common_month == 6:

         mon = 'June' 

            
    print('Most Common Month \n', mon)


    # TO DO: display the most common day of week

    common_day = df['DayOfWeek'].mode()[0]
    print('Most Common day is \n', common_day)



    # TO DO: display the most common start hour

    
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour is \n', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # ------------------------------------------------STATIONS FUNCATION START -----------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most common start station

    start = df['Start Station'].value_counts().idxmax()
    print('The Common start station is \n', start)


    # TO DO: display most common end station

    end = df['End Station'].value_counts().idxmax()
    print('\nThe Common end station is \n', end)


    # TO DO: display most common combination of start station and end station trip

    combain = df.groupby(['Start Station', 'End Station']).count()
    print('\n The Common combination of start station and end station is \n', start, " & ", end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # ------------------------------------------------DURATION FUNCATION START -----------------------------------

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total = (sum(df['Trip Duration']))/86400
    print('The Total travel time is \n', total)


    # TO DO: display mean travel time

    mean = (df['Trip Duration'].mean()) / 60
    print('The Mean travel time is \n', mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # ------------------------------------------------USERS STATS FUNCATION START -----------------------------------
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    users = df['User Type'].value_counts()
    print('\n The User Type is \n', users)

    # TO DO: Display counts of gender
    if  city == 'new york city' or city== 'chicago':

      gender = df['Gender'].value_counts()
      print('\n The Gender Type is\n', gender)
    # TO DO: Display earliest, most recent, and most common year of birth

      earliest = df['Birth Year'].min()
      print('\nThe Earliest Year is \n', earliest)
     
      recent = df['Birth Year'].max()
      print('\nThe Recent Year is \n', recent)
    
      common = df['Birth Year'].value_counts().idxmax()
      print('\nThe Most Common Year is \n', common)
    else: 
        print('\n---------------------Opps---------------------------')
        print (' No Avalibale Data about gender And Birth Year !! \n')
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()