from django import forms

from .models import Post

from tinymce.widgets import TinyMCE



class PostForm(forms.ModelForm):
	content = forms.CharField(label="",widget=TinyMCE(attrs={'cols': 200, 'rows': 300}))
	title = forms.CharField(max_length=300, label="Tytul")
	class Meta:
		model = Post
		fields = [
			"title",
			"content"
		]