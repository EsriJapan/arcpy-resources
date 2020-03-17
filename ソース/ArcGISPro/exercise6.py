import arcpy

new_point_fc = r"C:\data\ArcGISPro\arcpy.gdb\newPoint"

# ポイントのジオメトリを作る
point = arcpy.Point(139.7560384, 35.6737209)
pointGeom = arcpy.PointGeometry(point)

# カーソル使って insert 
with arcpy.da.InsertCursor(new_point_fc, ['SHAPE@']) as iCur:
    iCur.insertRow(pointGeom)


new_line_fc = r"C:\data\ArcGISPro\arcpy.gdb\newLine"

# ポリラインのジオメトリを作る
point1 = arcpy.Point(139.7592245, 35.6750152)
point2 = arcpy.Point(139.7560384, 35.6710451)
point3 = arcpy.Point(139.7530154, 35.6721598)
point4 = arcpy.Point(139.7559762, 35.6764465)
array = arcpy.Array()
array.add(point1)
array.add(point2)
array.add(point3)
array.add(point4)
polyline = arcpy.Polyline(array)

# カーソル使って insert 
with arcpy.da.InsertCursor(new_line_fc, ['SHAPE@']) as iCur:
    iCur.insertRow([polyline])


