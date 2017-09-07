from django.conf.urls import url

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^contact', views.contact, name='contact'),
]

