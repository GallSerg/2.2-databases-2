# Generated by Django 4.2.3 on 2023-08-14 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_scope_scopes_remove_article_scopes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scopes', to='articles.tag'),
        ),
    ]
