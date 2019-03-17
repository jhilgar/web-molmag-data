from django.db import models
#Create your models here.

class Dimension(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(max_length=1,
    help_text="Enter the dimensionality of the magnet (e.g. 0(molecular), linear chain(1D), etc.)"  )
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
		
class Author(models.Model):
    """Model representing an author."""
    primary_author = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)

    class Meta:
        ordering = ['primary_author', 'institution']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.primary_author, self.institution)

class Magnet(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=256)
	
    author = models.ManyToManyField(Author, help_text="Select an author for this magnet.")
    compound = models.CharField(max_length=256)
    # ManyToMany used because magnet can have more than one author, and authors can have multiple magnets
    
    Ueffective = models.CharField(max_length=12, help_text="Enter the effective barrier height in wavenumbers")
    doi = models.CharField('DOI', max_length=48,
                            help_text='DOI from the original publication')
    csdd = models.CharField('CCDC', max_length=48,
                            help_text='Cambridge Crystallographic structural database number (CCDC) from the original publication - if applicable')
							
    dimension = models.ManyToManyField(Dimension, help_text="Select a dimensionality for this magnet.")
	

   
    # Dimension class has already been defined so we can specify the object above.
    date_of_publication = models.DateField(null=True, blank=True)

    def display_dimension(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([dimension.name for dimension in self.dimension.all()[:3]])

    display_dimension.short_description = 'Dimension'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title