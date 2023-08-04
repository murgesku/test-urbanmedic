from rest_framework import serializers

from .models import *


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    period = serializers.ListSerializer(child=serializers.IntegerField(min_value=0, max_value=1), allow_empty=False,
                                        min_length=7, max_length=7)

    class Meta:
        model = Exercise
        fields = '__all__'


class AssignedExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)
    exercise_period = serializers.ListField(child=serializers.IntegerField(), source='exercise.period', read_only=True)

    class Meta:
        model = AssignedExercise
        fields = '__all__'

    def validate(self, data):
        exercise = data['exercise']
        if not exercise.allowed_doctors.filter(pk=data['doctor'].id).exists():
            raise serializers.ValidationError('Not allowed doctor')
        return super().validate(data)


__all__ = ('DoctorSerializer', 'PatientSerializer', 'ExerciseSerializer', 'AssignedExerciseSerializer')
