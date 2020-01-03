from bs4 import BeautifulSoup
import requests


# find cities, return names as a list
def find():

    # the requests library will make a GET request to a web server
    # this which will download the HTML contents of a given web page
    page = requests.get("http://worldpopulationreview.com/world-cities/")

    # status codes indicate the succuss of a specific HTTP request
    # print(page.status_code)

    # created an object of Beauiful soup

    soup = BeautifulSoup(page.content, 'html.parser')

    # to print well formated information of the website
    # print(soup.prettify())

    # prints the desired <ol> list
    # data = soup.find('ol')
    # print(data.text)

    # this will find all <li>
    # although, there are uneeded <li> that do not contain the cities
    # n_list = []

    '''
    for name in soup.find_all('li'):
        n_list.append(name.text)
    '''

    # this fuction works becayse the cities are stored in the ONlY <ol>
    # in the entire HTML file
    # append each <li> element in a text format to the locatons list
    # elements will appear as for ex. ["Tokyo (Population: 37,435,191)"]
    locations = []
    name = soup.find('ol') 
    for place in name.find_all('li'):
        locations.append(place.text)

    # print("before")
    # print(b)

    # pop because there was a random uneeded value at the end of the list
    locations.pop()

    # print("after")
    # print(b)

    # of type <class 'list'>
    # print(type(b))

    # temp is going to be list of the components of i seperated by spaces
    # temp[0] is the name of the city and it will update the locations list
    num = 0
    for i in locations:
        temp = i.split(" ")
        locations[num] = temp[0]
        num += 1

    return locations


test = find()

# <class 'list'>, list of strings
# print(type(test))
# print(test)
