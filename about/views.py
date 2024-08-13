from django.shortcuts import render
from .models import About

# Create your views here.
def about_detail(request):
    """
    Display the latest 'About content
    """
    queryset = About.objects.all().order_by('-updated_on').first()
    about = queryset

    return render(
        request,
        "about/about.html",
        {"about": about}
    )
