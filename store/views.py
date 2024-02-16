from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.utils.decorators import method_decorator


from .models import CharityItem

# Create your views here.

# temp data for testing

def index(req):

    return render(req, 'store/index.html')

def about(req):

    return render(req, 'store/about.html', {"title" : "about page"})

class StoreListView(ListView):
    model = CharityItem
    template_name = 'store/store.html'
    context_object_name = 'charities'
    ordering = ['-upload_date']
    paginate_by = 2


class StoreDetailView(DetailView):
    model = CharityItem
    template_name = 'store/video_detail.html'


