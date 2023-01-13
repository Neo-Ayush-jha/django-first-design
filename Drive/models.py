from django.db import models
class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    contact=models.TextField()
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
class Intern(models.Model):
    name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    post=models.CharField(max_length=150)

    def __str__(self):
        return self.name
    