import requests
from django.shortcuts import render

def search_characters(request):
    query = request.GET.get('query', '')
    characters = []
    if query:
        response = requests.get(f'https://dragonball-api.com/api/characters?name={query}')
        if response.status_code == 200:
            characters = response.json()
    return render(request, 'characters/search.html', {'characters': characters, 'query': query})