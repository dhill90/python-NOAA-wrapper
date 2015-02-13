import urllib2
import xml
import datetime
import Enum

class Products(object):
    # Most used - receives all data between given 'begin' and 'end' times.
    time-series = 0
    # Unused - receives only data on maxt, mint, sky, wx, and icons for 'begin' and 'end' times.
    glance = 1

class Unit(object):
    #English
    e = 0
    #Metric
    m = 1

# Class for gathering unsummarized data.
class Forecast(object):
    url = 'http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?'
    lat = ''
    lon = ''
    prod = Product.time-series
    unit = Unit.english
    begin = ''
    end = ''
    pass

    def __init__():
        pass

    def single_point():
        pass

    def multi_point():
        pass

    def subgrid():
        pass

    def line():
        pass

    def zipcodes():
        pass

    def city():
        pass

    def subgrid_center():
        pass

class PointFinder(object):
    pass

    def subgrid():
        pass

    def line():
        pass

    def zipcodes():
        pass

    def cities():
        pass

    def subgrid_center():
        pass

    def corners_grid():
        pass
