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

    password = forms.CharField(max_length=30,widget=forms.PasswordInput,label=u'密码1：')
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput,label=u'密码2：')

    class Meta:
        model = Stu
        fields = ('sname',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password']!=cd['password2']:
            self.errors['password2'] = ['密码不一致']

            # raise forms.ValidationError('密码不一致！')
        return cd['password2']