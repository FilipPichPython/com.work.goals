# Generated by Django 2.1.1 on 2018-09-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180918_0837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='movie2',
            new_name='filmy',
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.IntegerField(choices=[(1, 'Horror'), (0, 'Nieznany'), (2, 'Komedia'), (4, 'Dramat'), (3, 'Sci-Fi')], default=0),
        ),
    ]
