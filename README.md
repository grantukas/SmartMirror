# SmartMirror

<image src="images/SmartMirror2.jpg" width="286"> <image src="images/SmartMirror.jpg" width = 575>

## Summary of the SmartMirror project
The goal of this project is to create a simple, Python-based smart mirror. We chose to design a smart mirror because it can be more seamlessly integrated within a home, as opposed to a smart speaker, and still has the same functionality along with the added benefits of a GUI.

To use the SmartMirror, you only need to run the SmartMirror.py code. There are libraries that need to be installed and settings that can be customized before running. A comprehensive build guide is below. Please be sure to run the code using Python 3.



### Python libraries to install before running
There are a number of libraries that must be installed in order to run the SmartMirror. If you already have Pandas or any other libraries, please make sure they are updated to the latest version. The libraries to install are as follows:
* Pandas
* News API
* Forecastiopy for DarkSky API
* Google API Client
* Google oauthlib
* Google Assistant API (separate script to run on Raspberry Pi)

If there are any errors installing, such as "module not found", try installing with pip.
If you need elevated permissions to install, run "sudo pip3 <LIBRARY_TO_INSTALL>"

To install Pandas:
```
pip3 install pandas
```

To install News API:
```
pip3 install newsapi-python
pip3 install newsapi
```
To install Forecastio for DarkSky weather:
```
pip3 install forecastiopy
pip3 install darkskylib
```
To install Google API Client library:
```
pip3 install --upgrade google-api-python-client
```
To install Google oauthlib:
```
pip3 install google-auth-oauthlib
```



### Configure width and height for your display
The SmartMirror.py code launches a GUI using Tkinter, a built in Python library. The GUI is launched in fullscreen mode, with no borders to the window. So, you need to make sure that you configure the aspect ratio to that of your screen so everything scales appropriately.

Within the SmartMirror.py file, use your favorite text editor to change the variables WIDTH and HEIGHT:
```
WIDTH = X
HEIGHT = Y
```
where X is the width of your display and Y is the height of your display.
Furthermore, at the bottom of the SmartMirror.py, change window.geometry:
```
window.geometry('800x600')
```
Replace the values 800 and 600 with the same width and height values that you have above.
Be sure to leave it in the format '800x600'.

If you cannot see the clock and calendar information in the upper-right corner(or it is cut off), you can manually adjust the spacing so that the elements are in the frame. To do so, find line 122 in the SmartMirror.py code, where this block of code lives:
```
# Adjust this width for spacing
frame_placeholder = Frame(self, width=WIDTH/8, height=10, bg='black')
frame_placeholder.grid(row=0, column=1)
```
You can change the frame_placeholder width=WIDTH/8 value. For example, if you divide the width by a higher number, such as 8 or 10, it will make the spacing shorter, bringing the time and calendar elements closer to the middle of the frame. Conversely, if you make the value smaller, like 2 or 3, then the spacing will be greater. You can play with values to see what suits your aspect ratio the best.



### OPTIONAL- Set weather location to your location
The location for weather forecasts can be changed to be something other than Orange, CA.
To change the location, you must get the latitude and longitude of your location which can be done easily with [LatLong.net](https://www.latlong.net/)

Within the SmartMirror.py file, change the variable ORANGE:
```
ORANGE = {LATITUDE}, {LONGITUDE}
```
Replace the values {LATITUDE} and {LONGITUDE} with that of your location.



### After installing all the libraries, you are ready to run!
Be sure you are in the SmartMirror directory, and run the SmartMirror.py program using Python 3 with:
```
python3 SmartMirror.py
```
For the first launch, you will be asked by the Google Auth API to connect to your Google Account to access your Google Calendar information. The prompt will look something like:
```
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?re........
```
Copy and paste the link into your browser and sign into your Google Account. Allow Quickstart permission to access your calendar (so it can get your upcoming events on your calendar). Once completed, it will tell you to close the window, and the SmartMirror program will launch! If at any time you wish to exit, hitting the escape button (ESC) will stop and close the program.

If you are not running this on a Raspberry Pi 3 B+, then you can stop here. If you are running this on a Raspberry Pi but don't want Google Assistant, you can also stop here. Enjoy your new Smart Mirror!



## Set up Google Cloud Project to get API access key (RASPBERRY PI ONLY)
Please follow this link to get Google Assistant set up on your Raspberry Pi 3 B+: [Voice Activated Google Assistant](https://www.novaspirit.com/2017/05/23/voice-activated-google-assistant-raspberry-pi/)

NOTE: The Assistant SDK with voice activation only works on the Raspberry Pi 3 B+. It will NOT work on any other Raspberry Pi model. If you do not want voice activation/have an older Raspberry Pi, you can activate Assistant with the keyboard or a wired-in button. However, this is a topic for another tutorial.

### Extra info and sources

[Tkinter display GIF](https://www.daniweb.com/programming/software-development/code/216550/tkinter-to-put-a-gif-image-on-a-canvas-python)

[Tkinter documentation](https://effbot.org/tkinterbook/tkinter-index.htm)

[Dark Sky API docs](https://darksky.net/dev/docs)

[News Api](http://www.rychdata.com/the-news-api-requesting-live-headlines-with-python.html)

[Calander API](https://developers.google.com/calendar/quickstart/python)

### Issues with GoogleAPIClient
GoogleAPIClient is deprecated so use the [Google API Client Library for Python](https://developers.google.com/api-client-library/python/)
