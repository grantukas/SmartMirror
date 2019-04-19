# SmartMirror

[Tkinter display GIF](https://www.daniweb.com/programming/software-development/code/216550/tkinter-to-put-a-gif-image-on-a-canvas-python)

[Tkinter documentation](https://effbot.org/tkinterbook/tkinter-index.htm)

[Dark Sky API docs](https://darksky.net/dev/docs)

[News Api](http://www.rychdata.com/the-news-api-requesting-live-headlines-with-python.html)

[Calander API](https://developers.google.com/calendar/quickstart/python)

## Issues with GoogleAPIClient
GoogleAPIClient is deprecated so use the [Google API Client Library for Python](https://developers.google.com/api-client-library/python/)

## Summary of the SmartMirror project
The goal of this project is to create a simple, Python-based smart mirror. We chose to design a smart mirror because it can be more seamlessly integrated within a home, as opposed to a smart speaker, and still has the same functionality along with the added benefits of a GUI.

To use the SmartMirror, you only need to run the SmartMirror.py code. There are libraries that need to be installed and settings that can be customized before running. A comprehensive build guide is below.

### Python libraries to install before running
There are a number of libraries that must be installed in order to run the SmartMirror. The libraries to install are as follows:
* News API
* Forecastiopy for DarkSky API
* Google API Client
* Google oauthlib
* Google Assistant API (separate script to run on Raspberry Pi)

To install News API:
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

### Configure aaspect ratio for your display
The SmartMirror.py code launches a GUI using Tkinter, a built in Python library. The GUI is launched in fullscreen mode, with no borders to the window. So, you need to make sure that you configure the aspect ratio to that of your screen so everything scales appropriately.

Within the SmartMirror.py file, change:``` WIDTH = 800
HEIGHT = 600 ``` to the width and height of your display.

### Set up weather settings to your location


### Set up Google Cloud Project to get API access key
