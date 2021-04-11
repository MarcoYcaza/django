from django import forms


class MyAnswerForm(forms.Form):
    answer = forms.CharField(
        widget=forms.Textarea(attrs={"style": "height: 100px;width:100%"})
    )
