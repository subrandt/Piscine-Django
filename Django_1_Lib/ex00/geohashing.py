import sys, antigravity

def geohash(latitude, longitude, date):
    antigravity.geohash(latitude, longitude, date.encode())

def parse_args(latitude, longitude, date):
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        print("Error: Latitude and Longitude must be numbers")
        sys.exit(1)
    if not -90.0 <= latitude <= 90.0:
        print("Error: Latitude must be between -90 and 90")
        sys.exit(1)
    if not -180.0 <= longitude <= 180.0:
        print("Error: Longitude must be between -180 and 180")
        sys.exit(1)
    if len(date) != 8:
        print("Error: Date must be in the format YYYYMMDD")
        sys.exit(1)
    try:
        int(date)
    except ValueError:
        print("Error: Date must be in the format YYYYMMDD")
        sys.exit(1)

    geohash(latitude, longitude, date)

if __name__ == '__main__':
    
    if len(sys.argv) == 4:
            parse_args(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python geohashing.py <latitude> <longitude> <date>")