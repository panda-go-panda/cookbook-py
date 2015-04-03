from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cook.views.home', name='home'),
    url(r'^recipes/(.+)$', 'cook.views.recipes', name='recipes'),
    url(r'^ingredients/(.+)$', 'cook.views.ingredients', name='ingredients'),
    url(r'^recipe/(.+)$', 'cook.views.recipe', name='recipe'),
    url(r'^admin/', include(admin.site.urls)),
)
