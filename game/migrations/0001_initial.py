# Generated by Django 2.2.9 on 2020-01-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attacker', models.CharField(max_length=20)),
                ('atk', models.IntegerField()),
                ('defender', models.CharField(max_length=20)),
                ('dfs', models.IntegerField(null=True)),
                ('result', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('win', models.IntegerField(default=0)),
                ('lose', models.IntegerField(default=0)),
            ],
        ),
    ]
