# Generated by Django 4.2.3 on 2023-08-14 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['-is_main', 'tag'],
            },
        ),
        migrations.DeleteModel(
            name='Scopes',
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.tag'),
        ),
    ]
