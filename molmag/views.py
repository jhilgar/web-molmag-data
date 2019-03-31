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
	
	# Generate counts of some of the main objects
    num_compounds = Compound.objects.all().count()

	
	
	##Featured entries

    
    context = {

		'num_visits':num_visits,
		'num_compounds':num_compounds,
		
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)