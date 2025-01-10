from .forms import *
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse


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
