# アプリ内からインポート
import datetime
# django内からインポート
from django import forms
from django.core.files.storage import default_storage

from .models import Article, BridgePicture, DamageComment, FullReportData, Image, Infra, Regulation, UploadedFile
from .models import Photo, Table, NameEntry, PartsNumber
from django.core.exceptions import ValidationError

# ファイルアップロード
class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

# << Infra毎にdxfファイルを登録 >>
class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['infra', 'dxf', 'article']

# << 各橋作成時のボタン選択肢 >>
class BridgeCreateForm(forms.ModelForm):
    class Meta:
        model = Infra
        fields = ['交通規制', '活荷重', '等級', '適用示方書', '近接方法', '第三者点検', '路下条件'] # 他のフィールドについても必要に応じて追加してください。
        widgets = {
            '交通規制': forms.CheckboxSelectMultiple,
            '活荷重': forms.RadioSelect,
            '等級': forms.RadioSelect,
            '適用示方書': forms.RadioSelect,
            '近接方法': forms.CheckboxSelectMultiple,
            '第三者点検': forms.RadioSelect,
            '路下条件': forms.CheckboxSelectMultiple,
        }
        
# << 各橋更新時のボタン選択肢 >>
class BridgeUpdateForm(forms.ModelForm):
    class Meta:
        model = Infra
        fields = ['交通規制', '活荷重', '等級', '適用示方書', '近接方法', '第三者点検', '路下条件'] # 他のフィールドについても必要に応じて追加してください。
        widgets = {
            '交通規制': forms.CheckboxSelectMultiple,
            '活荷重': forms.RadioSelect,
            '等級': forms.RadioSelect,
            '適用示方書': forms.RadioSelect,
            '近接方法': forms.CheckboxSelectMultiple,
            '第三者点検': forms.RadioSelect,
            '路下条件': forms.CheckboxSelectMultiple,
        }

# << センサス入力用 >>
class CensusForm(forms.Form):
    traffic = forms.CharField(label='交通量')
    mixing = forms.CharField(label='大型車混入率')
    
# << 名前とアルファベットの紐付け >>
class NameEntryForm(forms.ModelForm):
    class Meta:
        model = NameEntry
        fields = ['name', 'alphabet', 'article']

# NameEntryFormSet = modelformset_factory(NameEntry, form=NameEntryForm, extra=3)
#          Formセットを生成するための関数(modelクラス, Formクラス, 最初に表示する空のクラス数)

# << 要素番号の登録 >>
class PartsNumberForm(forms.ModelForm):
    class Meta:
        model = PartsNumber
        fields = ['parts_name', 'symbol', 'material', 'main_frame', 'span_number', 'number', 'infra', 'article']
        
    def clean(self):
        data = self.cleaned_data
        print(data)

        materials = data["material"]

        #タグは3個まで
        if len(materials) > 3:
            raise ValidationError("materialは3個まで")

        return self.cleaned_data

# 1回のリクエストで、必ず5個のデータを入力したいときに使う。必ず一定数のデータを入れたいときに使う。
# PartsNumberFormSet = modelformset_factory(PartsNumber, form=PartsNumberForm, extra=5)


# <<損傷写真表示>>
class NameForm(forms.Form):
    initial = forms.CharField(label='イニシャル')
    name = forms.CharField(label='名前')
    folder_path = forms.CharField(label='フォルダパス')
    

# 全景写真用
class UploadForm(forms.ModelForm): # UploadFormという名前のFormクラスを定義(Modelクラスと紐付け)
    photo = forms.ImageField() # modelに定義されているものを使用
    class Meta: # ModelFormと紐付ける場合に記載
        model = Image # models.pyのImageクラスと紐付け
        fields = ['photo'] # Image.modelのphotoフィールドのみを使用
        
class PhotoUploadForm(forms.ModelForm): # PhotoUploadFormという名前のFormクラスを定義(Modelクラスと紐付け)
    class Meta: # ModelFormと紐付ける場合に記載
        model = Photo # models.pyのPhotoクラスと紐付け
        fields = ['image'] # このFormで扱うフィールドを指定
        
# 損傷写真変更用(Ajax)
class FileUploadSampleForm(forms.Form):
    file = forms.ImageField()
    
    def save(self):
        """ファイルを保存するメソッド"""
        now_date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # ファイル名に現在時刻を付与するため取得
        upload_file = self.files['file']  # フォームからアップロードファイルを取得
        file_name = default_storage.save(now_date + "_" + upload_file.name, upload_file)  # ファイルを保存 戻り値は実際に保存したファイル名
        return default_storage.url(file_name)
    
# << 写真帳の全データを管理サイトに登録 >>
class FullReportDataForm(forms.ModelForm):
    class Meta:
        model = FullReportData
        fields = ['parts_name', 'damage_name', 'join', 'picture_number', 'this_time_picture', 'last_time_picture',
                  'textarea_content', 'damage_coordinate_x', 'damage_coordinate_y', 'picture_coordinate_x', 'picture_coordinate_y']

# << 損傷写真帳の入力データを登録 >>　update_full_report_data関数をビューに作成　update_full_report_dataパスをURLに作成
class FullReportDataEditForm(forms.ModelForm):
    class Meta:
        model = FullReportData
        fields = ["measurement", "damage_size", "classification", "pattern"]
        
# << 所見のコメントを登録 >>
class DamageCommentEditForm(forms.ModelForm):
    class Meta:
        model = DamageComment # モデルのクラス名
        fields = ["comment"] # モデルのフィールド名

# << 判定区分のボタンを登録 >>
class DamageCommentJadgementEditForm(forms.ModelForm):
    class Meta:
        model = DamageComment
        fields = ["jadgement"]
        
# << 損傷原因のボタンを登録 >>
class DamageCommentCauseEditForm(forms.ModelForm):
    class Meta:
        model = DamageComment
        fields = ["cause"]
        
# << 損傷写真帳の変更内容を保存 >>
class EditReportDataForm(forms.ModelForm):
    class Meta:
        model = FullReportData
        fields = ['parts_name', 'damage_name']

# << ファイルパスを選択し保存 >>
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['案件名', '土木事務所', '対象数', '担当者名', 'その他', 'ファイルパス']
        
class InfraForm(forms.ModelForm):
    class Meta:
        model = Infra
        fields = ['title', '径間数', '橋長', '全幅員', '路線名', 'latitude', 'longitude', 'end_latitude', 'end_longitude', '橋梁コード', '活荷重', '等級', '適用示方書', 
                  '上部構造形式', '下部構造形式', '基礎構造形式', '近接方法', '交通規制', '第三者点検', '海岸線との距離', '路下条件', 
                  '特記事項', 'カテゴリー', '交通量', '大型車混入率', 'article']
        
class BridgePictureForm(forms.ModelForm):
    class Meta:
        model = BridgePicture
        fields = ['image', 'picture_number', 'damage_name', 'parts_split', 'memo', 'damage_coordinate_x', 'damage_coordinate_y', 'picture_coordinate_x', 'picture_coordinate_y', 'span_number', 'table', 'infra', 'article']