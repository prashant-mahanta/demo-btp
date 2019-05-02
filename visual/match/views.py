from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from .serializers import *
from .models import *
from datetime import datetime


def main(request):
	matches = Matches.objects.all()
	return render(request, "index.html", {"matches":matches})


class MatchAppView(APIView):
	permission_classes = [AllowAny]

	def get(self, request, format=None):
		objects = Matches.objects.all()
		serialized_object = MatchSerializer(objects, many=True)
		# print("get request")
		try:
			return Response(serialized_object.data)
		except:
			return Response("NoData")

# # match_id, date, location, team1, team2, match_type, competition, winner, mom, win_wickets, win_run, toss_win, decision

	def post(self, request, format=None):
		match_id = request.data.get("match_id")
		date = request.data.get("date")
		location = request.data.get("location")
		team1 = request.data.get("team1")
		team2 = request.data.get("team2")
		match_type = request.data.get("match_type")
		competition = request.data.get("competition")
		winner = request.data.get("winner")
		mom = request.data.get("mom")
		win_wickets = request.data.get("win_wickets")
		win_run = request.data.get("win_run")
		toss_win = request.data.get("toss_win")
		decision = request.data.get("decision")

		instance = Matches(match_id=match_id, date=date, location=location, team1=team1, team2=team2, match_type=match_type,competition=competition,winner=winner,mom=mom,win_wickets=win_wickets,win_run=win_run,toss_win=toss_win, decision=decision)
		instance.save()


		serialized_object = MatchSerializer(instance, many=True)
		try:
			return Response(serialized_object.data)
		except:
			return Response("Done")


class MatchDetailsView(APIView):
	permission_classes = [AllowAny]

	def get(self, request, format=None):
		objects = MatcheDetails.objects.all()
		serialized_object = MatchDetailsSerializer(objects, many=True)
		try:	
			return Response(serialized_object.data)
		except:
			return Response("NoData")

# # match_id, date, location, team1, team2, match_type, competition, winner, mom, win_wickets, win_run, toss_win, decision

	def post(self, request, format=None):
		match_id = request.data.get("match_id")
		over = request.data.get("over")
		runs = request.data.get("runs")
		wickets = request.data.get("wickets")
		striker = request.data.get("striker")
		non_striker = request.data.get("non_striker")
		bowler = request.data.get("bowler")
		team = request.data.get("team")
		match = Matches.objects.get(match_id=match_id)
		instance = MatchDetails(match_id=match,over=over, team = team, runs=runs, wickets = wickets, striker=striker, non_striker=non_striker, bowler=bowler)
		instance.save()

		print("POSTT",instance)
		serialized_object = MatchDetailsSerializer(instance, many=True)
		try:
			return Response(serialized_object.data)
		except:
			return Response("Done")


class GetMatchesView(APIView):
	permission_classes = [AllowAny]

	def get(self, request, format=None):
		competition = request.GET["competition"]
		team = request.GET["team"]
		date = request.GET["date"]
		print(date)
		dates = {"Jan":"01", "Feb":"02", "Mar": "03", "Apr":"04", "May":"05", "Jun":"06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct":"10", "Nov":"11", "Dec":"12"}
		try:
			date = date.split("/")
			date[1]=str(dates[date[1]])
			date='/'.join(date)
		except:
			date = date

		date = datetime.strptime(date, '%d/%m/%y')
		matches = Matches.objects.filter(competition=competition)
		# print(matches)
		flag = 0

		for match in matches:
			# print(match.team1,match.team2, team)
			if match.team1 == team or match.team2 == team:
				dat = match.date
				print(dat.date,date)
				if date == dat.date:
					instance = match
					flag = 1
					break
		if flag:
			matches = MatchDetails.objects.filter(match_id=instance)
			print(matches)
		return Response({})