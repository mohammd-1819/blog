from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from blog.models import Post
from home.forms import ContactUsForm
from home.models import ContactUsMessage


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')[:4]
        last_posts = Post.objects.all().order_by('-created_at')[:3]
        return render(request, 'home/home.html', {'posts': posts, 'last_posts': last_posts})


class AboutUsView(TemplateView):
    template_name = 'home/about.html'


class ContactUsView(FormView):
    template_name = 'home/contact.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form_data = form.cleaned_data
        ContactUsMessage.objects.create(**form_data)

        return super().form_valid(form)



