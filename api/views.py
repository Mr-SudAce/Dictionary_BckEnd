from rest_framework.response import Response
import requests
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import *
from .models import *
from .forms import *

# Create your views here.


######################### API ############################
@api_view(["GET", "POST"])
def WordView(request):
    try:
        if request.method == "GET":
            word = Word.objects.all()
            serialized = WordSerializer(word, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            serialized = WordSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                print(serialized.data)
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def WordDetail(request, id):
    try:
        word = Word.objects.get(id=id)
    except Word.DoesNotExist:
        return Response({"Word Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialized = WordSerializer(word)
        return JsonResponse(serialized.data)

    elif request.method == "PUT":
        serialized = WordSerializer(word, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"Updated Successfully"},
                serialized.data,
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        word.delete()
        return HttpResponse("DELETE SUCCESSFULLY", status.HTTP_204_NO_CONTENT)


################################## Templates ###########################

baseURL = "http://127.0.0.1:8000"
GetWord = f"{baseURL}/api/word/"


def apiadmin(request):
    response = requests.get(GetWord)
    if response.status_code == 200:
        ApiWordsList = response.json()
    else:
        ApiWordsList = []

    form = WordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("apiadmin")
    context = {"ApiWordsList": ApiWordsList, "form": form}
    return render(request, "admin/admin.html", context)


def delapiadmin(request, id):
    word = Word.objects.get(id=id)
    word.delete()
    return redirect("apiadmin")


def updateadmin(request, id):
    word = get_object_or_404(Word, id=id)
    if request.method == "POST":
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return HttpResponse("Updated")
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        form = WordForm(instance=word)

    context = {
        "form": form,
        "word": word,
    }

    return render(request, "admin/admin.html", context)
