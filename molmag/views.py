from django.views.generic.base import TemplateView
from django.views import generic
from django.shortcuts import render
from datastore.models import Compound, Reference
import random


class AboutPageView(TemplateView):
 
	template_name = "about.html"

class SearchPageView(TemplateView):
 
	template_name = "search.html"

class DocumentationPageView(TemplateView):

	template_name = "documentation.html"
		
class MagnetListView(generic.ListView):
	model = Compound
	paginate_by = 4
	
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
	
	##logic for selecting 3 compounds based on the total db size, the selection only changes as the DB has more entries added.
    x1 = num_compounds
    x2 = x1 + 1
    x3 = x1 + 2
    ## logic for selecting the correct reference doi from the Reference model.
    doix1 = num_compounds - 4
    doix2 = doix1 + 1 
    doix3 = doix1 + 2 
	
    imgx1 = random.randint(1,4)
    imgx2 = random.randint(1,4)
    imgx3 = random.randint(1,4)

	##Featured entries
    
    fst_feat = Compound.objects.values_list('doi', flat=True).get(pk=x1)
    fst_comp = Compound.objects.values_list('formula', flat=True).get(pk=x1)
    fst_ueff = Compound.objects.values_list('ueff', flat=True).get(pk=x1)
    fst_dim = Compound.objects.values_list('dimensionality', flat=True).get(pk=x1)
    fst_doi = Reference.objects.values_list('doi', flat=True).get(pk=doix1)
    fst_update = Compound.objects.values_list('updated_on', flat=True).get(pk=x1)
    fst_info = Compound.objects.values_list('info', flat=True).get(pk=x1)
    fst_url = fst_feat + 4
	
    snd_feat = Compound.objects.values_list('doi', flat=True).get(pk=x2)
    snd_comp = Compound.objects.values_list('formula', flat=True).get(pk=x2)
    snd_ueff = Compound.objects.values_list('ueff', flat=True).get(pk=x2)
    snd_dim = Compound.objects.values_list('dimensionality', flat=True).get(pk=x2)
    snd_doi = Reference.objects.values_list('doi', flat=True).get(pk=doix2)
    snd_update = Compound.objects.values_list('updated_on', flat=True).get(pk=x2)
    snd_info = Compound.objects.values_list('info', flat=True).get(pk=x2)
    snd_url = fst_feat + 5
	
    trd_feat = Compound.objects.values_list('doi', flat=True).get(pk=x3)
    trd_comp = Compound.objects.values_list('formula', flat=True).get(pk=x3)
    trd_ueff = Compound.objects.values_list('ueff', flat=True).get(pk=x3)
    trd_dim = Compound.objects.values_list('dimensionality', flat=True).get(pk=x3)
    trd_doi = Reference.objects.values_list('doi', flat=True).get(pk=doix3)
    trd_update = Compound.objects.values_list('updated_on', flat=True).get(pk=x3)
    trd_info = Compound.objects.values_list('info', flat=True).get(pk=x3)
    trd_url = fst_feat + 6
	

    context = {

		'num_magnets': num_compounds,
		'num_0d': num_0d,
		'num_1d': num_1d,
		'num_2d': num_2d,
		'num_3d': num_3d,
		'num_visits': num_visits,
		'imgx1': imgx1,
		'imgx2': imgx2,
		'imgx3': imgx3,
		
		
		'fst_feat': fst_feat,
		'fst_comp': fst_comp,
		'fst_ueff': fst_ueff,
		'fst_dim': fst_dim,
		'fst_doi': fst_doi,
		'fst_update': fst_update,
		'fst_info': fst_info,
		'fst_url': fst_url,
		
		'snd_feat': snd_feat,
		'snd_comp': snd_comp,
		'snd_ueff': snd_ueff,
		'snd_dim': snd_dim,
		'snd_doi': snd_doi,
		'snd_update': snd_update,
		'snd_info': snd_info,
		'snd_url': snd_url,
		
		'trd_feat': trd_feat,
		'trd_comp': trd_comp,
		'trd_ueff': trd_ueff,
		'trd_dim': trd_dim,
		'trd_doi': trd_doi,
		'trd_update': trd_update,
		'trd_info': trd_info,
		'trd_url': trd_url,
		
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)