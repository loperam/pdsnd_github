import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    response = 'tryagain'
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while response == 'tryagain':
        city = input("Would you like to see data for Chicago, New York or Washington? ")
        if ( (city.lower() == 'chicago') or (city.lower() == 'new york') or (city.lower() == 'washington')):
            print("{} it is!".format(city.title()))
            city=city.lower()
            response = 'Good'

    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    months=['january','february','march','april','may','june']
    response1= 'tryagain'
    while response1 == 'tryagain':
        date_filter = input('Would you like to filter by month, day, both or none? Type "none" for no time filter. ')
        date_filter = date_filter.lower()
        if date_filter == 'both':
            # TO DO: get user input for month (all, january, february, ... , june)
            month = input('\nWhich month? January, February, March, April, May, or June? ')
            month=month.lower()
            if (month in months):
                print('\nMonth selected: {}'.format(month.title()))
                response1= 'Good'
            else:
                print('\nNot a valid month selected')
                response1= 'tryagain'
                continue
            
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input ('\nWhich day? Monday, Tuesday, ... Sunday? ')
            day=day.lower()
            if (day in days):
                print('\nDay selected: {}'.format(day.title()))
                response1= 'Good'
            else:
                print('\nNot a valid day selected')
                response1= 'tryagain'
        
        elif date_filter == 'month':
            # TO DO: get user input for month
            month = input('\nWhich month? January, February, March, April, May, or June? ')
            month=month.lower()
            
            if (month in months):
                print('\nMonth selected: {}'.format(month.title()))
                day = 'all'
                response1= 'Good'
            else:
                print('\nNot a valid month selected')
                response1= 'tryagain'
        
        elif date_filter == 'day':
            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = input ('\nWhich day? Monday, Tuesday, ... Sunday? ')
            day=day.lower()
            if (day in days):
                print('\nDay selected: {}'.format(day.title()))
                month = 'all'
                response1= 'Good'
            else:
                print('\nNot a valid day selected')
                response1= 'tryagain'
        
        elif date_filter == 'none':
            # TO DO:
            month = 'all'
            day = 'all'
            print('\nNo date filters')
            response1= 'Good'
        else: 
            print('Please enter a valid option')
            response1= 'tryagain'
            
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day= day.title()
        df = df[df['day_of_week']==day]    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    pop_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[pop_month-1]
    print('\nMost Popular Month:', popular_month.title())

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Popular Day:', popular_day)

    # TO DO: display the most common start hour
    popular_starthour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_starthour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station: ', popular_startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('\nMost Popular End Station: ', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('\nMost Popular Start and End Station Combination is \nStart Station: \t{}  and \nEnd Station: \t{}'.
          format(popular_start_end_station[0], popular_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time=df['Trip Duration'].sum()
    print('\nTotal Travel Time: {} seconds'.format(travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('\nAverage Travel Time: {} seconds'.format(mean_travel_time))
    
    #Display longest trip
    longest_trip=df['Trip Duration'].max()
    print('\nLongest trip: {} seconds'.format(longest_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts=df['User Type'].value_counts()
    print('\nThe user types were: ')
    for i in range(len(user_counts)):
        print('{} {}(s)'.format(user_counts[i],user_counts.index[i]))

    # TO DO: Display counts of gender
    gender_counts = df.groupby('Gender')['Gender'].count()
    print('\nThe total gender count is ',gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    df['Birth Year'].dropna(inplace=True)
    #Earliest birth year
    earliest_year = df['Birth Year'].min()
    print('\nThe earliest birth year is: ',int(earliest_year))
    #Most recent birth year
    most_recent_byear = df['Birth Year'].max()
    print('\nThe most recent birth year is: ',int(most_recent_byear))
    #Most common birth year
    most_common_byear = df['Birth Year'].value_counts().idxmax()
    print('\nThe most common birth year is: ',int(most_common_byear))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_w(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts=df['User Type'].value_counts()
    print('\nThe user types were: ')
    for i in range(len(user_counts)):
        print('{} {}(s)'.format(user_counts[i],user_counts.index[i]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data from the bikeshare users."""
    
    iter = 0
    rows=len(df.index)
    print('\n Total number of trips in this selection: ',rows)
    print('\n Displaying individual trip data\n')
    while True:
        for row in range(5):
            print('\n--------------- Record: {} ---------------------'.format(iter+1))
            print(df.iloc[iter])
            iter+=1
            if iter==rows:
                print('\nThat\'s the end of the trip data')
                return
        more_data=input("\n Would you like to view more individual trip data? 'yes' or 'no' ").lower()
        if (more_data=='yes'):
            continue
        elif(more_data=='no'):
            break
        else:
            print('Not a valid option')
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city=='washington':
            user_stats_w(df)
        else:
            user_stats(df)

        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no. ')
        if restart.lower() != 'yes':
            print('\nThanks for using this code. Have a nice day :o) ')
            break


if __name__ == "__main__":
	main()
