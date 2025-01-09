from .serializers import *
from .models import *
from .forms import *
from django.contrib import messages
import requests
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

# import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from .forms import RegistrationForm, LoginForm, UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

# Create your views here.


######################### USERAPI ############################
@api_view(["POST"])
def CreateUser(request):
    try:
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            user = serialized.save()
            if user:
                return Response(
                    {"message": "User created successfully"},
                    status=status.HTTP_201_CREATED,
                )
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {"message": f"Failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def GetAllUser(request):
    users = User.objects.all()
    serialized = UserSerializer(users, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def GetUserById(request, id):
    users = get_object_or_404(User, id=id)
    serialized = UserSerializer(users)
    return Response(serialized.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def UpdateUser(request, id):
    users = get_object_or_404(User, id=id)
    serialized = UserSerializer(users, data=request.data, partial=True)
    if serialized.is_valid():
        serialized.save()
        return Response(
            {"message": "User updated successfully"}, status=status.HTTP_200_OK
        )
    return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeleteUser(request, id):
    users = get_object_or_404(User, id=id)
    users.delete()
    return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)


######################### USERAPI ############################


######################### WORDAPI ############################
@api_view(["POST"])
def CreateWord(request):
    try:
        serialized = WordSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"message": "Failed"}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetAllWord(request):
    try:
        word = WordModel.objects.all()
        serialized = WordSerializer(word, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Word Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def GetWordById(request, id):
    try:
        word = get_object_or_404(WordModel, id=id)
        serialized = WordSerializer(word)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Word Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def UpdateWord(request, id):
    try:
        word = get_object_or_404(WordModel, id=id)
        serialized = WordSerializer(word, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"message": "Updated Successfully", "data": serialized.data},
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"Updatation Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeleteWord(request, id):
    try:
        word = get_object_or_404(WordModel, id=id)
        word.delete()
        return HttpResponse({"Word Deleted Successfully"}, status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse({"Failed"}, status=status.HTTP_400_BAD_REQUEST)


######################### POST CATEGORY API ############################
@api_view(["POST"])
def CreatePostCategory(request):
    try:
        serialized = PostCategorySerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(
                {"message": "Created Successfully", "data": serialized.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"message": "Failed"}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetAllCategories(request):
    try:
        postcat = PostCategoryModel.objects.prefetch_related("posts").all()
        serialized = PostCategorySerializer(postcat, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Category Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def GetCategoriesById(request, id):
    try:
        postcat = get_object_or_404(PostCategoryModel, id=id)
        serialized = PostCategorySerializer(postcat)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Category Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def UpdateCategory(request, id):
    try:
        postcat = get_object_or_404(PostCategoryModel, id=id)
        serialized = PostCategorySerializer(postcat, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"message": "Updated Successfully", "data": serialized.data},
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"Updatation Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeleteCategory(request, id):
    try:
        postcat = get_object_or_404(PostCategoryModel, id=id)
        postcat.delete()
        return HttpResponse(
            {"Category Deleted Successfully"}, status.HTTP_204_NO_CONTENT
        )
    except:
        return HttpResponse({"Failed"}, status=status.HTTP_400_BAD_REQUEST)


######################### POSTAPI ############################
@api_view(["POST"])
def CreatePost(request):
    try:
        serialized = PostSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"message": "Failed"}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetAllPost(request):
    try:
        post = PostModel.objects.all()
        serialized = PostSerializer(post, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Category Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def GetAllPostById(request, id):
    try:
        post = get_object_or_404(PostModel, id=id)
        serialized = PostSerializer(post)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Category Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def UpdatePost(request, id):
    try:
        post = get_object_or_404(PostModel, id=id)
        serialized = PostSerializer(post, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"message": "Updated Successfully", "data": serialized.data},
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"Updatation Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeletePost(request, id):
    try:
        post = get_object_or_404(PostModel, id=id)
        post.delete()
        return HttpResponse({"Post Deleted Successfully"}, status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse({"Failed"}, status=status.HTTP_400_BAD_REQUEST)


######################### FOOTERAPI ############################
@api_view(["POST"])
def CreateFooter(request):
    try:
        serialized = FooterSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"message": "Failed"}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetAllFooter(request):
    try:
        footer = FooterModel.objects.all()
        serialized = FooterSerializer(footer, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Footer Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def GetAllFooterById(request, id):
    try:
        footer = get_object_or_404(FooterModel, id=id)
        serialized = FooterSerializer(footer)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Footer Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["PUT"])
def UpdateFooter(request, id):
    try:
        footer = get_object_or_404(FooterModel, id=id)
        serialized = FooterSerializer(footer, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"message": "Updated Successfully", "data": serialized.data},
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"Updatation Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeleteFooter(request, id):
    try:
        footer = get_object_or_404(FooterModel, id=id)
        footer.delete()
        return HttpResponse({"Footer Deleted Successfully"}, status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse({"Failed"}, status=status.HTTP_400_BAD_REQUEST)


######################### HEADERAPI ############################
@api_view(["POST"])
def CreateHeader(request):
    try:
        serialized = HeaderSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"message": "Failed"}, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetAllHeader(request):
    try:
        header = HeaderModel.objects.all()
        serialized = HeaderSerializer(header, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Header Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def GetAllHeaderById(request, id):
    try:
        header = get_object_or_404(HeaderModel, id=id)
        serialized = HeaderSerializer(header)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Header Found"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def UpdateHeader(request, id):
    try:
        header = get_object_or_404(HeaderModel, id=id)
        serialized = HeaderSerializer(header, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"message": "Updated Successfully", "data": serialized.data},
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"Updatation Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeleteHeader(request, id):
    try:
        header = get_object_or_404(HeaderModel, id=id)
        header.delete()
        return HttpResponse({"Header Deleted Successfully"}, status.HTTP_204_NO_CONTENT)
    except:
        return HttpResponse({"Failed"}, status=status.HTTP_400_BAD_REQUEST)


######################### PAGEAPI ############################
@api_view(["POST"])
def CreatePage(request):
    try:
        serialized = PageSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetAllPage(request):
    try:
        page = PageModel.objects.all()
        serialized = PageSerializer(page, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Page Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def GetAllPageById(request, id):
    try:
        page = get_object_or_404(PageModel, id=id)
        serialized = PageSerializer(page)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({f"{id} doesn't exist"}, status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def UpdatePage(request, id):
    try:
        page = get_object_or_404(PageModel, id=id)
        serialized = PageSerializer(page, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"message": "Updated Successfully", "data": serialized.data},
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"Updatation Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeletePage(request, id):
    page = PageModel.objects.get(id=id)
    page.delete()
    return JsonResponse({"message": "Deleted Successfully"}, status.HTTP_204_NO_CONTENT)


######################### BLOGAPI ############################
@api_view(["POST"])
def CreateBlog(request):
    try:
        serialized = BlogSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse(
            {"error": f"Blog creation failed: {str(e)}"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def GetAllBlog(request):
    try:
        blog = BlogModel.objects.all()
        serialized = BlogSerializer(blog, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({"No Blog Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def GetAllBlogById(request, id):
    try:
        blog = get_object_or_404(BlogModel, id=id)
        serialized = BlogSerializer(blog)
        return Response(serialized.data, status=status.HTTP_200_OK)
    except:
        return HttpResponse({f"{id} doesn't exist"}, status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def UpdateBlog(request, id):
    try:
        blog = get_object_or_404(BlogModel, id=id)
        serialized = BlogSerializer(blog, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(
                {"message": "Updated Successfully", "data": serialized.data},
                status=status.HTTP_202_ACCEPTED,
            )
        return JsonResponse(serialized.data, status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse({"Updatation Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeleteBlog(request, id):
    blog = BlogModel.objects.get(id=id)
    blog.delete()
    return JsonResponse({"message": "Deleted Successfully"}, status.HTTP_204_NO_CONTENT)


################################## Templates ###########################
baseURL = "http://127.0.0.1:8000"
Get_Word = f"{baseURL}/api/all/word/"  # WordAPI Url
Get_POST = f"{baseURL}/api/all/post/"  # PostAPI Url
Get_POSTCATE = f"{baseURL}/api/all/postcat/"  # Post_CategoryAPI Url
GET_Footer = f"{baseURL}/api/all/footer/"  # FooterAPI Url
GET_Header = f"{baseURL}/api/all/header/"  # HeaderAPI Url
GET_Page = f"{baseURL}/api/all/page/"  # PAGEAPI Url
GET_Blog = f"{baseURL}/api/all/blog/"  # BLOGAPI Url
GET_User = f"{baseURL}/api/all/user/"  # USER URL


# Admin Login
@login_required
@csrf_exempt
def supermain(request):
    return render(request, "admin/supermain.html")
@csrf_exempt
def authentication(request):
    return render(request, "admin/authentication.html")


@csrf_exempt
def admin_register(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if len(password) < 8:
            messages.error(request, "Password should be at least 8 characters long")
            return redirect("admin_register")

        if password != confirm_password:
            messages.error(request, "Password Do not match")
            return redirect("admin_register")

        if User.objects.filter(username=username).exists():
            messages.error(request, f"{username} already Exists")
            return redirect("admin_register")

        if User.objects.filter(email=email).exists():
            messages.error(request, f"{email} already Exists")
            return redirect("admin_register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.save()
        messages.success(
            request, f"Admin Account created successfully! You can now log in."
        )
        return redirect("admin_login")

    return render(request, "admin/auth/register.html")


@csrf_exempt
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # messages.success(request, f"Login Successfully Welcome, {username}!")
            return redirect("supermain")
        else:
            messages.error(request, f"Invalid username and Password.")
    return render(request, "admin/auth/login.html")


def admin_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("admin_login")


# User Login
@csrf_exempt
def user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if len(password) < 8:
            messages.error(request, "Password should be at least 8 characters long")
            return redirect("user_register")

        if password != confirm_password:
            messages.error(request, "Password Do not match")
            return redirect("user_register")

        if User.objects.filter(username=username).exists():
            messages.error(request, f"{username} already Exists")
            return redirect("user_register")

        if User.objects.filter(email=email).exists():
            messages.error(request, f"{email} already Exists")
            return redirect("user_register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_staff = True
        
        user.save()
        messages.success(
            request, f"User Account created successfully! You can now log in."
        )
        return redirect("user_login")

    return render(request, "admin/user/User_register.html")


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            if user.status == "Superuser":
                login(request, user)
                messages.success(request, f"Login Successfully Welcome, {username}!")
                return redirect("supermain")
            else:
                return HttpResponse("Did match")
        else:
            messages.error(request, f"Invalid username and Password.")
    return render(request, "admin/user/User_login.html")


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("user_login")


##########################################################################################################################################################################


# User CRUD Operation
def userListApi(request):
    response = requests.get(GET_User)
    ApiUsersList = response.json() if response.status_code == 200 else []
    userform = User(request.POST or None)
    if (
        request.method == "POST"
        and "user_submit" in request.POST
        and userform.is_valid()
    ):

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if username and email and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username, email=email, password=password
                )
                messages.success(request, "User added successfully!")
                return redirect("apiuser")
            messages.error(request, "User already exists!")
        else:
            messages.error(request, "All fields are required.")

    context = {
        "ApiUsersList": ApiUsersList,
    }
    return render(request, "admin/user.html", context)


def userDelApi(request, id):
    users = get_object_or_404(User, id=id)
    users.delete()
    messages.warning(request, "User Deleted Successfully")
    return redirect("apiuser")


def userUpdateApi(request, id):
    users = get_object_or_404(User, id=id)
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        if username and email:
            if not User.objects.filter(username=username).exclude(id=id).exists():
                users.username = username
                users.email = email
                users.save()
                messages.success(request, "User updated successfully!")
                return redirect("apiuser")
            messages.error(request, "Username already exists.")
        else:
            messages.error(request, "All fields are required.")
    return render(request, "admin/user.html", {"users": users})


# WORD CRUD OPERATION
def adminWordListApi(request):
    response = requests.get(Get_Word)
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
    response = requests.get(Get_POST)
    response1 = requests.get(Get_POSTCATE)
    ApiPostsList = response.json() if response.status_code == 200 else []
    ApiPostCatList = response1.json() if response1.status_code == 200 else []
    postform = PostForm(request.POST, request.FILES or None)
    # postcateform = PostCatForm(request.POST or None)

    if (
        request.method == "POST"
        and "post_submit" in request.POST
        and postform.is_valid()
    ):
        postform.save()
        messages.success(request, "Post added successfully!")
        return redirect("apipost")
    context = {
        "ApiPostCatList": ApiPostCatList,
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
    post_instance = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        pform = PostForm(request.POST, request.FILES, instance=post_instance)
        if pform.is_valid():
            pform.save()
            messages.success(request, "Post updated successfully!")
            return redirect("apipost")
    else:
        pform = PostForm(instance=post_instance)

    return render(
        request, "admin/post.html", {"postform": pform, "post_instance": post_instance}
    )


# POST CATEGORY OPERATION
def adminPostCateListApi(request):
    response = requests.get(Get_POSTCATE)
    ApiPostCatList = response.json() if response.status_code == 200 else []
    postcateform = PostCatForm(request.POST or None)

    if (
        request.method == "POST"
        and "postCat_submit" in request.POST
        and postcateform.is_valid()
    ):
        postcateform.save()
        messages.success(request, "Post Category added Successfully!")
        return redirect("apipostcat")
    context = {"ApiPostCatList": ApiPostCatList, "postcateform": postcateform}
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

    return render(
        request,
        "admin/postcategory.html",
        {"postcateform": postcateform, "postcate": postcate},
    )


# FOOTER CRUD OPERATION
def adminFooterListApi(request):
    response = requests.get(GET_Footer)
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
    response = requests.get(GET_Header)
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


# Page CRUD OPERATION
def adminPageListApi(request):
    response = requests.get(GET_Page)
    ApiPageList = response.json() if response.status_code == 200 else []
    pageform = PageForm(request.POST or None)

    if (
        request.method == "POST"
        and "page_submit" in request.POST
        and pageform.is_valid()
    ):
        pageform.save()
        messages.success(request, "Page added Successfully!")
        return redirect("apipage")
    context = {"ApiPageList": ApiPageList, "pageform": pageform}

    return render(request, "admin/page.html", context)


def adminPageDelApi(request, id):
    page = get_object_or_404(PageModel, id=id)
    page.delete()
    messages.warning(request, "Deleted Successfully")
    return redirect("apipage")


def adminPageUpdateApi(request, id):
    page = get_object_or_404(PageModel, id=id)
    if request.method == "POST":
        page_form = PageForm(request.POST, instance=page)
        if page_form.is_valid():
            page_form.save()
            messages.success(request, "Page Updated Sucessfully!")
            return redirect("apipage")
        else:
            messages.error(request, "Error updating page. Please check the form.")
    else:
        page_form = PageForm(instance=page)

    return render(request, "admin/page.html", {"pageform": page_form, "page": page})


# Blog CRUD OPERATION
def adminBlogListApi(request):
    response = requests.get(GET_Blog)
    ApiBlogList = response.json() if response.status_code == 200 else []
    blogform = BlogForm(request.POST, request.FILES or None)

    if (
        request.method == "POST"
        and "blog_submit" in request.POST
        and blogform.is_valid()
    ):
        blogform.save()
        messages.success(request, "Blog added Successfully!")
        return redirect("apiblog")
    context = {"ApiBlogList": ApiBlogList, "blogform": blogform}

    return render(request, "admin/blog.html", context)


def adminBlogDelApi(request, id):
    blog = get_object_or_404(BlogModel, id=id)
    blog.delete()
    messages.warning(request, "Deleted Successfully")
    return redirect("apiblog")


def adminBlogUpdateApi(request, id):
    blog = get_object_or_404(BlogModel, id=id)
    if request.method == "POST":
        blog_form = BlogForm(request.POST, instance=blog)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, "Blog Updated Sucessfully!")
            return redirect("apiblog")
        else:
            messages.error(request, "Error updating blog. Please check the form.")
    else:
        blog_form = BlogForm(instance=blog)

    return render(request, "admin/blog.html", {"blogform": blog_form, "blog": blog})
