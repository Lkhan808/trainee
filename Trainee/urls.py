
from django.contrib import admin
from django.urls import path
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', tasks_list_api_view),
    path('api/tasks/<int:id>/', task_api_view),
]
