from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import championship, sports

def championship_list(request):
    championships = championship.objects.all()
    return render(request, 'list.html', {'championships': championships})

def championship_detail(request, pk):
    championship = get_object_or_404(championship, pk=pk)
    return render(request, 'detail.html', {'championship': championship})