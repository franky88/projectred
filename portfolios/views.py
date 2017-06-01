from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Portfolio, Category
from .forms import PortfolioForm
# Create your views here.
def portfolioIndex(request):
	cat_list = Category.objects.all()
	# counter = Category.objects.values("portfolio").annotate(Count("id"))
	portfolio_list = Portfolio.objects.order_by('-timestamp', '-updated')
	# portfolio_count = len(counter)
	context = {
		"title": "portfolio list",
		"portfoliolist": portfolio_list,
		"catlist": cat_list,
		# "portcount": portfolio_count,
	}
	return render(request, "portfolio/portfolio_index.html", context)

def portfolioCatDetail(request, pk):
	cat_list = Category.objects.all()
	instance = get_object_or_404(Category, pk=pk)
	context = {
		"title": "categories",
		'instance': instance,
		"catlist": cat_list,
	}
	return render(request, "portfolio/portfolio_catdetail.html", context)

def portfolioDetail(request, slug=None):
	instance = get_object_or_404(Portfolio, slug=slug)
	context = {
		"title": "Portfolio Informations",
		"instance": instance,
	}
	return render(request, "portfolio/portfolio_detail.html", context)

@login_required
def addPortfolio(request):
	if not request.user.is_authenticated():
		raise Http404

	if request.method == 'POST':
		form = PortfolioForm(
			request.POST or None, 
			request.FILES or None,
			)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('portfolio:detail', pk=instance.pk)
	else:
		form = PortfolioForm()
	context = {
		"form": form,
		"title": "Add Portfolio",
	}
	return render(request, "portfolio/add_portfolio.html", context)