from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^instagram/profile$',views.profile,name='displayProfile'),
    url(r'^instapp/prof/(\d+)',views.prof,name="prof"),
    url(r'^project',views.project,name="project"),
    url(r'^profile/',views.profile,name="profile"),
    url(r'^prof/',views.prof,name="prof"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
