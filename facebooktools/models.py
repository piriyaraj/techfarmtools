from django.db import models

# Create your models here.

class Actress(models.Model):
    instaid=models.CharField(unique=True, max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Actress")
        verbose_name_plural = ("Actresss")

    def __str__(self):
        return self.instaid

    def get_absolute_url(self):
        return reverse("Actress_detail", kwargs={"pk": self.pk})

class Metadata(models.Model):
    name=models.CharField(unique=True, max_length=50)
    key=models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    pageId=models.CharField(max_length=500,default="")
    def __str__(self):
            return self.name  # or any other string representation you prefer
    
class Facebook_group(models.Model):
    name=models.CharField(unique=True, max_length=50)
    groupId=models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    page = models.ManyToManyField(Metadata)