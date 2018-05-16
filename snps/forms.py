from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('PUBMEDID', 'published_date', 'JOURNAL', 'STUDY', 'LINK', 'DISEASE_TRAIT', 'CHR_ID', 'CHR_POS', 'RSID_CURRENT', 'P_VALUE', 'PVALUE_MLOG')
