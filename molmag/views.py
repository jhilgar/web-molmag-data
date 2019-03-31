from django.views.generic.base import TemplateView
from django.views import generic
from django.shortcuts import render
from datastore.models import Compound


class AboutPageView(TemplateView):
 
	template_name = "about.html"

class SearchPageView(TemplateView):
 
	template_name = "search.html"

class DocumentationPageView(TemplateView):

	template_name = "documentation.html"
		
class MagnetListView(generic.ListView):
	model = Compound
	
class MagnetDetailView(generic.DetailView):
    model = Compound	

def index(request):
    """View function for home page of site."""
	
	# Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
	
	# Generate counts of the compounds model
    num_compounds = Compound.objects.all().count()
   
    # 0D compounds (dimensionality = '0')
    num_0d = Compound.objects.filter(dimensionality='0').count()
	
	# 1D Magnets (dimensionality = '1')
    num_1d = Compound.objects.filter(dimensionality='1').count()
	
	# 2D Magnets (dimensionality = '2')
    num_2d = Compound.objects.filter(dimensionality='2').count()
	
	# 3D Magnets (dimensionality = '3')
    num_3d = Compound.objects.filter(dimensionality='3').count()
	
	##logic for selecting 3 magnets based on the total db size, the selection only changes as the DB has more entries added.
    x1 = num_compounds
    x2 = x1 - 1
    x3 = x1 - 2

	
	
	##Featured entries

    
    context = {

		'num_magnets': num_compounds,
		'num_0d': num_0d,
		'num_1d': num_1d,
		'num_2d': num_2d,
		'num_3d': num_3d,
		'num_visits':num_visits,
		
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)