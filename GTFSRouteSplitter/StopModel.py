#-----------------------------------------------------------------------------
# stop_id
# stop_code
# stop_name
# stop_desc
# stop_lat
# stop_lon
# stop_url
# location_type
# parent_station
# tpis_name
#-----------------------------------------------------------------------------
from CSVRowModel import CSVRowModel

class StopModel(CSVRowModel):

	headerNames = "stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,stop_url,location_type,parent_station,tpis_name"

	#-----------------------------------------------------------------------------
	def __init__(self):
		super(StopModel, self).__init__(StopModel.headerNames)

