from import_export import resources

from accounts.models import Data


class dataResource(resources.ModelResource):
    class Meta:
        model = Data
