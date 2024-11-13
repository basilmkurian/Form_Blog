from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['name', 'description', 'attachment']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
