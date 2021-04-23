from django import forms
from blog.models import Comment

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'content')
        
