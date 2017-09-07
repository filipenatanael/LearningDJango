from django.conf.urls import include, url

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^contact', views.contact, name='contact'),
]

