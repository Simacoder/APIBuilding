from django.http import response
from django.shortcuts import render
import requests


def home(request):
  # using an API
  response = requests.get('https://api.github.com/events')
  data = response.json()
  results = data[0]["repo"]

  # Example 2
  response2 = requests.get('https://dog.ceo/api/breeds/image/randoms')
  data2 = response2.json()
  result2 = data2[0]["message"]
  return render(request, 'template/index.html', {
      'results': results,
      'result2': result2
  })
