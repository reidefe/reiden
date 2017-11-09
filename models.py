from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
 

class Post(models.model) :
 	STATUTUS_CHOICES = (
 		('draft', 'Draft'), 
 		('published', 'Published'),
 		)
 	
 	title = models.CharField(max_length=500)
 	
 	slug = models.SlugField(max_length=500 , unique_for_date='published')

 	author = models.ForeignKey(User, related_name='blog_post')

 	body = models.TextField()

 	publish = models.DateTimeField(default=timezone.now)

 	created = models.DateTimeField(auto_now_add=True)

 	updated = models.DateTimeField(auto_now=True)

 	status = models.CharField(max_length10, choices=STATUTUS_CHOICES, default='draft')

 	class Meta :
 		ordering = ('-publish',)

 	def __str__(self) : 
 		return self.title



# Create your models here.
