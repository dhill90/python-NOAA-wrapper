try:
    import urllib.request as request
    import xmltodict
    assert xmltodict
    import datetime
    assert datetime
except ImportError:
    pass

# Class for gathering unsummarized data.
class Forecast(object):
    # This object is used to make a variety of calls to the weather weather.gov ndfdxmlclient.
    # Hopefully the object will appear as more of a module for pure functions.
    url = 'http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?'

    def __init__(self):
        self.list_lat_lon = []
        self.prod = 'time-series'
        self.unt = 'e'
        self.begin = ''
        self.end = ''

    def __point_url_construction__(self,list_lat_lon,begin,end,elements):
        listLatLon = "listLatLon={},{}".format(str(list_lat_lon[0][0]), str(list_lat_lon[0][1]))
        for lat,lon in list_lat_lon[1:]:
            listLatLon = "{} {},{}".format(listLatLon, str(lat), str(lon))
        product = "&product={}".format(self.prod)
        times = "&begin={}&end={}".format(begin, end)
        unit = "&Unit={}".format(self.unt)
        element_string = ""
        for elem in elements:
            new_element = "&{0}={0}".format(elem)
            element_string = "{}{}".format(element_string,new_element)
        return self.url + listLatLon + product + times + unit + element_string


    # @params: list [[lat, lon]], begin, end, NDFD elements
    # @return: a dictionary with information about the NDFD elements
    def single_point(self,list_lat_lon,begin,end,elements):
        single_url = self.__point_url_construction__(list_lat_lon,begin,end,elements)
        with request.urlopen(single_url) as noaa:
            noaa_dict = xmltodict.parse(noaa.read())
        params = noaa_dict['dwml']['data']['parameters']
        print (params)
        return #params


    # @params: list [[lat, lon],[lat,lon]] product, begin, end, unit, NDFD elements
    # @return: a dictionary with information about the NDFD elements
    def multi_point(self,list_lat_lon,begin,end,elements):
        multi_url = self.__point_url_construction__(list_lat_lon,begin,end,elements)
        return multi_url

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



obj = Forecast()
#print(obj.__point_url_construction__([(37.2988451,-78.40321589999999)], '','',['maxt','mint','pop12']))
print (obj.single_point([(37.2988451,-78.40321589999999)], '','',['maxt','mint','pop12']))
