#
# Dependencies
#

import os
import csv
import sys

#
# Constants
#

CSV_PATH = os.path.join(os.path.dirname(__file__), 'cities.csv')

#
# Define class
#

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = float(lat)
    self.lon = float(lon)

  def __str__(self):
    return f"{self.name}, {self.lat:f}, {self.lon:f}"

  def __repr__(self):
    return f"City({self.name}, {self.lat:f}, {self.lon:f})"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
    with open(CSV_PATH, 'r') as csvfile:
      csv_cities = csv.reader(csvfile)
      
      # Skip headers
      next(csv_cities)

      for city in csv_cities:
        cities.append(City(city[0], city[3], city[4]))
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# Get latitude and longitude values from the user
coord1_input = input('Enter (lat1, lon1): ')
coord1 = coord1_input.split(',')
lat1 = float(coord1[0])
lon1 = float(coord1[1])

coord2_input = input('Enter (lat2, lon2): ')
coord2 = coord2_input.split(',')
lat2 = float(coord2[0])
lon2 = float(coord2[1])

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  within = []

  # Ensure lat and lon values are floats.
  lat1 = float(lat1)
  lat2 = float(lat2)
  lon1 = float(lon1)
  lon2 = float(lon2)

  def isWithinBounds(city_lat, city_lon):
    if (lat1 > lat2):
      if (lon1 > lon2):
        if city_lat <= lat1 and city_lat >= lat2 and city_lon <= lon1 and city_lon >= lon2:
          return True
        else:
          return False
      else:
        if city_lat <= lat1 and city_lat >= lat2 and city_lon <= lon2 and city_lon >= lon1:
          return True
        else:
          return False
    else:
      if (lon1 > lon2):
        if city_lat <= lat2 and city_lat >= lat1 and city_lon <= lon1 and city_lon >= lon2:
          return True
        else:
          return False
      else:
        if city_lat <= lat2 and city_lat >= lat1 and city_lon <= lon2 and city_lon >= lon1:
          return True
        else:
          return False

  # Check if city is within the specified coordinates.
  for city in cities:
    if isWithinBounds(city.lat, city.lon):
      within.append(city)

  return within

citymatch = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
print(citymatch)
