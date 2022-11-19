import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please input city (chicago, new york city, washington): ')
    while city not in CITY_DATA:
        city = input('Incorrect city name, please try again:')
        city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please input month ' + str(MONTH_DATA) + ': ')
    while month not in MONTH_DATA:
        month = input('Incorrect month, please try again:')
        month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please input day ' + str(DAY_DATA) + ': ')
    while day not in DAY_DATA:
        day = input('Incorrect day name, please try again:')
        day = day.lower()

    print('-'*40)
    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        month = MONTH_DATA.index(month) + 1

        # Filtering by month to create new dataframe
        df = df[df['Month'] == month]
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month: ', MONTH_DATA[df['Month'].mode()[0]-1])

    # TO DO: display the most common day of week
    print('Most common day: ', df['Day of Week'].mode()[0])

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print('Most common start hour:', df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip:\n', df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: ', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('Counts of gender: ', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Display earliest year of birth:', df['Birth Year'].min())
    print('Most recent year of birth:', df['Birth Year'].max())
    print('Most common year of birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
