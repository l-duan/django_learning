from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board

# Python functions that receive an HttpRequest object and returns an HttpResponse object. 

# def home(request):
# 	boards = Board.objects.all()
# 	boards_names = list()

# 	for board in boards:
# 		boards_names.append(board.name)

# 	response_html = '<br>'.join(boards_names)
# 	return HttpResponse(response_html)

def home(request):
	boards = Board.objects.all()
	return render(request, 'home.html', {'boards': boards})