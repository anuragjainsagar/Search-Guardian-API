# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
#from rest_framework.pagination import PaginationSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task.models import GuardianRestAPI
from task.serializers import GuardianRestAPISerializer
import requests

from django.views.generic import TemplateView
from .form import SearchForm
# Create your views here.

class SearchView(TemplateView):
    template_name = 'search.html'

    def get_name(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = SearchForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/notfound/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = SearchForm()

        return render(request, 'search.html', {'form': form})

def index(request):
    return render(request,'index.html')
@api_view(['GET', 'POST','REQUEST'])
def search_param(request):
    if request.method == "POST":
        BASE_URL = "http://content.guardianapis.com/search?api-key=test"
        PATTERN = "&q="+request.POST['name']+"&showfields=thumbnail,headline&show-tags=keyword&page="+request.POST['page']+"&page-size=5"
        data = requests.get(BASE_URL + PATTERN)
        print(BASE_URL + PATTERN)
    return render(request, "newsview.html",  {'data':data.json() ,'url':BASE_URL + PATTERN})
    #return render_to_response(request,'newsview.html',{'data':data.json()})
@api_view(['GET', 'POST','REQUEST'])
def search_keyword(request):
    BASE_URL = "http://content.guardianapis.com/search?api-key=test"
    PATTERN = "&showfields=thumbnail,headline&page=1&page-size=10"
    data = requests.get(BASE_URL+PATTERN)
    return Response(data.json())
    '''
    if request.method == 'GET':
        snippets = GuardianRestAPI.objects.all()
        serializer = GuardianRestAPISerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GuardianRestAPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
class ListNewsView(generics.ListAPIView):
    queryset = GuardianRestAPI.objects.all()
    serializer_class = GuardianRestAPISerializer
class GetALLNewsfromAPI():
    pass