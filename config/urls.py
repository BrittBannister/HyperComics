"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path

from ComicBaseApp.views import index, AddCommentView, SignupView, LoginView, logout_view, e404, e500

urlpatterns = [
    path("", index, name="home"),
    path("admin/", admin.site.urls),
    path("add_comment/", AddCommentView.as_view(), name="add_comment"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    # path('404/', e404),
    # path('500/', e500)
]

handler404 = 'ComicBaseApp.views.e404'
handler500 = 'ComicBaseApp.views.e500'