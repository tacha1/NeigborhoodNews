from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .email import send_welcome_email
from .models import NewsLetterRecipients,Profile,Neighborhood,Business,Post
from .forms import NewProfileForm,NewNeighborhoodForm,NewBusinessForm,NewPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    all_hoods = Neighborhood.objects.all()
    return render(request, 'welcome.html', {"all_hoods": all_hoods})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')

    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def my_profile(request):

    current_user = request.user
    # my_projects = Project.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', { "my_profile":my_profile})

@login_required(login_url='/accounts/login/')
def add_neighborhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
        return redirect('welcome')

    else:
        form = NewNeighborhoodForm()
    return render(request, 'add_hood.html', {"form": form})


@login_required(login_url='/accounts/login/')
def neighborhood(request,id):
    # hoods = Neighborhood.filter_neighborhood_by_id(id)
    posts = Post.filter_post_by_id(id)
    busines = Business.filter_business_by_id(id)
    return render(request,'business.html', {"busines":busines,"posts":posts})

@login_required(login_url='/accounts/login/')
def add_business(request,id):
    current_user = request.user
    hoods = Neighborhood.filter_neighborhood_by_id(id = id).first()
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.neighborhood = hoods
            hood.save()
            return redirect('hood',id)

    else:
        form = NewBusinessForm()
    return render(request, 'add_business.html', {"form": form,"id":id})


@login_required(login_url='/accounts/login/')
def add_post(request,id):
    current_user = request.user
    hoods = Neighborhood.filter_neighborhood_by_id(id = id).first()
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.neighborhood = hoods
            hood.save()
            return redirect('hood',id)

    else:
        form = NewPostForm()
    return render(request, 'add_post.html', {"form": form,"id":id})


def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'Your account has been successfully created'}
    return JsonResponse(data)

# @login_required(login_url='/accounts/login/')
def search_business(request):
    if 'busines' in request.GET and request.GET["busines"]:
        search_term = request.GET.get("busines")
        searched_busines = Business.search_by_business_name(search_term)
        message = f"{search_term}"
        return render(request, "search.html",{"message":message,"businesses": searched_busines})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})