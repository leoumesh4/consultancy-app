# Generated by Django 3.1.6 on 2021-02-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210204_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('gallery_img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
