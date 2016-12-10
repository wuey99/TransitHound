#-----------------------------------------------------------------------------
# route_id
# service_id
# trip_id
# trip_headsign
# direction_id
# block_id
# shape_id
#-----------------------------------------------------------------------------
from CSVRowModel import CSVRowModel

class TripModel(CSVRowModel):

	headerNames = "route_id,service_id,trip_id,trip_headsign,direction_id,block_id,shape_id"

	#-----------------------------------------------------------------------------
	def __init__(self):
		super(TripModel, self).__init__(TripModel.headerNames)

