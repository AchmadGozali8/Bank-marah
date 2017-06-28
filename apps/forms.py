from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    picture_feeling = forms.ImageField(label=('picture_feeling',),
                                       required=False, widget=forms.FileInput)

    class Meta:
        model = Post
        fields = ('anger', 'description', 'picture_feeling')
        widgets = {
            'anger': forms.Select(attrs={'class': "form-control",
                                         'style': "margin-top:10px;"}),
            'description': forms.Textarea(attrs={
                'cols': 20, 'rows': 5, 'class': "form-control",
                'id': "text", 'name': "text",
                'style': "margin-top:10px; margin-bottom:10px; "
                         "resize:None;"
            }),
        }
