from django import forms

class AddTweetForm(forms.Form):
    content = forms.CharField(max_length=140)

    