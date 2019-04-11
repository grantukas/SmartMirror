from darksky import forecast
from datetime import date, timedelta

key = '93a522f375502ea4e4a091c06d034ff1'
orange = forecast(key, 33.779638, -117.853700)


ORANGE = 33.779638, (-117.853700)
weekday = date.today()
with forecast(key, *ORANGE) as orange:
    print(orange.daily.summary, end='\n---\n')
    for day in orange.daily:
        day = dict(day = date.strftime(weekday, '%a'),
                   sum = day.summary,
                   tempMin = day.temperatureMin,
                   tempMax = day.temperatureMax,
                   icon = day.icon
                   )
        # Save each of these in a list to display to GUI
        print('{day}: {sum} Temp range: {tempMin} - {tempMax}\t {icon}'.format(**day))
        weekday += timedelta(days=1)