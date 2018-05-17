from django.db import models
from django.utils import timezone

# Create your models here.

class SNP(models.Model):
    Chrom = models.IntegerField()
    Chrom_pos = models.IntegerField()
    Rsid = models.IntegerField()

class Reference(models.Model):
    Pubmedid = models.IntegerField()
    Journal = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Date = models.DateField()

class Disease_trait(models.Model):
    Name = models.CharField(max_length=200)

class SNP2Phenotype2Ref(models.Model):
    Snp_id = models.ForeignKey(SNP, on_delete=models.CASCADE)
    Disease_trait_id = models.ForeignKey(Disease_trait, on_delete=models.CASCADE)
    Reference_id = models.ForeignKey(Reference, on_delete=models.CASCADE)
    pvalue = models.FloatField(default = 0)
    neglog10pvalue = models.FloatField(default = 0)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    PUBMEDID = models.IntegerField(default = 0)
    published_date = models.DateField(
             blank=True, null=True)
    JOURNAL = models.CharField(max_length=100, default = "")
    LINK = models.CharField(max_length=200, default = "")
    STUDY = models.CharField(max_length=400, default = "")
    DISEASE_TRAIT = models.CharField(max_length=200, default = "")
    CHR_ID = models.IntegerField(default = 0)
    CHR_POS = models.IntegerField(default = 0)
    RSID_CURRENT = models.IntegerField(default = 0)
    P_VALUE = models.FloatField(default = 0)
    PVALUE_MLOG = models.FloatField(default = 0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.STUDY

class Tost(models.Model):
    f1 = models.CharField(max_length=100, default = "")
    f2 = models.CharField(max_length=200, default = "")
