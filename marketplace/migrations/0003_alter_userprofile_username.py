# Generated by Django 4.0.4 on 2022-06-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_userprofile_alter_product_creator_delete_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
