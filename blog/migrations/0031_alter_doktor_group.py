# Generated by Django 4.2.4 on 2024-11-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_small_category_bc_alter_doktor_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doktor',
            name='group',
            field=models.CharField(choices=[('travmatalogiya', 'travmatalogiya'), ('stamatologiya', 'stamatologiya'), ('okulistika', 'okulistika')], default='stamatologiya', max_length=100),
        ),
    ]