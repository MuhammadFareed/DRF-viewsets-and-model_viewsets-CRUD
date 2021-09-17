from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentViewSet(viewsets.ViewSet):
    # def list(self, request):
    #     students = Student.objects.all()
    #     serialized_data = StudentSerializer(students, many=True)
    #     return Response(serialized_data.data)

    # def retrieve(self, request, pk=None):
    #     if pk is not None:
    #         student = Student.objects.get(id=pk)
    #         serialized_data = StudentSerializer(student, many=True)
    #         return Response(serialized_data.data)

    # def create(self, request):
    #     serialized_data = StudentSerializer(data=request.data)
    #     if serialized_data.is_valid():
    #         serialized_data.save()
    #         return Response({'messsage': 'Data created!'}, status.HTTP_201_CREATED)
    #     return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk):
    #     student = Student.objects.get(id=pk)
    #     serialized_data = StudentSerializer(student, data=request.data)
    #     if serialized_data.is_valid():
    #         serialized_data.save()
    #         return Response({'messsage': 'Data Updated Completely!'})
    #     return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk=None):
    #     student = Student.objects.get(id=pk)
    #     serialized_data = StudentSerializer(student, data=request.data, partial=True)
    #     if serialized_data.is_valid():
    #         serialized_data.save()
    #         return Response({'messsage': 'Data Updated Partially!'})
    #     return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # def destroy(self, request, pk=None):
    #     student = Student.objects.get(id=pk)
    #     student.delete()
    #     return Response({'message': 'Data deleted!'}, status=status.HTTP_202_ACCEPTED)