#-----------------------------------------------------------------------------
# trip_id
# arrival_time
# departure_time
# stop_id
# stop_sequence
# stop_headsign
# pickup_type
# drop_off_type
#-----------------------------------------------------------------------------
from CSVRowModel import CSVRowModel

class StopTimeModel(CSVRowModel):

	headerNames = "trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type"

	#-----------------------------------------------------------------------------
	def __init__(self):
		super(StopTimeModel, self).__init__(StopTimeModel.headerNames)

