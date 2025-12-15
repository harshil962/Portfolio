from django.shortcuts import render, redirect
from .models import Project, Certificate
from .forms import ContactForm
from django.contrib import messages 
from .models import Project, Certificate, Skill, Timeline, Testimonial

def home(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html', {'projects': projects})


def certificates(request):
    # Order by 'date_earned' descending (Newest first)
    certs = Certificate.objects.all().order_by('-date_earned')
    return render(request, 'main/certificates.html', {'certs': certs})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def about(request):
    # Fetch data from DB
    skills_backend = Skill.objects.filter(category='backend')
    skills_frontend = Skill.objects.filter(category='frontend')
    skills_tools = Skill.objects.filter(category='tools')
    
    experience = Timeline.objects.filter(category='experience')
    education = Timeline.objects.filter(category='education')
    
    testimonials = Testimonial.objects.all()

    context = {
        'skills_backend': skills_backend,
        'skills_frontend': skills_frontend,
        'skills_tools': skills_tools,
        'experience': experience,
        'education': education,
        'testimonials': testimonials,
    }
    return render(request, 'main/about.html', context)