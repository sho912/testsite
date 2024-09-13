from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")



#admin 複数画像管理ウィジェット
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# 複数のファイルをアップロードするフィールドクラスを作成
#（コピペでOK！）
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

# 複数のファイルをアップロードするフォームクラスを作成
# （ご自身の使用したいフォームクラスにMultipleFileFieldを追加してください）
class MultipleFileUploadForm(forms.Form):

    #  複数のファイルをアップロードするフィールドを作成
    files = MultipleFileField(label="複数のファイルを選択")
