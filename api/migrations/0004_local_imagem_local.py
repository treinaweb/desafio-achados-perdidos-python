# Generated by Django 3.2.7 on 2021-09-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210915_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='imagem_local',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
