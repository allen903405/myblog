from django import forms

class BlogForm(forms.Form):
    title =  forms.CharField(label='標題')
    author = forms.CharField(label='作者')
    content = forms.CharField(label='內文',widget=forms.Textarea)