from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('PUBMEDID', 'published_date', 'JOURNAL', 'STUDY', 'LINK', 'DISEASE_TRAIT', 'CHR_ID', 'CHR_POS', 'RSID_CURRENT', 'P_VALUE', 'PVALUE_MLOG')

class SNP_search_form(forms.ModelForm):
    CHR_ID =  forms.IntegerField(label='Chromosome ID', required=False)
    CHR_POS =  forms.IntegerField(label='Position of SNP on Chromosome', required=False)
    RSID_CURRENT =  forms.IntegerField(label='RSID of SNP', required=False)
    # limit = forms.IntegerField(label='Limit', required=False)

    class Meta:
        model = Post
        fields = ('CHR_ID', 'CHR_POS', 'RSID_CURRENT')

class interval_SNP_search(forms.Form):

    min_limit = forms.IntegerField(label='Bottom Limit', required=True)
    max_limit = forms.IntegerField(label='Upper Limit', required=True)

class phenotype_search_form(forms.Form):

    my_pheno = forms.CharField(label='Phenotype', required=True)
