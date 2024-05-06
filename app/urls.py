from django.urls import path
from app import views


urlpatterns = [
    path('portfolio/',views.home_view,name='portfolio'),
    path('education/',views.education_view,name= 'education'),
    path('skils/',views.skils_view,name='skils'),
    path('project/',views.project_view,name='project'),
    path('detials/',views.details_view,name='details'),
    path('contact/',views.contact_view,name='contact'),
]