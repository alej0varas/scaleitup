from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^', include('board.urls', namespace="board", app_name="board")),

    url(r'^admin/', include(admin.site.urls)),
)
