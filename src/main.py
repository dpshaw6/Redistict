from CensusTract import CensusTract

# States numbers from 01 to 50 (09=Connecticut)
ct_data = CensusTract("09")
print ct_data.get_population()
print ct_data.get_boundary()