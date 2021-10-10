import requests
import marshmallow_dataclass
from dataclasses import dataclass, field


@dataclass
class User:
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

    # function to get the users from payload
    def getUsers(r):
        # list to add the users
        userList = []
        # Setting the object to receive the data
        users = marshmallow_dataclass.class_schema(LondonUser)()
        # connecting to the api
        lodonUsers = requests.get(r)
        # parsing the data on to a dictionary
        lUsers = lodonUsers.json()
        # loop to get append the users on to a list of users
        for user in range(len((lUsers))):
            newuser = users.load(lUsers[user])
            userList.append(newuser)
        return userList

    # method to return headers
    def getHeaders(r):
        req = requests.get(r)
        return req.headers

    # method to return status_code
    def getCode(r):
        req = requests.get(r)
        return req.status_code
    # method to print the users
    def printUsers(r):
        print(User.getUsers(r))