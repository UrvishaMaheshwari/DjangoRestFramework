from rest_framework import serializers
from .models import Student, NBFC, TrainingProvider, LoanApplication, StudentProgress

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class NBCFSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBFC
        fields = '__all__'

class TrainingProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingProvider
        fields = '__all__'

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = '__all__'

class StudentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgress
        fields = '__all__'
