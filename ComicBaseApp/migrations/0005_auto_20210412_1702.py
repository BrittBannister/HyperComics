# Generated by Django 3.1.7 on 2021-04-12 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComicBaseApp', '0004_auto_20210412_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicuser',
            name='favorites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='ComicBaseApp.comicbook'),
        ),
    ]
