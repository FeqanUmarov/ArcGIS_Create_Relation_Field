"""
Bu script iki ferqli layda relationun qurulmasi ucun laylar arasinda elaqe qurulmasi mumkun olan stunlari yaradir. Meselen bir torpaq
poliqonu uzerinde 2 tikili varsa bu zaman, torpaq layinin OBJECTID sutunudaki melumati goturur ve hemin torpagin uzerindeki
tikilide yeni bir sutun acaraq OBJECTID-deki melumati tikiliye yazir. Meselen torpaqda OBJECTID=1-ise ve onun uzerinde 2 tikili varsa bu zaman
hemin tikililerin her ikisinin atributuna 1 yazilir.


"""




import arcpy

############# Inputs ###############################
def inputs():
    feature_one = arcpy.GetParameterAsText(0)
    feature_two = arcpy.arcpy.GetParameterAsText(1)
    
    RunProcess(feature_one,feature_two)
def RunProcess(feature_one,feature_two):
    AddField(feature_two)
    CreateRelation(feature_one,feature_two)
############# Inputs ###############################
def AddField(feature_two):


############# Add Relation Field ###############################
    arcpy.AddField_management(feature_two,"relation","LONG")
############# Add Relation Field ###############################


    
   
def CreateRelation(feature_one,feature_two):
    rows = arcpy.SearchCursor(feature_one)
    for row in rows:
        value = row.getValue("OBJECTID")
        arcpy.SelectLayerByAttribute_management(feature_one,"NEW_SELECTION","OBJECTID={}".format(value))
        arcpy.SelectLayerByLocation_management(feature_two,"WITHIN",feature_one,"","NEW_SELECTION")
        arcpy.CalculateField_management(feature_two,"relation",value)


inputs()
