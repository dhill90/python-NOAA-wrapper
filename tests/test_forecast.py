import unittest
from NOAAweather import forecast

class NOAAweatherTester(unittest.TestCase):

    def test_single_point(self):
        obj = forecast.Forecast()
        response = (obj.single_point([(37.2988451,-78.40321589999999)], '','',['maxt','mint','pop12','qpf','sky','snow','temp']))
        self.assertIn('Daily Maximum Temperature 0',response)
        self.assertIn('Daily Minimum Temperature 0',response)
        self.assertIn('12 Hourly Probability of Precipitation 0',response)
        self.assertIn('Liquid Precipitation Amount 0',response)
        self.assertIn('Cloud Cover Amount 0',response)
        self.assertIn('Snow Amount 0',response)
        self.assertIn('Temperature 0',response)

    def test_multi_point(self):
        obj = forecast.Forecast()
        response = (obj.multi_point([(37.2988451,-78.40321589999999),(37.299,-78.3011)], '','',['maxt','mint','pop12','qpf']))
        self.assertIn('Daily Maximum Temperature 0',response)
        self.assertIn('Daily Minimum Temperature 0',response)
        self.assertIn('12 Hourly Probability of Precipitation 0',response)
        self.assertIn('Liquid Precipitation Amount 0',response)
        self.assertIn('Daily Maximum Temperature 1',response)
        self.assertIn('Daily Minimum Temperature 1',response)
        self.assertIn('12 Hourly Probability of Precipitation 1',response)
        self.assertIn('Liquid Precipitation Amount 1',response)

    def test_zipcodes(self):
        obj = forecast.Forecast()
        response = (obj.zipcodes([23901,23909], '','',['maxt','mint','pop12','qpf','sky','snow','temp']))
        self.assertIn('Daily Maximum Temperature 0',response)
        self.assertIn('Daily Minimum Temperature 0',response)
        self.assertIn('12 Hourly Probability of Precipitation 0',response)
        self.assertIn('Liquid Precipitation Amount 0',response)
        self.assertIn('Cloud Cover Amount 0',response)
        self.assertIn('Snow Amount 0',response)
        self.assertIn('Temperature 0',response)
        self.assertIn('Daily Maximum Temperature 1',response)
        self.assertIn('Daily Minimum Temperature 1',response)
        self.assertIn('12 Hourly Probability of Precipitation 1',response)
        self.assertIn('Liquid Precipitation Amount 1',response)
        self.assertIn('Cloud Cover Amount 1',response)
        self.assertIn('Snow Amount 1',response)
        self.assertIn('Temperature 1',response)

    def test_simple_calls(self):
        self.assertIn('Daily Maximum Temperature 0', forecast.maxt(37.2988,-78.4032))
        self.assertIn('Daily Minimum Temperature 0', forecast.mint(37.2988,-78.4032))
        self.assertIn('Temperature 0', forecast.temp(37.2988,-78.4032))
        self.assertIn('12 Hourly Probability of Precipitation 0', forecast.pop12(37.2988,-78.4032))
        self.assertIn('Liquid Precipitation Amount 0', forecast.qpf(37.2988,-78.4032))

if __name__ == '__main__':
    unittest.main()
