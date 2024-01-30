from datetime import datetime
import time
import pytz

def calculate_time_difference(city1, city2):
    india_time = pytz.timezone('Asia/Kolkata')
    usa_time = pytz.timezone(city2)

    current_time_india = datetime.now(india_time)
    print(current_time_india)
    current_time_usa = datetime.now(usa_time)
    print(current_time_usa)
    time_difference = current_time_india - current_time_usa
    return time_difference


time_difference = calculate_time_difference('Asia/Kolkata', 'America/New_York')
print(f'Time difference between India and USA: {time_difference}')

