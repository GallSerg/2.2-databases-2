# Generated by Django 4.2.3 on 2023-08-13 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_article_scopes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main', 'tag'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]