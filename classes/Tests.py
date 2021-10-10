import re

class Tests:
    # Test for a valid first name
    def first_name_check(first_name):
        if ' ' not in first_name:
            return True
        if first_name.isupper():
            return True
        if not any(c.isdigit() for c in first_name):
            return True
        return False

    # Test for a valid second name
    def last_name_check(last_name):
        if ' ' not in last_name:
            return True
        if last_name.isupper():
            return True
        if int not in last_name:
            return True
        return False

    # Test for a valid email
    def email_check(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return bool(re.fullmatch(regex, email))

    # test for a valid ip address
    def ip_address_check(ip_address):
        return ip_address.replace('.','').isdigit()

    # test for a valid ip address format
    def ip_address_check_format(ip_address):
        ipcheck = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        return bool(ipcheck.match(ip_address))

    # Test for a valid latitude
    def latitude_check(latitude):
        return type(latitude) == float

    # Test for a valid longitude
    def logitude_check(longitude):
        return type(longitude) == float






