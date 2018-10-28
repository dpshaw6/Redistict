# CensusTract.py is the class defining a Census Tract. The data is populated
# using the US Census Data API.
#
# Fields:
#  - Population (Integer)
#  - Boundary (Dictionary)
#    - length (Real - m -some unit(?))
#    - nodes [List of Nodes]
#    - edges [List of Edges]
#
# Methods:
#  - set_population_from_API
#  - get_population
#  - set_boundary_from_API
#  - get_population
import requests

class CensusTract:
    __population = -1
    __boundary = {}
    __POPULATION_API_STRING = "https://api.census.gov/data/2010/sf1?get=P0010001&for=tract:*&in=state:"
    __POPULATION_API_STRING = "https://api.census.gov/data/2010/sf1?get"
    __POPULATION_API_STRING = "https://api.census.gov/data/2010/sf1?get=P0010001&for=tract:*&in=state:"
    
    def set_population_from_API(self, state_key):
        # Pull data from Census API
        # https://api.census.gov/data/2010/sf1?get=P0010001&for=tract:*&in=state:02+county:170
        url = self.__POPULATION_API_STRING+str(state_key)
        response = requests.get(url)
        return response.json()
            
    def get_population(self):
        return self.__population
    
    def set_boundary_from_API(self, state_key):
        # Pull data from Census API
        population = self.__population
        pass
    
    def get_boundary(self):
        return self.__boundary
    
    def __init__(self, state_key):
        self.__population = self.set_population_from_API(state_key)
        self.__boundary = self.set_boundary_from_API(state_key)
    
