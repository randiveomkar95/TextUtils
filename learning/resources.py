from import_export import resources
from .models import Son

class SonResource(resources.ModelResource):
    class Meta:
        model = Son
