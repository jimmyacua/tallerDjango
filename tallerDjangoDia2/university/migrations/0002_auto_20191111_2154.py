# Generated by Django 2.2.7 on 2019-11-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-title']},
        ),
        migrations.AddIndex(
            model_name='departament',
            index=models.Index(fields=['name', 'budget'], name='university__name_02a1ae_idx'),
        ),
    ]
