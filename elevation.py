import requests
import cities
import pandas as pd
import matplotlib.pyplot as plt
from apikey import key

apikey = key


# find elevation function and return it
def elevationlatlng(lat, lon, apikey):

    # url of geoelevation api
    url = "https://maps.googleapis.com/maps/api/elevation/json"

    # the requests library will make a GET request to a web server
    # which will download the HTML contents of a given web page
    response = requests.get(url + "?locations="+str(lat) + "," + str(lon) +
     "&key="+apikey)

    # status codes indicate the success of a specific HTTP request
    # print("Status code: "+ str(response.status_code)+"\n")

    # The type of the return of .json() is a dictionary
    # so you can access values in the object by key.
    data = response.json()

    # location for elevation within the dictionary
    # print("Elevation: "+str(data['results'][0]["elevation"])+" meters\n")

    return data['results'][0]["elevation"]


# finding the lat and lng of address
# return string with lat seperated by a common with lng (x,y)
def locationlatlng(address, apikey):

    # url of geocode api
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    response = requests.get(url+address+"&key="+apikey)
    # print(url+address+"&key="+apikey)
    data_json = response.json()



    # print("Status code latlng: "+ str(response.status_code)+"\n")

    # location for lat and lng within the data_json dictionary

    lat = data_json['results'][0]["geometry"]["location"]["lat"]
    lng = data_json['results'][0]["geometry"]["location"]["lng"]

    return str(lat)+","+str(lng)


# main operation function
def main():

    # test functions
    '''
    city or adress("1600 Amphitheatre Parkway, Mountain View, CA")
    address=input("Enter address: ")
    print("\n")
    cord=locationlatlng(address,apikey)
    cord=cord.split(",")

    temp=elevation(cord[0],cord[1],apikey)
    print("this is temp"+str(temp))
    '''

    locations = cities.find()
    el = []
    place = []

    # throw locations in fucntions to find there respective elevations
    for city in locations:
        cord = locationlatlng(city, apikey)
        cord = cord.split(",")
        place.append(city)
        el.append(elevationlatlng(cord[0], cord[1], apikey))

    # create dictionary
    city_stats = {"City": place,
                "Elevation(m)": el}

    # create pandas Dataframe with previous dictionary inside
    dft = pd.DataFrame(city_stats)

    # print dataframe without index
    print(dft.to_string(index=False))

    # use matplotlib to display the scatter between elevations and cities
    plt.scatter(place, el)
    plt.ylabel('Meters(Elevation)')
    plt.xlabel('Cities')
    plt.show()


if __name__ == '__main__':
    main()
