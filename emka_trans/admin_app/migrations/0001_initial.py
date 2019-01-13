# Generated by Django 2.0.9 on 2018-12-13 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id_route', models.IntegerField(primary_key=True, serialize=False)),
                ('products_list', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('client', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id_truck', models.IntegerField(primary_key=True, serialize=False)),
                ('capacity', models.IntegerField()),
                ('return_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='id_truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='truck', to='admin_app.Truck'),
        ),
    ]
