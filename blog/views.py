from django.shortcuts import render

posts = [
    {
        'authon': 'Berg',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'October 30, 2019'
    },
    {
        'authon': 'Jhon Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'October 31, 2019'
    },
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
      return render(request, 'blog/about.html', {'title':'About'})



