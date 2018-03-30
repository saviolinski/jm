from django import forms

from .models import Post

from tinymce.widgets import TinyMCE



class PostForm(forms.ModelForm):
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 200, 'rows': 300}))
	class Meta:
		model = Post
		fields = [
			"title",
			"content"
		]