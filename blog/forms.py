from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    # post_image = forms.ImageField()

    class Meta:

        model = Post
        fields = ('author', 'title', 'text', 'playlist_id')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable'}),
            # 'playlist_id':forms.CharField(attrs={'class':'editable'})
        }


