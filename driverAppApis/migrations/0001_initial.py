# Generated by Django 4.0.2 on 2022-07-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('name', models.CharField(max_length=15)),
                ('customer_id', models.IntegerField()),
                ('mobile_no', models.IntegerField()),
                ('qrcode_img', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
