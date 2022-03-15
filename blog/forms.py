from django import forms
from tinymce import TinyMCE
from .models import PostModel, CommentModel


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = PostModel
        # fields = ('content', )
        fields = '__all__'
class CommentForm(forms.ModelForm):
    desc = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Type your comment',
                'id': 'usercomment',
                'rows': 4
                }
        )
    )
    class Meta:
        model = CommentModel
        fields = ('desc',)