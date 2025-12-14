from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()  
    tech_stack = models.CharField(max_length=200, help_text="Comma separated, e.g. Django, Bootstrap, SQLite")
    learnings = models.TextField(help_text="What did you learn from this project?", blank=True)
    def __str__(self):
        return self.title
    
    def get_tech_list(self):
        if self.tech_stack:
            return [x.strip() for x in self.tech_stack.split(',')]
        return []



class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    file = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


    


