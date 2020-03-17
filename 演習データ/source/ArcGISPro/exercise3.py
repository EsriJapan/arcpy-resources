# ArcPy サイト パッケージをインポートします。 
import arcpy

# ジオプロセシング ツールで利用する変数を定義
csv_table = r"C:\data\HandsOn.csv"
x_field = "X"
y_field = "Y"
event_layer = "point_layer"
out_path = r"C:\data\ArcGISPro\arcpy.gdb"

# CSV ファイルから XY イベント レイヤー （ テンポラリ のオブジェクト ） を作成します。
arcpy.MakeXYEventLayer_management(csv_table, x_field, y_field, event_layer)

# XY イベント レイヤー を フィーチャ クラス として保存します。
arcpy.FeatureClassToFeatureClass_conversion(event_layer, out_path, "csv001")

# XY イベント レイヤー を削除します。
arcpy.Delete_management(event_layer)

