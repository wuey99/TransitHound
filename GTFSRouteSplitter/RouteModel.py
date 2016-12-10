#-----------------------------------------------------------------------------
# route_id
# route_short_name
# route_long_name
# route_desc
# route_type
# route_color
# route_text_color
# route_url
#-----------------------------------------------------------------------------
from CSVRowModel import CSVRowModel

class RouteModel(CSVRowModel):

	headerNames = "route_id,route_short_name,route_long_name,route_desc,route_type,route_color,route_text_color,route_url"

	#-----------------------------------------------------------------------------
	def __init__(self):
		super(RouteModel, self).__init__(RouteModel.headerNames)

		self._matchingTrips = []
		self._matchingStopTimes = []
		self._matchingShapeIds = {}
		self._matchingShapes = []
		self._matchingStopIds = {}
		self._matchingStops = []

	#-----------------------------------------------------------------------------
	# with route_id:
	# 	(1) find all matching trips
	#
	# with trip_ids (from matching trips):
	#	(2) find all matching shapes
	#	(3) find all matching stop_times
	#
	# with stop_ids (from matching stop_times):
	#	(4) find all matching stops
	#-----------------------------------------------------------------------------
	def filter(self, allTrips, allStopTimes, allStops, allShapes):
		self._allTrips = allTrips
		self._allStopTimes = allStopTimes
		self._allStops = allStops
		self._allShapes = allShapes

		for trip in self._allTrips:
			if trip.getProperty("route_id") == self.getProperty("route_id"):
				self._matchingTrips.append(trip)

		for trip in self._matchingTrips:
			shape_id = trip.getProperty("shape_id")
			trip_id = trip.getProperty("trip_id")

			for shape in self._allShapes:
				shape_id_index = shape.getProperty("shape_id") + shape.getProperty("shape_pt_sequence")
				if shape.getProperty("shape_id") == shape_id and (shape_id_index not in self._matchingShapeIds):
					self._matchingShapes.append(shape)
					self._matchingShapeIds[shape_id_index] = shape

			for stopTime in self._allStopTimes:
				if stopTime.getProperty("trip_id") == trip_id:
					self._matchingStopTimes.append(stopTime)


		for stopTime in self._matchingStopTimes:
			self._matchingStopIds[stopTime.getProperty("stop_id")] = 1

		for stopId in self._matchingStopIds:
			for stop in self._allStops:
				if stop.getProperty("stop_id") == stopId:
					self._matchingStops.append(stop)


	#-----------------------------------------------------------------------------
	def getMatchingTrips(self):
		return self._matchingTrips

	#-----------------------------------------------------------------------------
	def getMatchingShapes(self):
		return self._matchingShapes

	#-----------------------------------------------------------------------------
	def getMatchingStopTimes(self):
		return self._matchingStopTimes

	#-----------------------------------------------------------------------------
	def getMatchingStopIds(self):
		return self._matchingStopIds

	#-----------------------------------------------------------------------------
	def getMatchingStops(self):
		return self._matchingStops

