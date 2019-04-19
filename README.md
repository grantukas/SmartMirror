# SmartMirror

[Tkinter display GIF](https://www.daniweb.com/programming/software-development/code/216550/tkinter-to-put-a-gif-image-on-a-canvas-python)

[Tkinter documentation](https://effbot.org/tkinterbook/tkinter-index.htm)

[Dark Sky API docs](https://darksky.net/dev/docs)

[News Api](http://www.rychdata.com/the-news-api-requesting-live-headlines-with-python.html)

[Calander API](https://developers.google.com/calendar/quickstart/python)

## Issues with GoogleAPIClient
GoogleAPIClient is deprecated so use the [Google API Client Library for Python](https://developers.google.com/api-client-library/python/)

## Python libraries to install before running
There are a number of libraries that must be installed in order to run the SmartMirror. The libraries to install are as follows:
* News API
* Forecastiopy for DarkSky API
* Google API Client
* Google oauthlib
* Google Assistant API (separate script to run on Raspberry Pi)

To install news API:
```
sudo pip3 install newsapi-python
```
To install Forecastio for DarkSky weather:
```
sudo pip3 install forecastiopy
```
To install Google API Client library:
```
sudo pip3 install --upgrade google-api-python-client
```
To install Google oauthlib:
```
sudo pip3 install google-auth-oauthlib
```
