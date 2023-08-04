from django.urls import path, include

from . import views

app_name = 'api'
urlpatterns = [
    path('doctor/', include([
        path('', views.DoctorCreateView.as_view()),
        path('list/', views.DoctorListView.as_view()),
        path('<int:pk>/', views.DoctorRetrieveUpdateDestroyView.as_view()),
    ])),
    path('patient/', include([
        path('', views.PatientCreateView.as_view()),
        path('list/', views.PatientListView.as_view()),
        path('<int:pk>/', views.PatientRetrieveUpdateDestroyView.as_view()),
    ])),
    path('exercise/', include([
        path('', views.ExerciseCreateView.as_view()),
        path('list/', views.ExerciseListView.as_view()),
        path('<int:pk>/', views.ExerciseRetrieveUpdateDestroyView.as_view()),

        path('assigned/', include([
            path('', views.AssignedExerciseCreateView.as_view()),
            path('list/', views.AssignedExerciseListView.as_view()),
            path('<int:pk>/', views.AssignedExerciseRetrieveUpdateDestroyView.as_view()),
        ]))
    ])),
]
