from rest_framework.response import Response
from django.contrib import messages
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


######################### WORDAPI ############################
@api_view(["GET", "POST"])
def WordView(request):
    try:
        if request.method == "GET":
            word = WordModel.objects.all()
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
        word = WordModel.objects.get(id=id)
    except WordModel.DoesNotExist:
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




######################### POSTAPI ############################
@api_view(["GET", "POST"])
def PostView(request):
    try:
        if request.method == "GET":
            post = PostModel.objects.all()
            serialized = PostSerializer(post, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            serialized = PostSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                print(serialized.data)
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def PostDetail(request, id):
    try:
        post = PostModel.objects.get(id=id)
    except PostModel.DoesNotExist:
        return Response({"Post Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialized = PostSerializer(post)
        return JsonResponse(serialized.data)

    elif request.method == "PUT":
        serialized = PostSerializer(post, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"Updated Successfully"},
                serialized.data,
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        post.delete()
        return HttpResponse("DELETE SUCCESSFULLY", status.HTTP_204_NO_CONTENT)










































################################## Templates ###########################

baseURL = "http://127.0.0.1:8000"
GetWord = f"{baseURL}/api/word/"  # WordAPI Url
GetPOST = f"{baseURL}/api/post/"  # PostAPI Url


# WORD CRUD OPERATION
def adminWordListApi(request):
    response = requests.get(GetWord)
    ApiWordsList = response.json() if response.status_code == 200 else []
    wordform = WordForm(request.POST or None)

    if request.method == "POST" and "word_submit" in request.POST and  wordform.is_valid():
        wordform.save()
        messages.success(request, "Word added successfully!")
        return redirect("apiword")
    context = {"ApiWordsList": ApiWordsList, "wordform": wordform}  # user this for data flow
    return render(request, "admin/admin.html", context)


def adminWordDelApi(request, id):
    word = get_object_or_404(WordModel, id=id)
    word.delete()
    messages.warning(request, "Deleted Successfully")
    return redirect("apiword")


def adminWordUpdateApi(request, id):
    word = get_object_or_404(WordModel, id=id)
    wordform = WordForm(request.POST or None, instance=word)
    if request.method == "POST" and wordform.is_valid():
        wordform.save()
        messages.success(request, "Word updated successfully!")
        return redirect("apiword")

    context = {
        "wordform": wordform,
        "word": word,
    }

    return render(request, "admin/admin.html", context)


# POST CRUD OPERATION
def adminPostListApi(request):
    response = requests.get(GetPOST)
    ApiPostsList = response.json() if response.status_code == 200 else []
    postform = PostForm(request.POST or None)
    
    if request.method == "POST" and "post_submit" in request.POST and postform.is_valid():
        postform.save()
        messages.success(request, "Post added successfully!")
        return redirect("apipost")
    context = {"ApiPostsList": ApiPostsList, "postform": postform}  # user this for data flow
    return render(request, "admin/post.html", context)


def adminPostDelApi(request, id):
    post = get_object_or_404(PostModel,id=id)
    post.delete()
    messages.warning(request, "Deleted Successfully")
    return redirect("apipost")


def adminPostUpdateApi(request, id):
    post = get_object_or_404(PostModel, id=id)
    postform = PostForm(request.POST, instance=post)
    if request.method == "POST":
        if postform.is_valid():
            postform.save()
            messages.success(request, "Post updated successfully!")
            return redirect("apipost")
        else:
            return redirect("apipost")
    else:
        postform = PostModel(instance=post)

    context = {
        "postform": postform,
        "post": post,
    }

    return render(request, "admin/post.html", context)
