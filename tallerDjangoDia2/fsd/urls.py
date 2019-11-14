from django.urls import path
from django.contrib import admin
from university.views import vistaSimple, misDepartamentos

urlpatterns = [
    # Examples:
    # url(r'^$', 'fsd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('vistaSimple/<int:pk>', vistaSimple, name="miVistaSimple"),
    path('misDepartamentos', misDepartamentos, name="misDepartamentos"),
]
