from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('anger', 'description')
        widgets = {
        	'anger': forms.Select(attrs={'class': "selectpicker"}),
            'description': forms.Textarea(attrs={'cols': 20, 'rows': 5, 'class': "form-control", 'id': "text", 'name': "text",'style': " resize:None;"}),
        }

class PostUpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('description',)
		widgets = {
			'description': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
		}