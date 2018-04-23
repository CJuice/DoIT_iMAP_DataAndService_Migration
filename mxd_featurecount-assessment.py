# Taken from http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-mapping/listbrokendatasources.htm
# slightly tweaked

import arcpy, os
mxds_root_directory = "E:\DoIT_iMAP_DataAndService_Migration\MXD"
csv_path = r"E:\DoIT_iMAP_DataAndService_Migration\MXD\mxd_featurecount_stats.csv"
# path = r"D:\MXD\iMAP_3_copies"


def write_to_csv(csv_path, mxd_name=None, total=None):
    if os.path.exists(csv_path):
        with open(csv_path, "a") as handler:
            handler.write("{},{}\n".format(mxd_name, total))
    else:
        with open(csv_path, "w") as handler:
            handler.write("MXD,TOTAL\n".format(mxd_name, total))

write_to_csv(csv_path=csv_path)

for dir, dirnames, files in os.walk(mxds_root_directory):
    if len(files) == 0:
        continue
    print("\nDirectory: {}".format(dir))
    for file_name in files:
        full_path = os.path.join(dir, file_name)
        basename, extension = os.path.splitext(full_path)
        if extension == ".mxd":
            mxd = arcpy.mapping.MapDocument(full_path)
            print "MXD: " + file_name
            layers_list = arcpy.mapping.ListLayers(mxd)
            mxd_feature_count = 0
            for layer in layers_list:
                if layer.isFeatureLayer:
                    feature_count_for_layer = int(arcpy.GetCount_management(layer)[0])
                    print("\t{}: {}".format(layer.name, feature_count_for_layer))
                    mxd_feature_count += feature_count_for_layer
                else:
                    print("\t{}: N/A".format(layer.name))
            print("\t\tTotal: {}\n".format(mxd_feature_count))
            del layers_list
            del mxd
            write_to_csv(csv_path=csv_path, mxd_name=file_name, total=mxd_feature_count)
        else:
            print("not mxd file")