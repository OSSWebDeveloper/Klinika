# Generated by Django 4.2.4 on 2024-08-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_category_alter_doktor_group_alter_xizmat_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doktor',
            name='group',
            field=models.CharField(choices=[('xirurg', 'xirurg'), ('kardiolog', 'kardiolog'), ('psixolog', 'psixolog')], default='psixolog', max_length=100),
        ),
        migrations.AlterField(
            model_name='xizmat',
            name='group',
            field=models.CharField(choices=[('reablitatsiya', 'reablitatsiya'), ('narkomaniya', 'narkomaniya'), ('alkogolizm', 'alkogolizm'), ('kodirovaniya', 'kodirovaniya')], default='alkogolizm', max_length=100),
        ),
        migrations.AlterField(
            model_name='xizmat',
            name='group_lang',
            field=models.CharField(choices=[('uz', 'uz'), ('ru', 'ru')], default='uz', max_length=100),
        ),
    ]
