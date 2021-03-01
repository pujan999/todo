from django.shortcuts import render

# Create your views here.
def viewlist(request):
    return render(request, 'index.html')
