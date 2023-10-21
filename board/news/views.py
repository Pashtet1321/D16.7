from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views import View
from .models import Article


def categories(request, catid):
    return HttpResponse(f"<h1> Статьи по категориям</h1><p>{catid}</p>")


def index(request):
    return render(request, 'news/index.html', )


def portal(request):
    news = Article.objects.all()
    return render(request, 'news/portal.html', {'news': news})


def create(request):
    return render(request, 'news/create.html')


class RegisterUser(DetailView, CreateView):
    form_class = UserCreationForm
    template_name = 'news/register.html'
    success_url = reverse_lazy('')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


@permission_required('polls.add_choice', raise_exception=True)
@login_required
def my_view(request):

    class MyView(LoginRequiredMixin, View):
        login_url = '/login/'


