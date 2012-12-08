# -*- coding: utf-8 -*-
from django import forms

class ReginsterForm(forms.Form):
    name = forms.CharField(required=False, label='用户名')
    email = forms.EmailField(required=False, label='电子邮箱')
    password = forms.CharField(required=False, widget=forms.PasswordInput(render_value=False), label='密码')
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(render_value=False), label='确认密码')
