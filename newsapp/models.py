from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as auth_User

# Create your models here.

class User(models.Model):
	# User_ID <-- built-in ID
	user = models.OneToOneField(auth_User, on_delete=models.CASCADE)
	# username = models.CharField(max_length=50)
	# email = models.CharField(max_length=100)
	# fname = models.CharField(max_length=50)
	# lname = models.CharField(max_length=50)

	def __str__(self):
		return " ID: "+str(self.id)+" -- "+self.user.username

class News_Article(models.Model):
	# Article_ID <-- built-in ID
	title = models.CharField(max_length=200)
	# Author_ID will be a Foreign Key referring to the user table
	author = models.ForeignKey(User, on_delete=models.PROTECT) # when a user is deleted, the article will not be deleted
	content = models.TextField(blank=False) #A large text field. The default form widget for this field is a Textarea.
	creation_time = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created. 
	last_modified = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved with .save()
	likes = models.IntegerField(default=0)
	non_empty = models.TextField(null=False)
	# demo_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return " ID: "+str(self.id)+" -- "+self.title 


class Comment(models.Model):
	# Comment_ID <-- built-in ID
	commenter = models.ForeignKey(User, on_delete=models.CASCADE) # when a user is deleted, all comments created by this user will be deleted.
	article = models.ForeignKey(News_Article, on_delete=models.CASCADE) # when an article is deleted, all comments about it will be deleted.
	comments = models.TextField() #A large text field. The default form widget for this field is a Textarea.

class Subscription(models.Model):
	subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriber")
	subscribee = models.ForeignKey(User, on_delete=models.PROTECT, related_name="subscribee")
	subscribe_when = models.DateTimeField(auto_now=True)
