from django.db import models

class Student(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class NBFC(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class TrainingProvider(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class LoanApplication(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    nbfc = models.ForeignKey(NBFC, on_delete=models.CASCADE)
    training_provider = models.ForeignKey(TrainingProvider, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=['approved', 'rejected', 'pending'])
    created_at = models.DateTimeField(auto_now_add=True)

class StudentProgress(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    training_provider = models.ForeignKey(TrainingProvider, on_delete=models.CASCADE)
    progress = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
