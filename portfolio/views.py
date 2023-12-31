from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Post, Project, Course
from .forms import PostForm

# Create your views here.

def home_page_view(request):
    return render(request, "portfolio/Main.html")

def menu_view(request):
    return render(request, "portfolio/Menu.html")

def about_me(request):
    return render(request, "portfolio/AboutMe.html")

def animations_view(request):
    return render(request, "portfolio/animations.html")

def beach_view(request):
    return render(request, "portfolio/beach.html")

def calculadora_view(request):
    return render(request, "portfolio/Calculadora.html")

def html5_css_view(request):
    return render(request, "portfolio/html5-css.html")

def imagemReponsiva_view(request):
    return render(request, "portfolio/imagemReponsiva.html")

def index_lab2_view(request):
    return render(request, "portfolio/indexlab2.html")

def index_lab4_view(request):
    return render(request, "portfolio/indexlab4.html")

def info_view(request):
    return render(request, "portfolio/info.html")

def LEI_view(request):
    return render(request, "portfolio/LEI.html")

def Licenciatura_view(request):
    return render(request, "portfolio/Licenciatura.html")

def local_view(request):
    return render(request, "portfolio/local.html")

def multimedia_view(request):
    return render(request, "portfolio/multimedia.html")

def parallax_view(request):
    return render(request, "portfolio/parallax.html")

def quizz_view(request):
    return render(request, "portfolio/quizz.html")

def tourveneza_view(request):
    return render(request, "portfolio/tourVeneza.html")

def diagram_view(request):
    return render(request, "portfolio/diagram.html")

def tecnologias_view(request):
    return render(request, "portfolio/tecnologias.html")

def contacts_view(request):
    return render(request, "portfolio/contacts.html")

def video_view(request):
    return render(request, "portfolio/video.html")

def blog_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)

def nova_page_view(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:posts')

    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)

def editar_blog_view(request, post_id):

    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:posts'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)

def apaga_blog_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:posts'))



def project_view(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'portfolio/project.html', context)


def course_view(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'portfolio/courseLEI.html', context)
