# Generated by Django 2.1.1 on 2018-09-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180918_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.IntegerField(choices=[(1, 'Horror'), (0, 'Nieznany'), (4, 'Dramat'), (2, 'Komedia'), (3, 'Sci-Fi')], default=0),
        ),
    ]
