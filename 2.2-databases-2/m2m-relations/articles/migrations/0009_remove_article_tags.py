# Generated by Django 4.2.3 on 2023-08-14 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_scope_delete_scopes_alter_article_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
    ]