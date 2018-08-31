from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
import json, os
from django.forms.models import model_to_dict
from django.core import serializers

# Create your views here.
def index(request):
    return TemplateResponse(request, 'index.html', {'name': 'world'})

def test(request):
    '''该接口用于测试环境'''
    result = {
        'status': 'success',
    }
    data = json.dumps(result)
    return HttpResponse(data, content_type="application/json")

def upload(request):
    file = request.FILES.get('file')
    # ext = os.path.splitext(file.name)[1].lower()
    # (is_json_data, data) = is_json(json.loads(file.read()))
    username = request.POST.get('username')
    userfile = request.FILES.get('userfile')
    print(file, username, userfile);

    print(request.FILES, userfile.read())
    return HttpResponse(json.dumps({}), content_type="application/json")
