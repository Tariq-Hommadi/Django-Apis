from django.urls import path, include, re_path
from App import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    re_path(r'^Api/admin$', views.adminApi),
    re_path(r'^Api/user/List$', views.userList),
    re_path(r'^Api/user/comleteTask$', views.comleteTask),
    re_path(r'^Api/user/userFilter$', views.userFilter),
    # url(r'^$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)


    # url(r'^department$',views.departmentApi),
    # url(r'^department/([0-9]+)$',views.departmentApi),

    # url(r'^employee$',views.employeeApi),
    # url(r'^employee/([0-9]+)$',views.employeeApi),

    # url(r'^employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
