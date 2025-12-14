from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Project(models.Model):
    title = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=200, help_text="Comma separated technologies")
    description = models.TextField() 
    image = models.ImageField(upload_to='portfolio/images/')
    live_link = models.URLField(blank=True, null=True, help_text="Link to deployed site")
    source_link = models.URLField(blank=True, null=True, help_text="Link to GitHub")
    demo_video = models.FileField(
        upload_to='portfolio/videos/', 
        blank=True, 
        null=True, 
        help_text="Upload a short .mp4 video or .gif showing the project in action."
    )
    
    def __str__(self):
        return self.title
        
    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]
    
class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    file = models.ImageField(upload_to='certificates/')
    date_earned = models.DateField(blank=True, null=True, help_text="When did you get this?")

    def __str__(self):
        return self.name

    # Auto-compress image on save
    def save(self, *args, **kwargs):
        if self.file:
            img = Image.open(self.file)
            # Resize if too huge (e.g. > 1000px)
            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)
                
                # Compress
                buffer = BytesIO()
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(buffer, format='JPEG', quality=75, optimize=True)
                
                new_image = ContentFile(buffer.getvalue())
                self.file.save(self.file.name, new_image, save=False)

        super().save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
    

    # portfolio/models.py (Add these to your existing file)

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('tools', 'Tools & DevOps'),
    )
    name = models.CharField(max_length=50) # e.g., "Django"
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name

class Timeline(models.Model):
    # This handles both Education and Experience
    TYPE_CHOICES = (
        ('education', 'Education'),
        ('experience', 'Experience'),
    )
    title = models.CharField(max_length=100) # e.g., "Full Stack Developer"
    organization = models.CharField(max_length=100) # e.g., "Tech Solutions Inc."
    start_date = models.CharField(max_length=20) # Keep as Char for flexibility like "Jan 2025"
    end_date = models.CharField(max_length=20, default="Present")
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=TYPE_CHOICES)

    class Meta:
        ordering = ['-id'] # Shows newest added first

    def __str__(self):
        return f"{self.title} at {self.organization}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100) # e.g., "Project Manager"
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name
