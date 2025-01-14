"""
URL configuration for theProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('project/',views.project),
    path('service/',views.service),
    path('content_details/<cid>/',views.content_details,name="content_details"),
    # path('project_info/<pid>/',views.project_info,name='project_info'),
    path('download/<int:project_id>/', views.project_folder, name='project_folder'),
    path('team/',views.team),
    path('feature/',views.feature),
    path('testimonial/',views.testimonial),
    # path('service_info/<sid>/',views.service_info),
    path('services_folder/<int:service_id>/', views.service_folder, name='service_folder'),
    path('quote/',views.quote),
    path('initiate_payment/<int:pid>/',views.initiate_payment,name="initiate_payment"),
    # path('initiate_payment_services/<int:pid>/',views.initiate_payment_services,name="initiate_payment_services"),
    path('payments/',views.payment,name="payments"),
    path('cart/<pid>',views.cart),
    path('remove/<rid>',views.remove),
    path('updateqty/<x>/<uid>/',views.updateqty),

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)