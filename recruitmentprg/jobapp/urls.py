from django.urls import path
from jobapp import views
from jobapp.views import CompanyView,CompanyList,UserView,UserList,JobView,JobList

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('company/',CompanyView.as_view()),
    path('display/',CompanyList.as_view()),
    path('user/',UserView.as_view()),
    path('dis/',UserList.as_view()),
    path('status/',views.ch),
    path('log/',views.login),
    path('postjob/',JobView.as_view()),
    path('viewjob/',JobList.as_view()),
    path('edituser/',views.edituser),
    path('updateuser/',views.updateuser),
    path('updatestatus/<int:id>/',views.updatestatus),
    path('deletestatus/<int:id>/',views.deletestatus),
    path('editcmp/',views.editcmp),
    path('updatecmp/',views.updatecmp),
    path('editadmin/', views.editadmin),
    path('updateadmin/', views.updateadmin),
    path('postnewjob/',views.postnewjob),
    path('apply/<int:id>/',views.apply),
    path('appliedlist/',views.appliedjob),
    path('deleteapplication/<int:id>/',views.deleteappliedjob),
    path('viewpostedjobs/',views.viewpostedjobs),
    path('viewapplicants/',views.viewapplicants),
    path('viewappli/<int:id>',views.viewjobseekers),
    path('viewprofile/<int:id>/',views.userprofile),
    path('select/<int:id>/',views.selectuser),
    path('deletepost/<int:id>/',views.deletejob),

]