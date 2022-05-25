from . import views
from django.urls import path , include
from .views import GeneratePdf


urlpatterns = [
   path('',views.home, name='home'),
   path('signup',views.signup, name='signup'),
   path('login',views.login, name='login'),
   path('logout',views.logout, name='logout'),
   path('export_data_to_excel', views.export_data_to_excel, name='export_data_to_excel' ),
   # path('list', views.resume_list, name='resume_list'),
   path('resume/upload', views.upload_resume, name='resume_upload'),
   path('resume', views.resume, name= 'resume'),
   path('pdf',GeneratePdf.as_view()),
   path('back',views.back,name='back'),
   path('apply',views.apply,name='apply'),

   # path('view',views.show_file, name='view'),
   # path('upload',views.resume_upload,name='upload')
]