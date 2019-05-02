
from django.contrib import admin
from django.urls import path, include

from .views import *
from django.conf.urls import url

namespace = 'match'
urlpatterns = [
	path('', main, name="main"),

	# api to post 
	path('api-matches/', MatchAppView.as_view(), name="MatchAppView"),

	path('api-match-details/', MatchDetailsView.as_view(), name="MatchDetails"),

	path('get-matches/', GetMatchesView.as_view(), name="GetMatchesView"),

]