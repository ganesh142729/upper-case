from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    data='sAi is PlAy'
    d={'data':data}
    return render(request,'built_in_filter.html',d)