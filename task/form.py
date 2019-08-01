from django import forms

class SearchForm(forms.Form):
    searchword = forms.CharField(label='Search Keyword', max_length=100)
'''
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-text',
                'required': True,
                'placeholder': 'Say something...'
            }),
        }
'''