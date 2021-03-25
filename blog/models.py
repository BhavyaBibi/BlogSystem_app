from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	rate = models.IntegerField(default=0)
	def __str__(self):
		return f'{self.user}'

class Categorie(models.Model):
	title = models.CharField(max_length=20)
	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length = 50)
	overview = models.TextField()
	time_upload = models.DateTimeField(auto_now_add = True)
	auther = models.ForeignKey(Author, on_delete=models.CASCADE)
	thumbnail = models.ImageField(upload_to = 'thumbnails')
	publish = models.BooleanField()
	categories = models.ManyToManyField(Categorie)
	read = models.IntegerField(default = 0)

	class Meta:
		ordering = ['-pk']

	def __str__(self):
		return self.title

    
    