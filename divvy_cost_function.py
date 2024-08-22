import pandas as pd

# read the cleaned data into a datafram
divvy = pd.read_csv('C:/Users/barry/~coding/R Programming/googleclass/divvytrips/divvy_clean.csv')

# define a fucntion to calculate cost of ride
def ride_value(a, b):
    if a['member_casual'][b] == "member" and a['rideable_type'][b] == "classic_bike":
        result = 0.18 * (a['total_time'][b] - 2700) / 60
    elif a['member_casual'][b] == "member" and a['rideable_type'][b] == "electric_bike":
        result = 0.18 * a['total_time'][b] / 60
    elif a['member_casual'][b] == "member" and a['rideable_type'][b] == "docked_bike":
        result = 0.29 * a['total_time'][b] / 60
    elif a['member_casual'][b] == "casual" and a['rideable_type'][b] == "classic_bike":
        result = 1 + (0.18 * (a['total_time'][b] - 10800) / 60)
    else:
        result = 1 + (0.44 * a['total_time'][b] / 60)

    if result < 0:
        result = 1

    return result

# initialize the 'cost' column
divvy['cost'] = 0

# iterate the function in the datafram
for ind in divvy.index:
  divvy['cost'][ind] = ride_value(divvy,ind)

divvy.to_csv('C:/Users/barry/~coding/R Programming/googleclass/divvytrips/divvy_cost.csv')
