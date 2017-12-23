"""
Root URLs for project.
"""
import warnings

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from apps.PubSite import urls as public_urls
from apps.Secure import urls as secure_urls
from apps.UserInfo import urls as userinfo_urls


admin.autodiscover()

# Turns deprecation warnings into errors
warnings.simplefilter('error', DeprecationWarning)

urlpatterns = [
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(
        regex=r'^demo/admin/',
        view=admin.site.urls,
    ),
    url(
        regex=r'^demo/brothers/',
        view=include(userinfo_urls),
    ),
    url(
        regex=r'^demo/users/',
        view=include(userinfo_urls),
    ),
    url(
        regex=r'^demo/secure/',
        view=include(secure_urls),
    ),
    url(
        regex=r'^demo/',
        view=include(public_urls),
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
