# Generated by Django 4.0.5 on 2022-06-07 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.seller'),
        ),
    ]
