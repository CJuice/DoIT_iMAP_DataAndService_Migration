# Taken from http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-mapping/listbrokendatasources.htm
# slightly tweaked

import arcpy, os
path = "MXD"
# path = r"D:\MXD\iMAP_3_copies"
for dir, dirnames, files in os.walk(path):
    if len(files) == 0:
        continue
    print("\nDirectory: {}".format(dir))
    for fileName in files:
        fullPath = os.path.join(dir, fileName)
        if os.path.isfile(fullPath):
            basename, extension = os.path.splitext(fullPath)
            if extension == ".mxd":
                mxd = arcpy.mapping.MapDocument(fullPath)
                print "MXD: " + fileName
                brknList = arcpy.mapping.ListBrokenDataSources(mxd)
                for brknItem in brknList:
                    print "\t" + brknItem.name
                del mxd
