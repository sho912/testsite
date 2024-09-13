from django.db import models
from django.utils import timezone
from django_summernote.fields import SummernoteTextField
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail
from django.urls import reverse


#記事のタグ生成クラス あとで実装する
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


#お知らせ
class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    slug = models.SlugField() #英数字のみなので、あとでタイトルから日本語に自動変換機能をつける
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)
    body = SummernoteTextField(verbose_name='本文')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        #管理画面での表示名
        verbose_name = 'お知らせ'
        verbose_name_plural = 'お知らせ 一覧'

#補助金
class Subsidy(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)
    body = SummernoteTextField(verbose_name='本文')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        #管理画面での表示名
        verbose_name = '補助金'
        verbose_name_plural = '補助金 一覧'

#施工事例
class Construction(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    slug = models.SlugField()
    image = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)

    kitchen_B = models.ImageField(upload_to='images', verbose_name='キッチンBefore', null=True, blank=True)
    kitchen_A = models.ImageField(upload_to='images', verbose_name='キッチンAfter', null=True, blank=True)
    toilet_B = models.ImageField(upload_to='images', verbose_name='トイレBefore', null=True, blank=True)
    toilet_A = models.ImageField(upload_to='images', verbose_name='トイレAfter', null=True, blank=True)
    living_B = models.ImageField(upload_to='images', verbose_name='リビングBefore', null=True, blank=True)
    living_A = models.ImageField(upload_to='images', verbose_name='リビングAfter', null=True, blank=True)
    entrance_B = models.ImageField(upload_to='images', verbose_name='玄関Before', null=True, blank=True)
    entrance_A = models.ImageField(upload_to='images', verbose_name='玄関After', null=True, blank=True)
    stairs_B = models.ImageField(upload_to='images', verbose_name='階段Before', null=True, blank=True)
    stairs_A = models.ImageField(upload_to='images', verbose_name='階段After', null=True, blank=True)
    etc_B = models.ImageField(upload_to='images', verbose_name='その他Before', null=True, blank=True)
    etc_A = models.ImageField(upload_to='images', verbose_name='その他After', null=True, blank=True)
    body = SummernoteTextField(verbose_name='本文')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    image_thumbnail = ImageSpecField(source='image',
                                    processors=[Thumbnail(200, 100)],
                                    format='JPEG',
                                    options={'quality': 60})

    def get_absolute_url(self):
        return reverse('construction_detail', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        #管理画面での表示名
        verbose_name = '施工事例'
        verbose_name_plural = '施工事例 一覧'