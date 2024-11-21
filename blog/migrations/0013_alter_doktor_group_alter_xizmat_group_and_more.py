# Generated by Django 4.2.4 on 2024-08-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_xizmat_staj_alter_doktor_group_alter_xizmat_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doktor',
            name='group',
            field=models.CharField(choices=[('xirurg', 'xirurg'), ('psixolog', 'psixolog'), ('kardiolog', 'kardiolog')], default='psixolog', max_length=100),
        ),
        migrations.AlterField(
            model_name='xizmat',
            name='group',
            field=models.CharField(choices=[('narkomaniya', 'narkomaniya'), ('kodirovaniya', 'kodirovaniya'), ('reablitatsiya', 'reablitatsiya'), ('alkogolizm', 'alkogolizm')], default='alkogolizm', max_length=100),
        ),
        migrations.AlterField(
            model_name='xizmat',
            name='group_lang',
            field=models.CharField(choices=[('uz', 'uz'), ('ru', 'ru')], default='uz', max_length=100),
        ),
    ]
