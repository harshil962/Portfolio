from django.shortcuts import render, redirect
from .models import Project, Certificate
from .forms import ContactForm
from django.contrib import messages 

def home(request):
    projects = Project.objects.all()
    return render(request, 'main/home.html', {'projects': projects})

def certificates(request):
    certs = Certificate.objects.all()
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
    # If you have models, fetch from DB:
    # experience = Experience.objects.all().order_by('-start_date')
    # education = Education.objects.all().order_by('-year')
    # projects = Project.objects.all()

    # OR, if you want to hardcode it for now in the view:
    context = {
        'experience': [
            {
                'role': 'Full Stack Developer Intern',
                'company': 'Tech Solution Inc.',
                'start_date': 'Jan 2025',
                'end_date': 'Present',
                'description': 'Developing web apps using Django and React.'
            }
        ],
        'education': [
            {
                'degree': 'B.Tech Computer Engineering',
                'institution': 'Gujarat Technological University',
                'year': '2021 - 2025',
                'description': 'CGPA: 8.5'
            }
        ],
        'skills': {
            'backend': ['Python', 'Django', 'REST APIs', 'PostgreSQL'],
            'frontend': ['JavaScript', 'HTML5', 'CSS3', 'Bootstrap 5']
        },
        'projects': [
            {'title': 'Online Medical Store', 'link': '/projects/medical-store'},
            {'title': 'Portfolio Website', 'link': '/projects/portfolio'},
        ]
    }
    return render(request, 'main/about.html', context)
