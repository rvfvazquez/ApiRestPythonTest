"""
Definition of urls for ApiRestPythonTest.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from rest_framework_swagger.views import get_swagger_view


from api.api import FeiraLivreResource

feiralivre_resource = FeiraLivreResource()


schema_view = get_swagger_view(title='API Feiras Livres')

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = [
    # Examples:
    url(r'^api/', include(feiralivre_resource.urls)),
    url(r'^swagger$', schema_view) , 
    
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # url(r'^api/', include(api.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

"""
from rest_framework import routers

from api.views import FeiraLivreViewSet
router = routers.DefaultRouter()

router.register(r'feiraslivres', FeiraLivreViewSet)

urlpatterns += router.urls
"""

"""
from rest_framework import routers

from api.views import FeiraLivreViewSet
router = routers.SimpleRouter()

router.register(r'feiraslivres', FeiraLivreViewSet)

urlpatterns += router.urls

"""