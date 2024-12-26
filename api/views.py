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


# Landing page
def supermain(request):
    return render(request, "admin/supermain.html")


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
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def WordDetail(request, id):
    try:
        word = WordModel.objects.get(id=id)
    except WordModel.DoesNotExist:
        return Response(
            {"error": "Word Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serialized = WordSerializer(word)
        return JsonResponse(serialized.data)

    elif request.method == "PUT":
        serialized = WordSerializer(word, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"message": "Updated Successfully", "data": serialized.data},
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        word.delete()
        return HttpResponse(
            {"message": "DELETE SUCCESSFULLY"}, status.HTTP_204_NO_CONTENT
        )


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


######################### POST CATEGORY API ############################
@api_view(["GET", "POST"])
def PostCatView(request):
    try:
        if request.method == "GET":
            postcat = PostCategoryModel.objects.prefetch_related("posts").all()
            serialized = PostCategorySerializer(postcat, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        elif request.method == "POST":
            serialized = PostCategorySerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.data, kmstatus=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response(
            {"error": str(error)}, serialized.data, status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET", "PUT", "DELETE"])
def PostCatDetailView(request, id):
    try:
        postCat = PostCategoryModel.objects.get(id=id)
    except PostCategoryModel.DoesNotExist:
        return Response(
            {"Post Category Doesn't Exist"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serialized = PostCategorySerializer(postCat)
        return JsonResponse(serialized.data)
    elif request.method == "POST":
        serialized = PostCategorySerializer(postCat, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"Updated Successfully"},
                serialized.data,
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        postCat.delete()
        return HttpResponse("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)


######################### FOOTERAPI ############################
@api_view(["GET", "POST"])
def FooterView(request):
    try:
        if request.method == "GET":
            footer = FooterModel.objects.all()
            serialized = FooterSerializer(footer, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            serialized = FooterSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def FooterDetail(request, id):
    try:
        footer = FooterModel.objects.get(id=id)
    except FooterModel.DoesNotExist:
        return Response({"Footer Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialized = FooterSerializer(footer)
        return JsonResponse(serialized.data)

    elif request.method == "PUT":
        serialized = FooterSerializer(footer, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"Updated Successfully"},
                serialized.data,
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        footer.delete()
        return HttpResponse("DELETE SUCCESSFULLY", status.HTTP_204_NO_CONTENT)


######################### HEADERAPI ############################
@api_view(["GET", "POST"])
def HeaderView(request):
    try:
        if request.method == "GET":
            header = HeaderModel.objects.all()
            serialized = HeaderSerializer(header, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            serialized = HeaderSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def HeaderDetail(request, id):
    try:
        header = HeaderModel.objects.get(id=id)
    except HeaderModel.DoesNotExist:
        return Response({"Header Doesn't Exists"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialized = HeaderSerializer(header)
        return JsonResponse(serialized.data)

    elif request.method == "PUT":
        serialized = HeaderSerializer(header, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"Updated Successfully"},
                serialized.data,
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        header.delete()
        return HttpResponse("DELETE SUCCESSFULLY", status.HTTP_204_NO_CONTENT)


################################## Templates ###########################


baseURL = "http://127.0.0.1:8000"
GetWord = f"{baseURL}/api/word/"  # WordAPI Url
GetPOST = f"{baseURL}/api/post/"  # PostAPI Url
GetPOSTCATE = f"{baseURL}/api/postcat/"  # Post_CategoryAPI Url
GETFooter = f"{baseURL}/api/footer/"  # FooterAPI Url
GETHeader = f"{baseURL}/api/header/"  # HeaderAPI Url


# WORD CRUD OPERATION
def adminWordListApi(request):
    response = requests.get(GetWord)
    ApiWordsList = response.json() if response.status_code == 200 else []
    wordform = WordForm(request.POST or None)

    if (
        request.method == "POST"
        and "word_submit" in request.POST
        and wordform.is_valid()
    ):
        wordform.save()
        messages.success(request, "Word added successfully!")
        return redirect("apiword")
    context = {
        "ApiWordsList": ApiWordsList,
        "wordform": wordform,
    }  # user this for data flow
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
    postform = PostForm(request.POST, request.FILES or None)

    if (
        request.method == "POST"
        and "post_submit" in request.POST
        and postform.is_valid()
    ):
        postform.save()
        messages.success(request, "Post added successfully!")
        return redirect("apipost")
    context = {
        "ApiPostsList": ApiPostsList,
        "postform": postform,
    }  # user this for data flow
    return render(request, "admin/post.html", context)

def adminPostDelApi(request, id):
    post = get_object_or_404(PostModel, id=id)
    post.delete()
    messages.warning(request, "Deleted Successfully")
    return redirect("apipost")

def adminPostUpdateApi(request, id):
    post = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        pform = PostForm(request.POST, request.FILES, instance=post)
        if pform.is_valid():
            pform.save()
            messages.success(request, "Post updated successfully!")
            return redirect("apipost")
    else:
        pform = PostForm(instance=post)

    return render(request, "admin/post.html", {"postform": pform, "post": post})


# POST CATEGORY OPERATION
def adminPostCateListApi(request):
    response = requests.get(GetPOSTCATE)
    ApiPostCatList = response.json() if response.status_code==200 else []
    postcateform = PostCatForm(request.POST or None)
    
    if (request.method == "POST" and "postCat_submit" in request.POST and postcateform.is_valid()):
        postcateform.save()
        messages.success(request, "Post Category added Successfully!")
        return redirect("apipostcat")
    context ={
        "ApiPostCatList" : ApiPostCatList,
        "postcateform" : postcateform
    }
    return render(request, "admin/postcategory.html", context)

def adminPostCateDelApi(request, id):
    postcate = get_object_or_404(PostCategoryModel, id=id)
    postcate.delete()
    messages.warning(request, "Deleted Successfully")
    return redirect("apipostcat")

def adminPostCateUpdateApi(request, id):
    postcate = get_object_or_404(PostCategoryModel, id=id)
    if request.method == "POST":
        postcateform = PostCatForm(request.POST, instance=postcate)
        if postcateform.is_valid():
            postcateform.save()
            messages.success(request, "Post Category Update Successfully!")
            return redirect("apipostcat")
    else:
        postcateform = PostCatForm(instance=postcate)

    return render(request, "admin/postcategory.html", {"postcateform":postcateform, "postcate": postcate})


# FOOTER CRUD OPERATION
def adminFooterListApi(request):
    response = requests.get(GETFooter)
    ApiFooterList = response.json() if response.status_code == 200 else []
    footerform = FooterForm(request.POST, request.FILES or None)

    if (
        request.method == "POST"
        and "footer_submit" in request.POST
        and footerform.is_valid()
    ):
        footerform.save()
        messages.success(request, "Footer added successfully!")
        return redirect("apifooter")
    context = {
        "ApiFooterList": ApiFooterList,
        "footerform": footerform,
    }  # user this for data flow
    return render(request, "admin/footer.html", context)

def adminFooterDelApi(request, id):
    footer = get_object_or_404(FooterModel, id=id)
    footer.delete()
    messages.warning(request, "Deleted Successfully")
    return redirect("apifooter")

def adminFooterUpdateApi(request, id):
    footer = get_object_or_404(FooterModel, id=id)
    if request.method == "POST":
        footer_form = FooterForm(request.POST, request.FILES, instance=footer)
        if footer_form.is_valid():
            footer_form.save()
            messages.success(request, "Footer updated successfully!")
            return redirect("apifooter")
    else:
        footer_form = FooterForm(instance=footer)

    return render(
        request, "admin/footer.html", {"footerform": footer_form, "footer": footer}
    )


# Header CRUD OPERATION
def adminHeaderListApi(request):
    response = requests.get(GETHeader)
    ApiHeaderList = response.json() if response.status_code == 200 else []
    headerform = HeaderForm(request.POST, request.FILES or None)

    if (
        request.method == "POST"
        and "header_submit" in request.POST
        and headerform.is_valid()
    ):
        headerform.save()
        messages.success(request, "Header added successfully!")
        return redirect("apiheader")
    context = {
        "ApiHeaderList": ApiHeaderList,
        "headerform": headerform,
    }  # user this for data flow
    return render(request, "admin/header.html", context)

def adminHeaderDelApi(request, id):
    header = get_object_or_404(HeaderModel, id=id)
    header.delete()
    messages.warning(request, "Deleted Successfully")
    return redirect("apiheader")

def adminHeaderUpdateApi(request, id):
    header = get_object_or_404(HeaderModel, id=id)
    if request.method == "POST":
        head_form = HeaderForm(request.POST, request.FILES, instance=header)
        if head_form.is_valid():
            head_form.save()
            messages.success(request, "Header updated successfully!")
            return redirect("apiheader")
        else:
            messages.error(request, "Error updating header. Please check the form.")
    else:
        head_form = HeaderForm(instance=header)

    return render(
        request, "admin/header.html", {"headerform": head_form, "header": header}
    )
