import datetime
import link
import scraper
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



locations = ['FCO','MXP','VCE']
source = 'RNO'
duration = 7
days_to_check = 10

dates=[]
for i in range(days_to_check):
    dates.append(datetime.datetime(2023, 6, 10)+datetime.timedelta(days=i))

urls = link.linkCreator(source,locations,dates,duration)

prices=[]
for url in urls:
    prices.append(scraper.scraper(url))

table = []
i=0
for location in locations:
    for date in dates:
        table.append({
            "Source": source,
            "Destination": location,
            "Date": date.isoformat()[0:10],
            "Price": prices[i]
        })
        # print(source, 'to', location, 'on', date.isoformat()[0:10], 'for', duration, 'days costs', prices[i], 'round trip')
        i+=1

df = pd.DataFrame(table)
pivot = df.pivot(index='Destination',columns='Date',values='Price')
print(pivot)
                    


sns.heatmap(pivot, annot=True, fmt='.0f', cmap="RdYlGn_r")
plt.show()
