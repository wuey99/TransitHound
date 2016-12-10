#-----------------------------------------------------------------------------
import csv

#-----------------------------------------------------------------------------
from CSVModel import CSVModel
from RouteModel import RouteModel
from TripModel import TripModel
from StopTimeModel import StopTimeModel
from StopModel import StopModel
from ShapeModel import ShapeModel

import os, sys, shutil

#-----------------------------------------------------------------------------
def lookUpRoute(allRoutes, route_id):
	for route in allRoutes:
		if route.getProperty("route_id") == route_id:
			return route

	return none

#-----------------------------------------------------------------------------
class CSVImporter(object):

	def __init__(self, list, classType, csvFile):
		f = open(os.path.join(srcPath, csvFile), "rb")

		reader = csv.reader(f, delimiter=",")

		for row in reader:
			csvModel = classType()

			csvModel.addColumns(row)

			list.append(csvModel)

		f.close()

#-----------------------------------------------------------------------------
class GTFSRouteExporter(object):

	def __init__(self, routeModel, allTrips, allStopTimes, allStops, allShapes):
		routePath = os.path.join(dstPath, routeModel.getProperty("route_id"))

		try:
			os.mkdir(routePath)

			shutil.copyfile(os.path.join(srcPath, "agency.txt"), os.path.join(routePath, "agency.txt"))
			shutil.copyfile(os.path.join(srcPath, "calendar.txt"), os.path.join(routePath, "calendar.txt"))
			shutil.copyfile(os.path.join(srcPath, "calendar_dates.txt"), os.path.join(routePath, "calendar_dates.txt"))
		except Exception, e:
			print ": exception: ", e

		f = open(os.path.join(routePath, "routes.txt"), "wb")
		routeModel.writeHeader(f)
                routeModel.writeRow(f)
		f.close()

		self.outputCSV(routePath, routeModel.getMatchingShapes(), "shapes.txt")
		self.outputCSV(routePath, routeModel.getMatchingTrips(), "trips.txt")
		self.outputCSV(routePath, routeModel.getMatchingStops(), "stops.txt")
		self.outputCSV(routePath, routeModel.getMatchingStopTimes(), "stop_times.txt")

	def outputCSV(self, routePath, csvModelsList, csvFileName):
		f = open(os.path.join(routePath, csvFileName), "wb")
		i = 0
		for row in csvModelsList:
			if i == 0:
				row.writeHeader(f)
				i = 1
			row.writeRow(f)
		f.close()


#-----------------------------------------------------------------------------
class GTFSRouteSplitter(object):

	def __init__(self):
		self._allRoutes = []
		self._allTrips = []
		self._allStopTimes = []
		self._allStops = []
		self._allShapes = []

		try:
			shutil.rmtree(dstPath)
		except Exception:
			pass

		try:
			os.mkdir(dstPath)
		except Exception:
			pass

		CSVImporter(self._allRoutes, RouteModel, "routes.txt")
		CSVImporter(self._allTrips, TripModel, "trips.txt")
		CSVImporter(self._allStops, StopModel, "stops.txt")
		CSVImporter(self._allShapes, ShapeModel, "shapes.txt")
		CSVImporter(self._allStopTimes, StopTimeModel, "stop_times.txt")

		print ": routes: ", len(self._allRoutes)
		print ": trips: ", len(self._allTrips)
		print ": stops: ", len(self._allStops)
		print ": shapes: ", len(self._allShapes)
		print ": stop_times: ", len(self._allStopTimes)

		route209 = lookUpRoute(self._allRoutes, "209-13092")
		route209.filter(self._allTrips, self._allStopTimes, self._allStops, self._allShapes)

		print ": trips on 209: ", len(route209.getMatchingTrips())
		print ": shapes on 209: ", len(route209.getMatchingShapes())
		print ": stop_times on 209: ", len(route209.getMatchingStopTimes())
		print ": stop ids on 209: ", len(route209.getMatchingStopIds())
		print ": stops on 209: ", len(route209.getMatchingStops())

		GTFSRouteExporter(route209, self._allTrips, self._allStopTimes, self._allStops, self._allShapes)


#-----------------------------------------------------------------------------
if len(sys.argv) < 3:
	print "usage: python GTFSRouteSplitter.py <path to GTFS files> <output directory>"

	exit(0)


srcPath = os.path.join(os.getcwd(), sys.argv[1])
dstPath = os.path.join(os.getcwd(), sys.argv[2])

print ": src: ", srcPath
print ": dst: ", dstPath

GTFSRouteSplitter()

