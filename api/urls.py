from django.urls import path
from .views import *

urlpatterns = [
    # API URL
    path('api/word/', WordView, name="word_list"),
    path('api/word/<int:id>', WordDetail, name="word_detail"),
    path('api/word/delete/<int:id>/', WordDetail, name="delete_word"),
    path('api/word/edit/<int:id>/', WordDetail, name='update_word'),
    
    
    
    
    
    
    
    
    # Template URL
    path('apiadmin/', apiadmin, name='apiword'),
    path('apiadmin/edit/<int:id>/', updateadmin, name='updateword'),
    path('apiadmin/delete/<int:id>/', delapiadmin, name="deleteword"),
]
