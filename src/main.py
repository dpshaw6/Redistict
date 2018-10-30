DEBUG = True

from CensusTract import CensusTract



# States numbers from 01 to 50 (09=Connecticut)
#ct_data = CensusTract("09", "API", True) # Read from API and Save
ct_data = CensusTract("09", "FILE", False) # Read from file
if DEBUG:
    print_count = 5
    i_count = 0
    for geokey, pop in ct_data.get_population().iteritems():
        if i_count > print_count:
            break
        print ct_data.get_population()[geokey]
        print ct_data.get_boundary()[geokey]
        i_count = i_count + 1

