# Generated by Django 4.0.4 on 2022-11-25 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_publication_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='photo',
            field=models.FileField(null=True, upload_to='images/website/pubs'),
        ),
    ]
