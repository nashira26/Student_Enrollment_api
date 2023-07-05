"""
URL configuration for apiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enrollment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funnelstatus/', views.get_funnel_status_list, name="get_funnel_status_list"),
    path('funnelstatus/create/', views.create_funnel_status, name="create_funnel_status"),
    path('funnelstatus/<int:id>/', views.get_funnel_status, name="get_funnel_status"),
    path('funnelstatus/<int:id>/update/', views.update_funnel_status, name="update_funnel_status"),
    path('funnelstatus/<int:id>/delete/', views.delete_funnel_status, name="delete_funnel_status"),
    path('student/create/', views.create_student, name="create_student"),
    path('student/<int:id>/', views.get_student, name="get_student"),
    path('student/<int:id>/update/', views.update_student, name="update_student"),
]

