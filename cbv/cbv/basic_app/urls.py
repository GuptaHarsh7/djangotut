from django.urls import path,re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('<pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('<pk>/update/',views.SchoolUpdateView.as_view(),name='update'),
    path('<pk>/delete/',views.SchoolDeleteView.as_view(),name='update'),
]
# re_path is used to check for regex in path