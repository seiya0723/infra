from django.urls import path
from .import views
from .views import file_upload, file_upload_success, get_subdirectories, get_symbol, serve_image
from .views import photo_list, selected_photos, panorama_list
from django.conf import settings
from django.conf.urls.static import static

# urlパスの設定は何を意味しているのか、ぱっと見でわかるように作成する
# 例：article/<int:article_pk>/infra/<int:pk>/update/（article〇番のinfra△番の更新ページ）
#                   ↑ article の id       ↑ infra の id
handler500 = views.my_customized_server_error

urlpatterns = [
    # << 初期ページ >>
    path('', views.index_view, name='index'),
    # << 橋梁関係 >>
    path('article/<int:article_pk>/infra/', views.ListInfraView.as_view(), name='list-infra'),# 対象橋梁の一覧
    path('article/<int:article_pk>/infra/create/', views.CreateInfraView.as_view(), name='create-infra'),# 橋梁データの登録
    path('article/<int:article_pk>/infra/<int:pk>/detail/', views.DetailInfraView.as_view(), name='detail-infra'),# 橋梁データの一覧
    path('article/<int:article_pk>/infra/<int:pk>/delete/', views.DeleteInfraView.as_view(), name='delete-infra'),# 橋梁データの削除
    path('article/<int:article_pk>/infra/<int:pk>/update/', views.UpdateInfraView.as_view(), name='update-infra'),# 橋梁データの更新
    # << 案件関係 >>
    path('article/', views.ListArticleView.as_view(), name='list-article'),# 案件の一覧
    path('article/create/', views.CreateArticleView.as_view(), name='create-article'),# 案件の登録
    path('get-subdirectories/', get_subdirectories, name='get-subdirectories'),
    path('article/<int:pk>/detail/', views.DetailArticleView.as_view(), name='detail-article'),# 案件のデータ内容
    path('article/<int:pk>/delete/', views.DeleteArticleView.as_view(), name='delete-article'),# 案件の削除
    path('article/<int:pk>/update/', views.UpdateArticleView.as_view(), name='update-article'),# 案件の更新
    # << インプット・アウトプット >>
    path('article/<int:article_pk>/infra/<int:pk>/upload/', views.file_upload, name='file-upload'),# ファイルアップロード
    path('upload/success/', views.file_upload_success, name='file_upload_success'),# アップロード成功時
    path('article/<int:article_pk>/infra/<int:pk>/excel_output/', views.excel_output, name='excel-output'),# Excelファイル出力
    path('article/<int:article_pk>/infra/<int:pk>/dxf_output/', views.dxf_output, name='dxf-output'),# DXFファイル出力
    # << 損傷写真帳 >>
    path('article/<int:article_pk>/infra/<int:pk>/bridge-table/', views.bridge_table, name='bridge-table'),# 損傷写真帳
    path('bridge_table_edit/<int:damage_pk>/<int:table_pk>/', views.edit_report_data, name='edit_report_data'), # 旗揚げ内容の受信
    path('bridge_table_send/<int:damage_pk>/<int:table_pk>/', views.edit_send_data, name='edit_send_data'), # 旗揚げ内容の修正を送信
    path('update_picture_number/', views.edit_picture_number, name='edit_picture_number'), # 写真番号の保存

    # << 名前の登録 >>
    path('article/<int:article_pk>/names/', views.names_list, name='names-list'),# 名前とアルファベットの紐付け
    path('delete_name_entry/<int:entry_id>/', views.delete_name_entry, name='delete_name_entry'),# 登録した名前を削除
    # << 要素番号の登録 >>
    path('article/<int:article_pk>/infra/<int:pk>/number/', views.number_list, name='number-list'),# 要素番号登録
    path('delete_number/<int:article_pk>/infra/<int:pk>/number/<uuid:unique_id>/', views.delete_number, name='delete_number'),# 登録した番号を削除
    # << 所見一覧 >>
    path('article/<int:article_pk>/infra/<int:pk>/observations/', views.observations_list, name='observations-list'),# 所見一覧
    path('damage_comment_edit/<int:pk>/', views.damage_comment_edit , name="damage_comment_edit"), # 所見コメントを管理サイトに保存
    path('damage_comment_jadgement_edit/<int:pk>/', views.damage_comment_jadgement_edit , name="damage_comment_jadgement_edit"), # 対策区分を管理サイトに保存
    path('damage_comment_cause_edit/<int:pk>/', views.damage_comment_cause_edit , name="damage_comment_cause_edit"), # 損傷原因を管理サイトに保存
    # << Ajax >>
    path('ajax-file-send/<int:pk>/', views.ajax_file_send, name='ajax_file_send'),# 損傷写真帳の写真変更
    path('ajax-get-symbol/', views.get_symbol, name='ajax_get_symbol'),# 部材名と部材記号の紐付け
    path('save_comment/<int:pk>/', views.save_comment, name='save_comment'), # 所見コメントのリアルタイム保存
    path('update_full_report_data/<int:pk>/', views.update_full_report_data, name='update_full_report_data'), # 損傷写真帳のリアルタイム保存
    
    # << 未完成 >>
    # path('photos/', views.photo_list, name='photo_list'),
    # path('photos/upload/', views.photo_upload, name='photo_upload'),
    # path('photos/selected/', views.selected_photos, name='selected_photos'),
    # path('panorama/list/', views.panorama_list, name='panorama_list'),
    # path('images/', views.image_list, name='image_list'),# 全景写真
    # path('photo/', views.display_photo, name='photo'),# 全景写真のアップロード
    # path('change-photo/', views.change_photo, name='change_photo'),# 全景写真の変更
    # path('serve-image/<str:file_path>/', serve_image, name='serve_image'), # 写真をアップロードせずに表示
    path('article/<int:article_pk>/infra/<int:pk>/bridge-table/upload/', views.upload_picture, name='upload-picture'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)