#-----------------------------------------------------------------------------
# shape_id
# shape_pt_lat
# shape_pt_lon
# shape_pt_sequence
#-----------------------------------------------------------------------------
from CSVRowModel import CSVRowModel

class ShapeModel(CSVRowModel):

	headerNames = "shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence"

	#-----------------------------------------------------------------------------
	def __init__(self):
		super(ShapeModel, self).__init__(ShapeModel.headerNames)

