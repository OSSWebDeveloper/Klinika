# Generated by Django 4.2.4 on 2024-08-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_doktor_group_alter_xizmat_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='xizmat',
            name='staj',
            field=models.IntegerField(default=1, verbose_name='Doktor ish staji'),
        ),
        migrations.AlterField(
            model_name='doktor',
            name='group',
            field=models.CharField(choices=[('psixolog', 'psixolog'), ('xirurg', 'xirurg'), ('kardiolog', 'kardiolog')], default='psixolog', max_length=100),
        ),
        migrations.AlterField(
            model_name='xizmat',
            name='group',
            field=models.CharField(choices=[('reablitatsiya', 'reablitatsiya'), ('narkomaniya', 'narkomaniya'), ('kodirovaniya', 'kodirovaniya'), ('alkogolizm', 'alkogolizm')], default='alkogolizm', max_length=100),
        ),
        migrations.AlterField(
            model_name='xizmat',
            name='group_lang',
            field=models.CharField(choices=[('ru', 'ru'), ('uz', 'uz')], default='uz', max_length=100),
        ),
    ]
