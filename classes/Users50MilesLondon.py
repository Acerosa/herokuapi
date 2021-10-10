import requests
from geopy.geocoders import Nominatim
from geopy import distance
from geopy.distance import geodesic, great_circle
import marshmallow_dataclass
from dataclasses import dataclass, field

# This class is used to represent all the users that live within 50 miles of London
@dataclass
class User50MilesLondon:
    id:int
    first_name: str
    last_name: str
    email: str
    ip_address: str
    latitude:float
    longitude:float

    def __init__(self,id, first_name ,last_name, email ,ip_address, latitude,longitude):
        self.id =id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.ip_address=ip_address
        self.latitude=latitude
        self.longitude=longitude

    def getUsers(r):
        # this is variable with the London value
        cityOfLondon = 'london'
        # geolocator is use to get the location of from a latitude and longitude coordinates
        geoLocator = Nominatim(user_agent="geopiExercises")

        # getting the exact London location
        londonLocation = geoLocator.geocode(cityOfLondon)
        # list to add the users
        user50londonList = []
        # Setting the object to receive the data
        users = marshmallow_dataclass.class_schema(User50MilesLondon)()
        # connecting to the api
        req = requests.get(r)
        # parsing the data on to a dictionary
        users50s = req.json()
        # loop the select the users that match the codition
        for user in range(len((users50s))):
            loadUsers = users.load(users50s[user])
            # selection of the users
            if distance.distance((loadUsers.latitude, loadUsers.longitude), (londonLocation.latitude, londonLocation.longitude)).miles <= 50.00:
                user50londonList.append(loadUsers)
        return user50londonList

        # method to return headers
        def getHeaders(r):
            req = requests.get(r)
            return req.headers

        # method to return status_code
        def getCode(r):
            req = requests.get(r)
            return req.status_code

        def printUsers(r):
            print(getLUser(r))
