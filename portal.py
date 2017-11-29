from datetime import datetime
import time
def store_events(events):
    calendar = {}
    for x in events:
        split_events = x.split(",")
        calendar.update({split_events[0]: [split_events[1], split_events[2]]})
    return calendar

all_events = store_events(["Interview at The Portal, 2/23/17, 3:00 PM - 4:30PM",
             "Lunch with Cindy, 2/25/17, 12:00PM - 1:00PM",
                "Dinner with John, 2/24/17, 5:00PM - 5:30PM",
                "Conference, 2/24/17, 11:00AM - 5:30PM",
                    "Breakfast with Stanley, 2/24/17, 11:00AM - 12:00 AM",
                    "Dance with Cara, 2/25/17, 12:00 PM - 1:00 PM",
                    "Party with Dad, 3/13/19, 12:00 PM - 1:00 PM",
                    "Birthday for Jon, 5/20/17, 1:00 PM - 2:00 PM"])

def conflicted_events(all_events):
    result = []
    comparison_dates = []
    comparison_times = []
    for event in all_events:
        dates, times = all_events[event]
        date = dates.strip()
        time = times.strip()
        print(time)
        if date in comparison_dates:
            if time in comparison_times:
                result.append(event)
            else:
                comparison_times.append(time)
        else:
            comparison_dates.append(date)
        #a = datetime.strptime(str(date), "%m/%d/%y")
    return result
print(conflicted_events(all_events))




