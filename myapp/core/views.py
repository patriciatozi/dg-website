from django.shortcuts import render
from .models import SocialMedia

def index(request):
    social_medias = SocialMedia.objects.all()
    return render(request, 'index.html', {'social_medias':social_medias})