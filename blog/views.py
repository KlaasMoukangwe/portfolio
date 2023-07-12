from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# class PostCreateView(CreateView):
#     model = Post
#     template_name = 'post_form.html'
#     fields = ['title', 'content', 'category', 'tags', 'featured_image']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         messages.success(self.request, 'Post created successfully!')
#         return super().form_valid(form)

# class PostUpdateView(UpdateView):
#     model = Post
#     template_name = 'post_form.html'
#     fields = ['title', 'content', 'category', 'tags', 'featured_image']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         messages.success(self.request, 'Post updated successfully!')
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         return self.request.user == post.author

# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'post_confirm_delete.html'
#     success_url = reverse_lazy('post-list')

#     def delete(self, request, *args, **kwargs):
#         messages.success(request, 'Post deleted successfully!')
#         return super().delete(request, *args, **kwargs)

#     def test_func(self):
#         post = self.get_object()
#         return self.request.user == post.author or self.request.user.is_superuser
