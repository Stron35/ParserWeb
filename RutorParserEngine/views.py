from django.shortcuts import render
from .parser import *

# Create your views here.

def search_torrent(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        print(query)
        # query = 'Warcraft'
        data = main_parser(query)
        data_keys = list(data.keys())
        
    else:
        data = {}
        data_keys = []
    return render(request, 'RutorParserEngine/search_torrent.html', {'data':data, 'data_keys': data_keys})
