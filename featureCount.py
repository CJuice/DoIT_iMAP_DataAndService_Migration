# Built by MSokol
# Passed to CJuice on 20180419

import arcpy, os

root_path = r"D:\LiveData"
text_file_output = r"D:\Scripts\FeatureCount\FeatureCounts.txt"

# List Geodatabases in root directory.
# Note: All gdb's are in root; No nested subdirectories at time of design
arcpy.env.workspace = root_path
gdb_list = arcpy.ListFiles("*.gdb")

# Loop through Geodatabase List
for gdb in gdb_list:
    arcpy.AddMessage("\nGDB: {}".format(gdb))

    # Set Workspace to Geodatabase
    gdb_path = os.path.join(root_path, gdb)
    arcpy.env.workspace = "{}".format(gdb_path)

    # List Feature Datasets in Geodatabase
    feature_datasets_list = arcpy.ListDatasets("*", "Feature")
    for feature_dataset in feature_datasets_list:
        new_path_fds = os.path.join(gdb_path, feature_dataset)
        arcpy.env.workspace = "{}".format(new_path_fds)
        featureClasses = arcpy.ListFeatureClasses()

        # Loop through Features Classes
        arcpy.AddMessage("\tFD: {}".format(arcpy.env.workspace))
        for feature_class in featureClasses:
            arcpy.AddMessage("\t\tFC: {}".format(feature_class))

            # Get Number of Features in Feature Class
            feature_count = arcpy.GetCount_management(feature_class)
            arcpy.AddMessage("\t\t\t{} features".format(feature_count))

            # Open output text file and create/write, or append (dne or exists) feature class name & feature count
            write_or_append = None
            if os.path.exists(text_file_output):
                write_or_append = "a"
            else:
                write_or_append = "w"

            with open(text_file_output, write_or_append) as output:
                output.write("{} -- {} = {}\n".format(feature_dataset, feature_class, feature_count))