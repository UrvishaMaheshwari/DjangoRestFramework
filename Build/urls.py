from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer, NBCFSerializer, TrainingProviderSerializer, LoanApplicationSerializer, StudentProgressSerializer # type: ignore
from .models import Student, NBFC, TrainingProvider, LoanApplication, StudentProgress # type: ignore

class StudentView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NBFCView(APIView):
    def post(self, request):
        serializer = NBCFSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainingProviderView(APIView):
    def post(self, request):
        serializer = TrainingProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanApplicationView(APIView):
    def post(self, request):
        serializer = LoanApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentProgressView(APIView):
    def post(self, request):
        serializer = StudentProgressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
