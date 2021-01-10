from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from challenge.models import Bookmarks
from django.shortcuts import get_object_or_404


def index(request):
    data = requests.get(
        "https://api.github.com/search/repositories?q=language:python&sort=stars=desc&per_page=10")
    if data.status_code == 200:
        return render(request, 'firstpage.html', {'data': data.json()})


def bookmarked(request):
    data = requests.get(
        "https://api.github.com/search/repositories?q=language:python&sort=stars=desc&per_page=10")
    d = data.json()
    reps = Bookmarks.objects.values_list('repo_id', flat=True)
    repos = list(reps)
    d["items"] = [x for x in d["items"] if str(x["id"]) in repos]
    if data.status_code == 200:
        return render(request, 'bookmarked.html', {'data': d})


def details(request, id, id2):
    data = requests.get(
        "https://api.github.com/repos/{}/{}".format(id, id2))

    if data.status_code == 200:
        return render(request, 'res.html', {'data': data.json()})


def bookmark(request, id):
    entry = Bookmarks.objects.filter(repo_id=id)
    if len(entry) > 0:
        return JsonResponse({'message': "The repo is already bookmarked"})
    b = Bookmarks(repo_id=str(id), bookmarked=True)
    b.save()
    return JsonResponse({'message': "Successfully added"})


def remove(request, id):
    entry = Bookmarks.objects.filter(repo_id=id)
    if len(entry) > 0:
        Bookmarks.objects.filter(repo_id=id).delete()
        return JsonResponse({'message': "Successfully deleted"})
    else:
        return JsonResponse({'message': "The record was not found"})
