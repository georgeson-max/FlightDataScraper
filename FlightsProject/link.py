import datetime


def linkCreator(source, locations, dates, length):
    baselink = "https://www.google.com/travel/flights?q=Flights"
    links = []
    for location in locations:
        for date in dates:
            start = date.isoformat()[0:10]
            z = date + datetime.timedelta(days=length)
            end = z.isoformat()[0:10]
            links.append(baselink + '%20to%20' + location + '%20from%20' + source + '%20on%20' + start +'%20through%20' + end)

    return links

