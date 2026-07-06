from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse


def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    pass

def post_detail(request, slug):
    pass
#  def monthly_challenge(request, month):
    #  try:
        #  return render(request, 'challenges/challenge.html', {'month': month, 'message': monthly_challenges[month]})
    #  except:
        #  raise Http404()
        #  #  return HttpResponseNotFound('Month not supported yet')

