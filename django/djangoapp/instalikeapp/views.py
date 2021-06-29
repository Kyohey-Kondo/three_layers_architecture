# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import User, FigurePaths

from django.http import HttpResponseRedirect
from django.urls import reverse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     latest_user_list = User.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.user_name for q in latest_user_list])
#     return HttpResponse(output)

def index(request):
    latest_user_list = User.objects.order_by('-pub_date')[:10]
    context = {
        'latest_user_list': latest_user_list,
    }
    return render(request, 'instalikeapp/index.html', context)


# def mypage(request):
#     return HttpResponse("You're looking at mypage.")


# def mypage(request, user_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % user_id)


def mypage(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'instalikeapp/mypage.html', {'user': user})


def results(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'instalikeapp/results.html', {'user': user})



# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


def vote(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        selected_figurepaths = user.figurepaths_set.get(pk=request.POST['figurepaths'])
    except (KeyError, FigurePaths.DoesNotExist):
        return render(request, 'instalikeapp/mypage.html', {
            'user': user,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_figurepaths.like_point += 1
        selected_figurepaths.save()
        return HttpResponseRedirect(reverse('results', args=(user.id,)))

