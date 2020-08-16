# Generated by Django 3.0.6 on 2020-06-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200613_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.CharField(default='https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png', max_length=300),
        ),
        migrations.AlterField(
            model_name='book',
            name='sites',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
