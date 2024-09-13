from django import forms
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

#コンタクトフォーム
class ContactForm(forms.Form):
    subject = forms.fields.ChoiceField(
        label = "件名",
            choices = (
                ("", "▼ お問い合わせ内容を選択してください"),
                ("renovate", "リフォームを依頼したい"),
                ("inspection", "住宅診断を依頼したい"),
                ("estimate", "見積りを作ってほしい"),
                ("catalog", "詳細なカタログが見たい"),
                ("etc", "その他"),
            ),
            required=True,
            widget=forms.widgets.Select(attrs={
                "class":"choice-area"
            })
        )


    post = forms.CharField(
        label = "郵便番号",
        required=True,
        widget = forms.TextInput(
            attrs = {
                "class": "form-sub",
                "placeholder": "例: XXX-XXXX"
            }
        )
    )


    address = forms.CharField(
        label = "住所",
        required=True,
        widget = forms.TextInput(
            attrs = {
                "class": "form-sub",
                "placeholder": "例: 大分市〇〇町〇丁目〇番地"
            }
        )
    )


    tel = forms.CharField(
        label = "電話番号",
        required=True,
        widget = forms.TextInput(
            attrs = {
                "class": "form-sub",
                "placeholder": "例: 090-XXXX-XXXX"
            }
        )
    )


    name = forms.CharField(
        label = "お名前",
        required=True,
        widget = forms.TextInput(
            attrs = {
                "class": "form-sub",
                "placeholder": "例: 田中 太郎"
            }
        )
    )


    message = forms.CharField(
        label = "問い合わせ内容",
        widget = forms.Textarea(
            attrs = {
                "class": "form-control",
                "placeholder": "問い合わせ内容例：\n築〇年の家のキッチンの改装の見積もりを依頼したい。\n住宅診断に興味があるので話だけでも聞いてみたい。\nSWリフォームや住宅診断について詳しいカタログが欲しい\netc."
            }
        )
    )

    def send_email(self, username, email):
        subject = "【お問い合わせ" + self.cleaned_data["subject"]
        message = self.cleaned_data["message"] + f"\n\nBy {username}."
        recipient_list = ["s.hira94912@gmail.com"]   ### 送信先
        try:
            send_mail(subject, message, email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")