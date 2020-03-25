from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
	'author' : 'Soif',
	'title' : 'Blog 1',
	'content' : "First Blog post",
	'date' : "25th Mar, 2020" 
	},
	{
	'author' : 'Samar',
	'title' : 'Blog 2',
	'content' : "second Blog post",
	'date' : "26th Mar, 2020"
	}
]

def home(request):
	cont = {
		'posts' : posts
	}

	return render(request,'blog/home.html', cont)

def about(request):
	return render(request,'blog/about.html', {'title': "About"})

	
