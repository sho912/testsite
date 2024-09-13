# Generated by Django 5.0.4 on 2024-07-19 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='construction',
            name='slide_show1',
        ),
        migrations.RemoveField(
            model_name='construction',
            name='slide_show2',
        ),
        migrations.RemoveField(
            model_name='construction',
            name='slide_show3',
        ),
        migrations.RemoveField(
            model_name='construction',
            name='slide_show4',
        ),
        migrations.RemoveField(
            model_name='construction',
            name='slide_show5',
        ),
        migrations.AddField(
            model_name='construction',
            name='entrance_A',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='玄関After'),
        ),
        migrations.AddField(
            model_name='construction',
            name='entrance_B',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='玄関Before'),
        ),
        migrations.AddField(
            model_name='construction',
            name='etc_A',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='その他After'),
        ),
        migrations.AddField(
            model_name='construction',
            name='etc_B',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='その他Before'),
        ),
        migrations.AddField(
            model_name='construction',
            name='kitchen_A',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='キッチンAfter'),
        ),
        migrations.AddField(
            model_name='construction',
            name='kitchen_B',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='キッチンBefore'),
        ),
        migrations.AddField(
            model_name='construction',
            name='living_A',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='リビングAfter'),
        ),
        migrations.AddField(
            model_name='construction',
            name='living_B',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='リビングBefore'),
        ),
        migrations.AddField(
            model_name='construction',
            name='stairs_A',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='階段After'),
        ),
        migrations.AddField(
            model_name='construction',
            name='stairs_B',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='階段Before'),
        ),
        migrations.AddField(
            model_name='construction',
            name='toilet_A',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='トイレAfter'),
        ),
        migrations.AddField(
            model_name='construction',
            name='toilet_B',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='トイレBefore'),
        ),
    ]
