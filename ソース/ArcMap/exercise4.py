# ArcPy サイト パッケージをインポートします。 
import arcpy

# csv001 フィーチャ クラスに LONG 型の total フィールドを追加します。
arcpy.AddField_management("csv001", "total", "LONG")

# csv001 フィーチャ クラスから取得するフィールド名のリストを作成
fields = ['total', 'bicycle', 'scooters', 'motorcycle']

# フィーチャ クラス (csv001) に対してカーソルを取得
cursor = arcpy.da.UpdateCursor("csv001", fields)

# for xx in :で、カーソルを移動しながら値を更新
for row in cursor:
    row[0] = row[1] + row[2] + row[3] # bicycle（インデックス番号:1）～ motorcycle（インデックス番号:3）の合計値
    cursor.updateRow(row) # 合計値の値を適用

# オブジェクトを削除して参照を解放します。
del cursor, row

