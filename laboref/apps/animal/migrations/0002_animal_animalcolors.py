# Generated by Django 2.2.7 on 2019-11-30 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=255)),
                ('animal_age', models.IntegerField()),
                ('animal_breed', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animal.Breed')),
                ('animal_color', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='animal.AnimalColors')),
            ],
        ),
    ]
