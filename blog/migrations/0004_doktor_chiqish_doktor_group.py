# Generated by Django 4.2.4 on 2024-07-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_doktor_staj'),
    ]

    operations = [
        migrations.AddField(
            model_name='doktor',
            name='chiqish',
            field=models.BooleanField(default=True, verbose_name='Ekranga chiqsinmi?'),
        ),
        migrations.AddField(
            model_name='doktor',
            name='group',
            field=models.CharField(choices=[('psixolog', 'psixolog'), ('xirurg', 'xirurg'), ('kardiolog', 'kardiolog')], default='psixolog', max_length=100),
        ),
    ]
