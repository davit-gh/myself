from main.models import IconBlurb
from main.models import PortfolioItemCategory
from mezzanine.pages.models import Page
from mezzanine.forms.models import Form
from django.template import RequestContext
from main.forms import ContactusForm

from mezzanine import template
register = template.Library()

@register.as_tag
def get_iconblurbs(*args):
	blurbs = IconBlurb.objects.all()
	return blurbs

@register.as_tag
def get_work_portitem(*args):
	work_portitem = PortfolioItemCategory.objects.get(slug='work').portfolioitems.all()[0]
	return work_portitem

@register.as_tag
def get_project_portitem(*args):
	project_portitem = PortfolioItemCategory.objects.get(slug='projects').portfolioitems.all()[0]
	return project_portitem

@register.as_tag
def get_about(*args):
	about_page = Page.objects.get(slug="about")
	return about_page
import pdb
@register.as_tag
def get_contact_form(*args):
	return ContactusForm()
