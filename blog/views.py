from django.shortcuts import render

posts = [
  {
    'author': 'David Tee',
    'title': 'Blog Post 1',
    'content': 'First post comment',
    'date_posted': 'August 27, 2021'
  },
    {
    'author': 'David Tee 2',
    'title': 'Blog Post 2',
    'content': 'Second post comment',
    'date_posted': 'September 10, 2021'
  },
    {
    'author': 'David Tee 3',
    'title': 'Blog Post 3',
    'content': 'Third post comment',
    'date_posted': 'Dec 25, 2021'
  },
]

# Create your views here.
def home(request):
  context = {
    'posts': posts
  }

  return render(request, 'blog/home.html', context)


def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})