from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse

# Create your models here.
def upload_location(instance, filename):
	return "%s/%s"%(instance.id, filename)
class Category(models.Model):
	class Meta:
		verbose_name_plural = "categories"
	cat_name = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.cat_name

class Portfolio(models.Model):
	slug = models.SlugField(unique=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	cat = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	art_name = models.CharField(max_length=120, help_text='Required. 120 characters or fewer. Letters, digits, numbers and @/./+/-/_ only.',)
	short_des = models.TextField(null=True, blank=True, verbose_name="short description")
	like = models.IntegerField(default=0)
	tags = models.IntegerField(default=0)
	image = models.ImageField(upload_to=upload_location)
	comments = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def get_absolute_url(self):
		return reverse("portfolio:detail", kwargs={"id": self.id})

	def portfolio_name(self):
		portname = "%s by: %s"%(self.art_name, self.user)
		return portname

	def __str__(self):
		return self.portfolio_name()

def create_slug(instance, new_slug=None):
	slug = slugify(instance.art_name)
	if new_slug is not None:
		slug = new_slug
	qs = Portfolio.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_portfolio_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_portfolio_receiver, sender=Portfolio)