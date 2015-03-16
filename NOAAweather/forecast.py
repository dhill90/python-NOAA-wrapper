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
        self.prod         = 'time-series'
        self.unt          = 'e'
        self.begin        = ''
        self.end          = ''

    def __point_url_construction__(self, list_lat_lon, begin, end, elements):
        listLatLon = "listLatLon={},{}".format(str(list_lat_lon[0][0]), str(list_lat_lon[0][1]))
        for lat,lon in list_lat_lon[1:]:
            listLatLon = "{}%20{},{}".format(listLatLon, str(lat), str(lon))
        product = "&product={}".format(self.prod)
        times = "&begin={}&end={}".format(begin, end)
        unit = "&Unit={}".format(self.unt)
        element_string = ""
        for elem in elements:
            new_element = "&{0}={0}".format(elem)
            element_string = "{}{}".format(element_string,new_element)
        return self.url + listLatLon + product + times + unit + element_string

    def __zip_url_construction__(self, zipcodelist, begin, end, elements):
        zipcodestring = "zipCodeList={}".format(str(zipcodelist[0]))
        for zipcode in zipcodelist[1:]:
            zipcodestring = "{}+{}".format(zipcodestring, str(zipcode))
        product = "&product={}".format(self.prod)
        times = "&begin={}&end={}".format(begin, end)
        times = "&begin={}&end={}".format(begin, end)
        unit = "&Unit={}".format(self.unt)
        element_string = ""
        for elem in elements:
            new_element = "&{0}={0}".format(elem)
            element_string = "{}{}".format(element_string,new_element)
        return self.url + zipcodestring + product + times + unit + element_string


    # @params: list of OrderedDicts
    # @return: a dictionary with each element/location the key for the list values.
    def __dict_to_dictlist__(self, params):
        return_dict = {}
        for location in range(len(params)):
            for ele in params[location]:
                if (ele != "@applicable-location"):
                    try:
                        element_values = params[location][ele]['value']
                        element_name = params[location][ele]['name']
                        element_name = element_name + ' ' + str(location)
                        return_dict[element_name] = element_values
                    except:
                        for counter in range(len(params[location][ele])):
                            element_values = params[location][ele][counter]['value']
                            element_name = params[location][ele][counter]['name']
                            element_name = element_name + ' ' + str(location)
                            return_dict[element_name] = element_values
        return return_dict


    # @params: list [(lat, lon)], begin, end, NDFD elements
    # @return: a dictionary with information about the NDFD elements
    def single_point(self, list_lat_lon, begin, end, elements):
        single_url = self.__point_url_construction__(list_lat_lon,begin,end,elements)
        with request.urlopen(single_url) as noaa:
            noaa_dict = xmltodict.parse(noaa.read())
        params = [noaa_dict['dwml']['data']['parameters']]
        # print (params)
        return_dict = self.__dict_to_dictlist__(params)
        return return_dict


    # @params: list [[lat, lon],[lat,lon]] product, begin, end, unit, NDFD elements
    # @return: a dictionary with information about the NDFD elements
    def multi_point(self, list_lat_lon, begin, end, elements):
        multi_url = self.__point_url_construction__(list_lat_lon, begin, end, elements)
        with request.urlopen(multi_url) as noaa:
            noaa_dict = xmltodict.parse(noaa.read())
        params = noaa_dict['dwml']['data']['parameters']
        return_dict = self.__dict_to_dictlist__(params)
        return return_dict

    def subgrid():
        pass

    def line():
        pass


    # @params: list[zip,zip], begin, end, unit, NDFD elements
    # @return: a dictionary with information about the NDFD elements
    def zipcodes(self, zipcodelist, begin, end, elements):
        zip_url = self.__zip_url_construction__(zipcodelist, begin, end, elements)
        with request.urlopen(zip_url) as noaa:
            noaa_dict = xmltodict.parse(noaa.read())
        params = noaa_dict['dwml']['data']['parameters']
        return_dict = self.__dict_to_dictlist__(params)
        return return_dict

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


# obj = Forecast()
# print (obj.single_point([(37.2988451,-78.40321589999999)], '','',['maxt','mint','pop12']))
# print (obj.multi_point([(37.2988451,-78.40321589999999),(37.299,-78.3011)], '','',['maxt','mint','pop12']))
# print (obj.zipcodes([23901,22015], '', '',['maxt','mint','pop12']))
