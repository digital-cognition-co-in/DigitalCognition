from django.contrib import admin
from django.urls import path , include
from django.conf.urls import include, url

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

#from dc_dash.views import *   ## App Name and Views.py -- Chained Call 
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('trader/', include('pyfintrader.urls')), # pyfintrader.urls
    #path('analytics/', include('dc_dash.urls')),
    path('dc/', include('dc_dash.urls')), # Trying to save rework -- as lots of URL's already with Prefix - DC 
    #BELOW-- Create own Login - get emails for Password Reset etc WITHOUT== ADMIN Approval - #registration.backends.admin_approval.urls
    #url(r'^corp_user_accounts/', include('registration.backends.default.urls')),
    #BELOW-- Create own Login - get emails for Password Reset etc WITH == ADMIN Approval- #registration.backends.admin_approval.urls
    url(r'^admin_approved_accounts/', include('registration.backends.admin_approval.urls')),
    ### Above == /home/dhankar/anaconda2/envs/dc_info_venv/lib/python3.5/site-packages/registration/backends/admin_approval/urls.py
    ### Above == https://django-registration-redux.readthedocs.io/en/latest/quickstart.html#setting-up-urls
]

## Commented Out == 20_SEP_19
if settings.DEBUG: ## IF DEBUG == TRUE , in the settings.py File --- then ADD the below URL Patterns , the urlpatterns += IS ADDING TO THE Python LIST URL PATTERNS
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)










## SOURCE == SO == https://stackoverflow.com/a/39907426/4928635
# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    
