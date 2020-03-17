import arcpy

# ArcGIS Online にサイン イン (自身のArcGIS Online のユーザー名、パスワードを入力)
arcpy.SignInToPortal("https://arcgis.com", "ユーザー名", "パスワード")

# プロジェクト ファイルのオブジェクト取得
aprx = arcpy.mp.ArcGISProject("CURRENT")

# マップとレイヤーを取得
map = aprx.listMaps()[0]
lyrs = map.listLayers()
# 作成するサービス定義ドラフトファイル、サービス定義ファイルのファイル名を設定
sddraft_output = r"C:\data\output\sample.sddraft"
sd_output = r"C:\data\output\sample.sd"

# サービス定義ドラフトの作成
sharing_draft = map.getWebLayerSharingDraft("HOSTING_SERVER","FEATURE","Sample",lyrs)
sharing_draft.exportToSDDraft(sddraft_output)

# サービス定義ファイルの作成（サービスのステージング ツールの使用）
arcpy.StageService_server(sddraft_output, sd_output)
# ArcGIS Online にアップロード（サービス定義のアップロード ツールの使用）
arcpy.UploadServiceDefinition_server(sd_output, "HOSTING_SERVER")
