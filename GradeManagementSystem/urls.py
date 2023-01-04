from django.urls import re_path
from django.contrib import admin
from gms.views import log_in,log_out,authenticated,course,addexam,setcriteria,update_exam

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/$',log_in,name='log_in'),
    re_path(r'^$',log_in,name='log_in'),
    re_path(r'^logout/$',log_out,name='log_out'),
    re_path(r'^authenticated/$',authenticated,name='authenticated'),
    re_path(r'^authenticated/(?P<course_no>[0-9]+)/$',course,name='course'),
    re_path(r'^authenticated/(?P<course_no>[0-9]+)/addexam/$',addexam,name='addexam'),
    re_path(r'^authenticated/(?P<course_no>[0-9]+)/setcriteria/$',setcriteria,name='setcriteria'),
    re_path(r'^authenticated/(?P<course_no>[0-9]+)/(?P<exam_no>[0-9]+)/$',update_exam,name='update_exam'),
]
