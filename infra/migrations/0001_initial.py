# Generated by Django 4.2.7 on 2024-08-08 09:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Approach",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "近接方法",
                    models.CharField(
                        choices=[
                            ("地上", "地上"),
                            ("梯子", "梯子"),
                            ("橋梁点検車", "橋梁点検車"),
                            ("高所作業車", "高所作業車"),
                            ("軌陸車", "軌陸車"),
                            ("ボート", "ボート"),
                            ("ロープアクセス", "ロープアクセス"),
                            ("ドローン", "ドローン"),
                            ("ファイバースコープ", "ファイバースコープ"),
                            ("画像解析", "画像解析"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("案件名", models.CharField(max_length=100)),
                ("土木事務所", models.CharField(max_length=100)),
                ("対象数", models.IntegerField()),
                ("担当者名", models.CharField(max_length=100)),
                ("その他", models.CharField(max_length=100)),
                (
                    "カテゴリー",
                    models.CharField(
                        choices=[
                            ("bridge", "橋梁"),
                            ("pedestrian", "歩道橋"),
                            ("other", "その他"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Damage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DamageReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first", models.CharField(max_length=100)),
                ("second", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo", models.ImageField(upload_to="photos/")),
            ],
        ),
        migrations.CreateModel(
            name="Infra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("径間数", models.IntegerField()),
                ("橋長", models.DecimalField(decimal_places=2, max_digits=10)),
                ("全幅員", models.DecimalField(decimal_places=2, max_digits=10)),
                ("路線名", models.CharField(max_length=50)),
                ("latitude", models.CharField(blank=True, max_length=50)),
                ("longitude", models.CharField(blank=True, max_length=50)),
                ("橋梁コード", models.CharField(blank=True, max_length=50)),
                ("上部構造形式", models.CharField(max_length=100)),
                ("下部構造形式", models.CharField(max_length=100)),
                ("基礎構造形式", models.CharField(max_length=100)),
                ("海岸線との距離", models.CharField(max_length=100)),
                ("特記事項", models.CharField(blank=True, max_length=100)),
                (
                    "カテゴリー",
                    models.CharField(
                        choices=[
                            ("bridge", "橋梁"),
                            ("pedestrian", "歩道橋"),
                            ("other", "その他"),
                        ],
                        max_length=100,
                    ),
                ),
                ("交通量", models.CharField(blank=True, max_length=10)),
                ("大型車混入率", models.CharField(blank=True, max_length=10)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="infra.article"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LoadGrade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "等級",
                    models.CharField(
                        choices=[
                            ("不明", "不明"),
                            ("一等橋", "一等橋"),
                            ("二等橋", "二等橋"),
                            ("三等橋", "三等橋"),
                            ("その他", "その他"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LoadWeight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "活荷重",
                    models.CharField(
                        choices=[
                            ("不明", "不明"),
                            ("A活荷重", "A活荷重"),
                            ("B活荷重", "B活荷重"),
                            ("TL-20", "TL-20"),
                            ("TL-14", "TL-14"),
                            ("TL-6", "TL-6"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("材料", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Panorama",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="panorama/")),
                ("checked", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="PartsName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("部材名", models.CharField(max_length=255)),
                ("記号", models.CharField(max_length=50)),
                ("主要部材", models.BooleanField()),
                ("material", models.ManyToManyField(to="infra.material")),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="photos/")),
            ],
        ),
        migrations.CreateModel(
            name="Regulation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "交通規制",
                    models.CharField(
                        choices=[
                            ("無し", "無し"),
                            ("片側交互通行", "片側交互通行"),
                            ("車線減少", "車線減少"),
                            ("歩道規制", "歩道規制"),
                            ("通行止め", "通行止め"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rulebook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "適用示方書",
                    models.CharField(
                        choices=[
                            ("不明", "不明"),
                            ("平成29年 道路橋示方書", "平成29年 道路橋示方書"),
                            ("平成24年 道路橋示方書", "平成24年 道路橋示方書"),
                            ("平成14年 道路橋示方書", "平成14年 道路橋示方書"),
                            ("平成8年 道路橋示方書", "平成8年 道路橋示方書"),
                            ("平成5年 道路橋示方書", "平成5年 道路橋示方書"),
                            ("平成2年 道路橋示方書", "平成2年 道路橋示方書"),
                            ("昭和55年 道路橋示方書", "昭和55年 道路橋示方書"),
                            ("昭和53年 道路橋示方書", "昭和53年 道路橋示方書"),
                            ("昭和47年 道路橋示方書", "昭和47年 道路橋示方書"),
                            ("昭和43年 プレストレスコンクリート道路橋示方書", "昭和43年 プレストレスコンクリート道路橋示方書"),
                            ("昭和39年 鉄筋コンクリート道路橋示方書", "昭和39年 鉄筋コンクリート道路橋示方書"),
                            ("昭和31年 鋼道路橋設計示方書", "昭和31年 鋼道路橋設計示方書"),
                            ("昭和15年 鋼道路橋設計示方書案", "昭和15年 鋼道路橋設計示方書案"),
                            ("大正15年 道路構造に関する細則案", "大正15年 道路構造に関する細則案"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Thirdparty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "第三者点検",
                    models.CharField(
                        choices=[("有り", "有り"), ("無し", "無し")], max_length=50
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UnderCondition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "路下条件",
                    models.CharField(
                        choices=[
                            ("河川", "河川"),
                            ("水路", "水路"),
                            ("湖沼", "湖沼"),
                            ("海洋", "海洋"),
                            ("道路", "道路"),
                            ("鉄道", "鉄道"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UploadedFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="uploads/")),
            ],
        ),
        migrations.CreateModel(
            name="Uploads",
            fields=[
                ("primary_key", models.AutoField(primary_key=True, serialize=False)),
                ("file", models.FileField(upload_to="uploads/")),
            ],
        ),
        migrations.CreateModel(
            name="Table",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dxf",
                    models.FileField(
                        upload_to="infra/table/dxf/", verbose_name="dxfファイル"
                    ),
                ),
                (
                    "infra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="infra.infra",
                        verbose_name="橋梁名",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PartsNumber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="(^\\d{4}$)|(^\\d{4}~\\d{4}$)"
                            )
                        ],
                    ),
                ),
                ("symbol", models.CharField(max_length=100)),
                ("main_frame", models.BooleanField()),
                ("span_number", models.CharField(max_length=50)),
                (
                    "infra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="infra.infra",
                        verbose_name="Infra",
                    ),
                ),
                ("material", models.ManyToManyField(to="infra.material")),
                (
                    "parts_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="infra.partsname",
                        verbose_name="部材名",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NameEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "alphabet",
                    models.CharField(
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(regex="[A-Za-z]+")
                        ],
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="infra.article",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="infra",
            name="交通規制",
            field=models.ManyToManyField(to="infra.regulation"),
        ),
        migrations.AddField(
            model_name="infra",
            name="活荷重",
            field=models.ManyToManyField(to="infra.loadweight"),
        ),
        migrations.AddField(
            model_name="infra",
            name="第三者点検",
            field=models.ManyToManyField(to="infra.thirdparty"),
        ),
        migrations.AddField(
            model_name="infra",
            name="等級",
            field=models.ManyToManyField(to="infra.loadgrade"),
        ),
        migrations.AddField(
            model_name="infra",
            name="路下条件",
            field=models.ManyToManyField(to="infra.undercondition"),
        ),
        migrations.AddField(
            model_name="infra",
            name="近接方法",
            field=models.ManyToManyField(to="infra.approach"),
        ),
        migrations.AddField(
            model_name="infra",
            name="適用示方書",
            field=models.ManyToManyField(to="infra.rulebook"),
        ),
        migrations.CreateModel(
            name="FullReportData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("parts_name", models.CharField(max_length=255)),
                ("damage_name", models.CharField(max_length=255)),
                ("parts_split", models.CharField(max_length=255)),
                ("join", models.CharField(max_length=255)),
                (
                    "picture_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "this_time_picture",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "last_time_picture",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("textarea_content", models.CharField(max_length=255)),
                ("damage_coordinate_x", models.CharField(max_length=255)),
                ("damage_coordinate_y", models.CharField(max_length=255)),
                (
                    "picture_coordinate_x",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "picture_coordinate_y",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("span_number", models.CharField(max_length=255)),
                ("special_links", models.CharField(max_length=255)),
                (
                    "measurement",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "damage_size",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "classification",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("pattern", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "infra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="infra.infra",
                        verbose_name="Infra",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DamageList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("parts_name", models.CharField(max_length=255)),
                ("symbol", models.CharField(max_length=255)),
                ("number", models.CharField(max_length=255)),
                ("material", models.CharField(max_length=255)),
                ("main_parts", models.CharField(max_length=255)),
                ("damage_name", models.CharField(max_length=255)),
                (
                    "damage_lank",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "classification",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("pattern", models.CharField(blank=True, max_length=255, null=True)),
                ("span_number", models.CharField(max_length=255)),
                (
                    "infra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="infra.infra",
                        verbose_name="Infra",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DamageComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("parts_name", models.CharField(max_length=255)),
                ("comment_parts_name", models.CharField(max_length=255)),
                ("replace_name", models.CharField(max_length=255)),
                (
                    "parts_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("main_parts", models.CharField(max_length=255)),
                ("material", models.CharField(max_length=255)),
                ("damage_name", models.CharField(max_length=255)),
                ("number", models.IntegerField(blank=True, null=True)),
                (
                    "damage_max_lank",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "damage_min_lank",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "this_time_picture",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("jadgement", models.CharField(blank=True, max_length=255, null=True)),
                ("cause", models.CharField(blank=True, max_length=255, null=True)),
                ("comment", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "auto_comment",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("span_number", models.CharField(max_length=255)),
                (
                    "infra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="infra.infra",
                        verbose_name="Infra",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="fullreportdata",
            constraint=models.UniqueConstraint(
                fields=(
                    "parts_name",
                    "damage_name",
                    "parts_split",
                    "join",
                    "damage_coordinate_x",
                    "damage_coordinate_y",
                    "span_number",
                    "special_links",
                ),
                name="unique_parts_damage",
            ),
        ),
        migrations.AddConstraint(
            model_name="damagelist",
            constraint=models.UniqueConstraint(
                fields=(
                    "parts_name",
                    "symbol",
                    "number",
                    "material",
                    "main_parts",
                    "damage_name",
                    "span_number",
                    "infra",
                ),
                name="unique_damage_list",
            ),
        ),
        migrations.AddConstraint(
            model_name="damagecomment",
            constraint=models.UniqueConstraint(
                fields=(
                    "parts_name",
                    "main_parts",
                    "damage_name",
                    "span_number",
                    "infra",
                ),
                name="unique_damage_comment",
            ),
        ),
    ]
