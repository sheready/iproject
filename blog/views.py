from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,PostImage
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404,render,redirect
from django.db.models import Q
# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    
    return render(request,'home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    
    model = Post
    template_name = 'post_detail.html'
    
def detail_view(request,id):
    post = get_object_or_404(Post,id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request,'detail.html',{'post':post,'photos':photos})

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
   
    fields =['title','content','article_image']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields =['title','content','article_image']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('blog-home')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True


    