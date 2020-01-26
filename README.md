# google-geocode
Retrieve the most populated cities by webscrapping and using these locations to print their respective elevation using google's elevation and location APIs.

## Getting Started
These instructions will allow you to run the project on your local machine.

### Prerequisites
You will need to obtain an api key from google, there is a list of google's API at https://developers.google.com/apis-explorer/

You will also need the following python packages installed on your machine: 
```
python -m pip install matplotlib
```

```
pip install beautifulsoup4
```

```
pip install pandas
```

```
pip install requests
``` 
### Instructions

* Make sure you have downloaded all th packpages in the "Prerequisites". Next download "elevation.py". and "cities.py". elevation.py imports funcions from cities.py
* A seperate python file named "apikey.py" will need to be created containing the line "key = "YOUR API KEY" with the api key you retrieve from google 
* Ensure that these three files(elevation.py, cities.py, and apikey.py) are in the same directory or they will not be able to import each other. 
* **Finally**, run the elvation.py file and the project will start

## Authors

* **Michael Jones** 
