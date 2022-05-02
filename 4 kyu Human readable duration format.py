def format_duration(seconds):

    if seconds == 0:
        return 'now'

    year = seconds // 31536000  # seconds in a year
    day = seconds % 31536000 // 86400  # seconds in a day
    hour = seconds % 86400 // 3600  # seconds in a hour
    minute = seconds % 3600 // 60  # seconds in a minute
    second = seconds % 60  # other seconds

    # here we set correct output for each time period
    # years
    if year > 1:
        years = f'{year} years,'
    elif year == 1:
        years = f'{year} year,'
    else:
        years = ''

    # days
    if day > 1:
        days = f'{day} days,'
    elif day == 1:
        days = f'{day} day,'
    else:
        days = ''

    # hours
    if hour > 1:
        hours = f'{hour} hours,'
    elif hour == 1:
        hours = f'{hour} hour,'
    else:
        hours = ''

    # minutes
    if minute > 1:
        minutes = f'{minute} minutes,'
    elif minute == 1:
        minutes = f'{minute} minute,'
    else:
        minutes = ''

    # seconds
    if second > 1:
        seconds = f'{second} seconds,'
    elif second == 1:
        seconds = f'{second} second,'
    else:
        seconds = ''

    # here we unite time periods except last for correct output
    present = []
    values = [year, day, hour, minute, second]
    time = [years, days, hours, minutes, seconds]
    for index, period in enumerate(values):
        if period > 0:
            present.append(time[index])

    # here we solve problems with 'and' output
    time_interval = len(present)
    if time_interval > 1:
        time_interval_except_one = present[:time_interval - 1]
        united_time_interval_except_one = ' '.join(time_interval_except_one)[:-1]
        print(time_interval_except_one)
        print(united_time_interval_except_one)
        result = f'{united_time_interval_except_one} and {present[-1]}'
        return result[:-1]
    else:
        # if time period only we don't need 'and'
        return present[0][:-1]  # we remove comma in the end


number = int(input())
print(format_duration(number))


# My solution
# https://www.codewars.com/kata/52742f58faf5485cae000b9a/solutions/python/me/best_practice
