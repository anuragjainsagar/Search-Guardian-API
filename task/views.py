# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PaginationSerializer
import requests

# Create your views here.
@api_view(['GET'])
def search_keyword(request):
    BASE_URL = "http://content.guardianapis.com/search?api-key=test"
    # PATTERN = "&showfields=thumbnail,headline&page=1&page-size=10"
    # import pdb;pdb.set_trace()
    if request.method == "GET":
        if request.GET['keyword']:
            key = request.GET['keyword']
            search_result = requests.get(BASE_URL+"&q="+key)
            return Response(search_result)
        else:
            message = "Enter any word"
            return Response(message)
