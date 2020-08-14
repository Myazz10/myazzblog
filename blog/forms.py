from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter text...', 'rows': '4', 'cols': '50'}))

    class Meta:
        model = Comment
        fields = ('text',)


'''
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['website', 'email']
        #fields = ('author', 'text',)
'''
