from django.shortcuts import render, redirect
from .models import Collagename
from .forms import MyUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from functools import reduce
from django.contrib.auth.decorators import login_required
# Create your views here.


def auth(request):
  context = {}
  if request.user.is_authenticated:
    return redirect('home')
  form = MyUserCreationForm()
  if request.method == 'POST' and 'login_user' in request.POST and "login_pass" in request.POST:
    username = request.POST.get("login_user")
    password = request.POST.get("login_pass")
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('rate')
    else:
      messages.info(request, 'Username or Password is incorrect')
  elif request.method == 'POST':
    form = MyUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(
        request,
        "Account was created for " + form.cleaned_data.get("username"))
  context = {'form': form}
  print(form)
  return render(request, 'auth.html', context)


def user_logout(request):
  logout(request)
  return redirect('home')


def home(request):
  if request.method == "GET" and request.GET and isfloat(
      request.GET.get('q')) and 0 <= float(request.GET.get('q')) <= 100:
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
    context['clgs'] = {}
    for clg in Collagename.objects.filter(
        cs_cutoff__range=[0, q + 1]).order_by('-cs_cutoff'):
      if clg not in context['clgs']:
        context['clgs'][clg] = ["CS"]
      else:
        context['clgs'][clg].append("CS")

    for clg in Collagename.objects.filter(
        ecs_cutoff__range=[0, q + 1]).order_by('-ecs_cutoff'):
      if clg not in context['clgs']:
        context['clgs'][clg] = ["ECS"]
      else:
        context['clgs'][clg].append("ECS")

    for clg in Collagename.objects.filter(
        extc_cutoff__range=[0, q + 1]).order_by('-extc_cutoff'):
      if clg not in context['clgs']:
        context['clgs'][clg] = ["EXTC"]
      else:
        context['clgs'][clg].append("EXTC")

    for clg in Collagename.objects.filter(
        mech_cutoff__range=[0, q + 1]).order_by('-mech_cutoff'):
      if clg not in context['clgs']:
        context['clgs'][clg] = ["MECH"]
      else:
        context['clgs'][clg].append("MECH")
    context['clgs'] = context['clgs'].items()
  return render(request, "mainpage.html", context)


def clg_page(request, cid):
  context = {'clg': Collagename.objects.filter(id=cid)[0]}
  context['rating'] = context['clg'].rating_set.all()
  
  ctr=0
  for i in context['rating']:
    ctr+=i.rating
  print("R:",ctr)
  context['rating'] = ctr if len(context['rating']) else 6
  print("R:", context['rating'])
  return render(request, "clgmain.html", context)


@login_required(login_url='auth')
def rate(request):
  context = {'clgs': Collagename.objects.all()}
  if request.method == "POST":
    p = request.POST
    print(p.get('rating'), p.get('clg'))
    li = request.user.rating_set.filter(collagename=Collagename.objects.filter(
      collage_name=p.get('clg'))[0])
    if li:
      li[0].rating = p.get('rating')
      li[0].save()
    else:
      request.user.rating_set.create(
        collagename=Collagename.objects.filter(collage_name=p.get('clg'))[0],
        rating=p.get('rating'))
    return redirect("home")
    messages.success(request, 'Success')
  return render(request, "rate.html", context)


def add(request):
  if request.user.is_superuser:
    return HttpResponse("Only admin acccess")
  else:
    return redirect('home')
