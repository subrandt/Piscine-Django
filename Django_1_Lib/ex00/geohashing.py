import sys, antigravity

# The antigravity.geohash function is a hidden function in Python's antigravity module.
# It takes three arguments: latitude, longitude, and a date encoded as bytes.
# This function uses these inputs to generate a geohash, which is a coded representation of the latitude and longitude.
# The geohash is printed to the console. Note that this function does not return any value.
# This function is a humorous reference to an XKCD webcomic about geohashing and is not intended for serious use.
def geohash(latitude, longitude, date):
    antigravity.geohash(latitude, longitude, date.encode())

def parse_date(date):
    try:
        int(date)
    except ValueError:
        print("Error: Date must be in the format YYYYMMDD")
        return False
    if len(date) != 8:
        print("Error: Date must be in the format YYYYMMDD")
        return False
    
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    if not (1 <= month <= 12 and 1 <= day <= 31):
        print("Error: Month must be between 1 and 12, and day must be between 1 and 31")
        return False
    if not (1 <= year <= 9999):
        print("Error: Year must be between 1 and 9999")
        return False
    if month == 2 and day > 29:
        print("Error: February cannot have more than 29 days")
        return False
    if month in [4, 6, 9, 11] and day > 30:
        print("Error: Month {} cannot have more than 30 days".format(month))
        return False
    if month == 2 and day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        print("Error: Year {} is not a leap year".format(year))
        return False
    return True

def parse_latitude(latitude):
    if not -90.0 <= latitude <= 90.0:
        print("Error: Latitude must be between -90 and 90")
        return False
    return True

def parse_longitude(longitude):
    if not -180.0 <= longitude <= 180.0:
        print("Error: Longitude must be between -180 and 180")
        return False
    return True

def parse_args(latitude, longitude, date):

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        print("Error: Latitude and Longitude must be numbers")
        sys.exit(1)
    if not parse_latitude(latitude):
        sys.exit(1)
    if not parse_longitude(longitude):
        sys.exit(1)
    if not parse_date(date):
        sys.exit(1)
    

    geohash(latitude, longitude, date)

if __name__ == '__main__':
    
    if len(sys.argv) == 4:
            parse_args(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python geohashing.py <latitude> <longitude> <date>")