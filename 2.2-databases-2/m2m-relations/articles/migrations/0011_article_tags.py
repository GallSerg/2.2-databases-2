# Generated by Django 4.2.3 on 2023-08-14 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_scope_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.tag'),
        ),
    ]