from django import forms
class Loginform(forms.Form):
    sname = forms.CharField(max_length=30,label=u'姓名')
    spwd = forms.CharField(label=u'密码',widget=forms.PasswordInput)