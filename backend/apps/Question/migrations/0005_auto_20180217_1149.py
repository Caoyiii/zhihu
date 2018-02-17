# Generated by Django 2.0.2 on 2018-02-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0004_auto_20180211_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('-vote',), 'verbose_name': '回答', 'verbose_name_plural': '回答'},
        ),
        migrations.AddField(
            model_name='answer',
            name='anonymous',
            field=models.BooleanField(default=False, verbose_name='是否匿名'),
        ),
        migrations.AddField(
            model_name='question',
            name='anonymous',
            field=models.BooleanField(default=False, verbose_name='是否匿名'),
        ),
    ]
