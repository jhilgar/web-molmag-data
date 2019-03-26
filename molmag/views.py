from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
 
	template_name = "about.html"

class SearchPageView(TemplateView):
 
	template_name = "search.html"


class DocumentationPageView(TemplateView):

	template_name = "documentation.html"