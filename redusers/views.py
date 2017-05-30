from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
def portfolioUser(request):
	user = User.objects.all()
	context = {
		"title": "profiles",
		"user": user,
	}
	return render(request, "reduser/reduser_user.html", context)

def portfolioUserDetail(request, pk):
	instance = get_object_or_404(User, pk=pk)
	context = {
		"title": "my portfolios",
		"instance": instance,
	}
	return render(request, "reduser/reduser_userdetail.html", context)