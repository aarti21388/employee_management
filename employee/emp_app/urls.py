from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('all_emp/',views.all_emp),
    path('remove_emp/',views.remove_emp),
    path('remove_emp/<int:emp_id>/',views.remove_emp),
    path('add_emp/',views.add_emp),
    path('filter_emp/',views.filter_emp),
    path('update_emp/',views.update_emp),
    path('update_emp/<int:id>/',views.update_emp),
]