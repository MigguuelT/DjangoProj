# pessoas/urls.py

from rest_framework import routers
from .views import PessoaViewSet

router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet)

urlpatterns = router.urls # Isso inclui as URLs geradas pelo router (ex: /api/pessoas/, /api/pessoas/<id>/)
