"""Step through MXD documents. Replace old sde references with new environment sde connection.
Does not revise anything but sde connection paths."""

import os
import arcpy

new_sde_workspace_path = r"Database Connections\Production as sde on gis-ags-imap01p.mdgov.maryland.gov.sde"
# Check to see if the new sde workspace path is valid. Yep, it works
# arcpy.env.workspace = new_sde_workspace_path
# myls = arcpy.ListDatasets()
# print(myls)

# Was originally to cull Cached and Image Services but did not go that path.
# cached_or_imageservice_names = [u'MD_ThreeInchImagery', u'MD_CanopyHeight', u'MD_ColorBasemap', u'MD_ParcelBoundaries',
#                                 u'MD_PropertyData',
#                                 u'MD_BlackAndWhiteBasemap', u'MD_NAIPImagery', u'MD_BroadbandProviderPerCensusBlock',
#                                 u'MD_SeaLevelRiseWetlandAdaptationAreas', u'MD_StormSurge', u'MD_SixInchImagery',
#                                 u'MD_CanopyCover', u'MD_Biomass',
#                                 u'MD_SSURGOSoils', u'MD_HighResolutionLandCover', u'MD_Floodplain', u'MD_USGSTopoQuads',
#                                 u'MD_LandUseLandCover']

# Brought down MXD's from server and processed them locally for speed and editing ease
for dir, dirname, files in os.walk("MXD"):
    #skip empty directories
    if len(files) == 0:
        continue

    # Only process .mxd documents
    for fileName in files:
        fullPath = os.path.join(dir, fileName)
        if os.path.isfile(fullPath):
            basename, extension = os.path.splitext(fullPath)
            if extension == ".mxd":
                mxd = arcpy.mapping.MapDocument(fullPath)
                set_of_workspace_paths = set()
                mxd_layer_list = arcpy.mapping.ListLayers(mxd)

                print("\n{}".format(basename))

                # Multiple sde connection paths can exist in each mxd. The process first inventories the paths that
                #   are present in the MXD and then runs the replace process on each one in this set. Couldn't apply
                #   a single replace because multiple paths can be present in one mxd
                for layer in mxd_layer_list:
                    set_of_workspace_paths.add(layer.workspacePath)

                print(set_of_workspace_paths)

                for path in set_of_workspace_paths:
                    print(path)
                    # Sometimes the process would fail. In reporcessing mxd's, skip over those that have already been fixed by me.
                    if path == r"C:\Users\cschaefer\AppData\Roaming\Esri\Desktop10.5\ArcCatalog\Production as sde on gis-ags-imap01p.mdgov.maryland.gov.sde":
                        continue
                    try:
                        # only process sde connections, not gdb etc
                        if ".sde" in path:
                            mxd.replaceWorkspaces(old_workspace_path=path,old_workspace_type="SDE_WORKSPACE", new_workspace_path=new_sde_workspace_path, new_workspace_type="SDE_WORKSPACE", validate=True)
                        else:
                            continue
                    except Exception as e:
                        # Occasionally an "Unexpected Error" occurs and the try and except fails to keep the process moving
                        print("Exception: {}".format(e))
                        print("GP Error: {}".format(arcpy.GetMessage(0)))
                        continue

                mxd.save()
                del mxd
