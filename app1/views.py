from urllib.request import HTTPRedirectHandler
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Collagename
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
  if request.method == "GET" and request.GET and request.GET.get(
      'q').isdigit() and 0 <= int(request.GET.get('q')) <= 100:
    p = redirect('main')
    p['location'] += '?q=' + request.GET.get('q')
    return p
  return render(request, 'home1.html')


def isfloat(num):
  try:
    float(num)
    return True
  except ValueError:
    return False


def main(request):
  context = {'clgs': Collagename.objects.all()}
  if request.method == "GET" and request.GET and isfloat(
      request.GET.get('q')) and 0 <= float(request.GET.get('q')) <= 100:
    q = float(request.GET.get('q'))
    context['cs_clgs'] = Collagename.objects.filter(
      cs_cutoff__range=[0, q + 1]).order_by('-cs_cutoff')
    context['ecs_clgs'] = Collagename.objects.filter(
      ecs_cutoff__range=[0, q + 1]).order_by('-ecs_cutoff')
    context['extc_clgs'] = Collagename.objects.filter(
      extc_cutoff__range=[0, q + 1]).order_by('-extc_cutoff')
    context['mech_clgs'] = Collagename.objects.filter(
      mech_cutoff__range=[0, q + 1]).order_by('-mech_cutoff')
  return render(request, "mainpage.html", context)


def clg_page(request, cid):
  context = {'clg': Collagename.objects.filter(id=cid)[0]}
  return render(request, "clgpage.html", context)


def add(request):
  if request.user.is_superuser:
    return HttpResponse("Only admin acccess")
  else:
    return redirect('home')
