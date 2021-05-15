from django.shortcuts import render, get_object_or_404
from .models import Diary

# Create your views here.
def home(request):
    posts = Diary.objects
    return render(request, 'home.html', {'posts' : posts})

def detail(request, diary_id):
    diary_detail = get_object_or_404(Diary, pk = diary_id)
    return render(request, 'detail.html', {'diary' : diary_detail})