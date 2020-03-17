# ArcPy サイト パッケージをインポートします。 
import arcpy
# マップ ドキュメントのオブジェクト取得
mxd = arcpy.mapping.MapDocument("current")
# データ フレームのオブジェクト取得
dfs = arcpy.mapping.ListDataFrames(mxd)
# レイヤーのオブジェクト取得
lyrs = arcpy.mapping.ListLayers(mxd,"",dfs[0])

for lyr in lyrs:
     # レイヤーの表示設定
     lyr.visible = True
     # レイヤーのシンボル更新
     if lyr.name == "current":
         sourceLayer = arcpy.mapping.Layer(r"C:\data\current_symbol.lyr")
         arcpy.mapping.UpdateLayer(dfs[0], lyr, sourceLayer, True)
     # エクステント使ってズーム
     if lyr.name == "tokyo" :
        dfs[0].extent = lyr.getExtent()
