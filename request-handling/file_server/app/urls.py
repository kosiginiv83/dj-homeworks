from django.urls import path
from app.views import FileList, file_content

urlpatterns = [
    path('', FileList.as_view(), name = 'file_list'),
    path('<int:year>-<int:month>-<int:day>', FileList.as_view(), name='file_list'),
    path('file/<str:file>', file_content, name='file_content'),
]

# 1) - (127.0.0.1:8000)
# 2) /2018-08-16 (127.0.0.1:8000/2018-08-16) 2018-01-01
# 3) /file/server.01 (127.0.0.1:8000/file/server.01)
