import arcpy

# ワーク スペースを設定します。
arcpy.env.workspace = r"C:\data\ArcMap\arcpy.gdb"

# fcList 変数に ListFeatureClasses() 関数の取得結果を代入
fcList = arcpy.ListFeatureClasses()

# フィーチャ クラスの一覧を表示
for fc in fcList:
    # 変数の代入 （Describe オブジェクト） をします。
    fcDesc = arcpy.Describe(fc)

    # Describe オブジェクトからフィーチャ クラスのプロパティを表示します。
    print "Shape Type: " + fcDesc.shapetype
    print "Feature Type: " + fcDesc.featuretype
    print "Extent: " + str(fcDesc.extent)


