import requests, re, unittest
from classes.LondonUsers import LondonUser
from classes.Users import User
from classes.Users50MilesLondon import User50MilesLondon
from classes.Tests import *

# print(LondonUser.getLUser('https://bpdts-test-app.herokuapp.com//city/London/users'))
# print(User50MilesLondon.getL50User('https://bpdts-test-app.herokuapp.com/users'))

londonUsers = LondonUser.getUsers('https://bpdts-test-app.herokuapp.com//city/London/users')

LondonUser.printUsers('https://bpdts-test-app.herokuapp.com//city/London/users')


class UnitTest(unittest.TestCase):
    def test_valid_first_name(self):
        self.assertTrue(Tests.first_name_check('ricardothe5'))

    def test_first(self):
        print('Just a test case')
        print(LondonUser.getUsers('https://bpdts-test-app.herokuapp.com//city/London/users')[1])

    # def test_headers_code(self):
    #     self.assertEqual(LondonUser.getHeaders('https://bpdts-test-app.herokuapp.com//city/London/users'), 6, 'headers are not right')

    def test_status_code(self):
        self.assertEqual(LondonUser.getCode('https://bpdts-test-app.herokuapp.com//city/London/users'), 200, 'code not valid')

    def test_valid_email(self):
        self.assertTrue(Tests.email_check(londonUsers[1].email))

    def test_valid_ip_address(self):
        self.assertTrue(Tests.ip_address_check(londonUsers[1].ip_address))

    def tes_valid_ip_address_format(self):
        self.assertTrue(Tests.ip_address_check_format(londonUsers[1].ip_address))


