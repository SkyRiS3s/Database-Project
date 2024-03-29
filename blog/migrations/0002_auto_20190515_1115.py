# Generated by Django 2.2 on 2019-05-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancellation',
            fields=[
                ('policy_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cancellation_policy', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'cancellation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('country_code', models.CharField(blank=True, max_length=3, null=True)),
                ('country_id', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
