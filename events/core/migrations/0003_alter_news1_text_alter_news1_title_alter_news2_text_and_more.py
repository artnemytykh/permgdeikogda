# Generated by Django 5.0.2 on 2024-03-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_news1_news2_news3_delete_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news1',
            name='text',
            field=models.CharField(blank=True, max_length=65536, null=True),
        ),
        migrations.AlterField(
            model_name='news1',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='news2',
            name='text',
            field=models.CharField(blank=True, max_length=65536, null=True),
        ),
        migrations.AlterField(
            model_name='news2',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='news3',
            name='text',
            field=models.CharField(blank=True, max_length=65536, null=True),
        ),
        migrations.AlterField(
            model_name='news3',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]