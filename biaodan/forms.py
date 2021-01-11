from django import forms
from .models import *
class Loginform(forms.Form):
    sname = forms.CharField(max_length=30,label=u'姓名')
    spwd = forms.CharField(label=u'密码',widget=forms.PasswordInput)


class ClazzForm(forms.ModelForm):
    class Meta:
        model = Clazz
        #元组形式
        fields = ('cname',)


class StuForm(forms.ModelForm):
    class Meta:
        model = Stu
        fields = ('sname',)