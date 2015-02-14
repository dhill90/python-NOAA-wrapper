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
    list_lat_lon = []
    prod = Product.time-series
    unt = Unit.english
    begin = ''
    end = ''
    pass

    def __init__():
        pass

    # @params: list [[lat, lon]], begin, end, NDFD elements
    # @return: a dictionary with information about the NDFD elements
    def single_point(list_lat_lon,begin,end,elements):
        # Since we are only grabbing a single point... This is no big deal.
        listLatLon = "listLatLon=", list_lat_lon[0][0], ",", list_lat_lon[0][1]
        product = "&product=", prod.name
        times = "&begin=", begin, "&end=", end
        unit = "&Unit=", unt.name
        element_string = ""
        for elem in elements:
            new_element = "&", elem, "=", elem
            element_string += new_element
        single_url = url + listLatLon + product + times + unit + element_string
        return single_url

    # @params: list [[lat, lon],[lat,lon]] product, begin, end, unit, NDFD elements
    # @return: a dictionary with information about the NDFD elements
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
