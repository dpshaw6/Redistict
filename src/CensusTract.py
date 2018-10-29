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
    population = {}
    boundary = {}
    geography = {}
    POPULATION_API_STRING = "https://api.census.gov/data/2010/sf1?get=P0010001&for=tract:*&in=state:"
    GEOGRAPHY_API_STRING1 = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/8/query?"
    GEOGRAPHY_API_STRING2 = "&text=&objectIds=&time=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=TRACT%2CCOUNTY%2CSTATE&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&resultRecordCount=&queryByDistance=&returnExtentsOnly=false&datumTransformation=&parameterValues=&rangeValues=&f=json"
    
    def set_population_from_API(self, state_key):
        # Pull data from Census API
        url = self.POPULATION_API_STRING+str(state_key)
        response = requests.get(url)
        population_data = response.json()
        #[[u'P0010001', u'state', u'county', u'tract'], [u'4476', u'09', u'001', u'010101'], ...
        for line in population_data[1:]:
            population = int(line[0])
            state = line[1]
            county = line[2]
            tract = line[3]
            geokey = state+"_"+county+"_"+tract
            self.population[geokey] = population
            self.geography[geokey] = (state,county,tract)
            
        return
            
    def get_population(self):
        return self.population
    
    def set_boundary_from_API(self, state_key):
        # Pull data from Census API        
        # SQL: where=state%3D09+and+county%3D001+and+tract%3D010101
        for geokey, tract in self.geography.iteritems():
            sql_where = "where=state%3D"+tract[0]+"+and+county%3D"+tract[1]+"+and+tract%3D"+tract[2]
            url = self.GEOGRAPHY_API_STRING1+sql_where+self.GEOGRAPHY_API_STRING2
            response = requests.get(url)
            polygon = response.json()['features'][0]['geometry']['rings'][0]
            self.boundary[geokey] = polygon

        return
    
    def get_boundary(self):
        return self.boundary
    
    def __init__(self, state_key):
        self.set_population_from_API(state_key)
        self.set_boundary_from_API(state_key)
    
