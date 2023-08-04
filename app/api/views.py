from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import views, generics
from rest_framework.filters import SearchFilter

from .models import *
from .serializers import *
from .filters import AssignedExerciseFilter


class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientCreateView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ExerciseCreateView(generics.CreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseListView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class AssignedExerciseCreateView(generics.CreateAPIView):
    queryset = AssignedExercise.objects.all()
    serializer_class = AssignedExerciseSerializer


class AssignedExerciseListView(generics.ListAPIView):
    queryset = AssignedExercise.objects.all()
    serializer_class = AssignedExerciseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AssignedExerciseFilter
    filterset_fields = ['doctor', 'patient', 'date']


class AssignedExerciseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignedExercise.objects.all()
    serializer_class = AssignedExerciseSerializer
