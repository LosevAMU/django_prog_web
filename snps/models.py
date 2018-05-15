from django.db import models
from django.utils import timezone

# Create your models here.

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
