# Read a json file containing information on iMAP services. Detect Cached and ImageServer services.
#   Those types were ggoing to be skipped by the UpdateFix_BrokenDataSources.py script but that was abandoned.

# RESULTS for ImageServer or Cached 20180417 CJS: Based on json file provided by Matt on day before
# results = [u'MD_ThreeInchImagery', u'MD_CanopyHeight', u'MD_ColorBasemap', u'MD_ParcelBoundaries', u'MD_PropertyData',
#            u'MD_BlackAndWhiteBasemap', u'MD_NAIPImagery', u'MD_BroadbandProviderPerCensusBlock',
#            u'MD_SeaLevelRiseWetlandAdaptationAreas', u'MD_StormSurge', u'MD_SixInchImagery', u'MD_CanopyCover',
#            u'MD_Biomass', u'MD_SSURGOSoils', u'MD_HighResolutionLandCover', u'MD_Floodplain', u'MD_USGSTopoQuads',
#            u'MD_LandUseLandCover']

import json
json_file = "GeodataServices.json"
with open(json_file, "r") as handler:
    contents = handler.read()
    loaded = json.loads(contents)

service_names_set = set()
for obj in loaded:
    if obj["Cached"] == "true" or obj["Type"] == "ImageServer":
        service_names_set.add(obj["ServiceName"])
# for name in service_names_set:
#     print(name)
print service_names_set
