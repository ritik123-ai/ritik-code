from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from service.models import Employee
from service.serializer.employee_serializer import EmployeeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination



class EmployeePagination(PageNumberPagination):
    page_size = 5  
    page_size_query_param = 10
    max_page_size = 50




        
class EmployeeAPIView(APIView):
    def get(self, request,pk):
        try:
            employees = Employee.objects.pk(pk=pk)
            paginator = EmployeePagination()
            paginated_employees = paginator.paginate_queryset(employees, request)
            serializer = EmployeeSerializer(paginated_employees, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



    def post(self,request):
        #emp_id = request.data.get("emp_id")
        #department= request.data.get("department")
        serializer = EmployeeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({
                "message":"employee add successfully",

            },
            status=status.HTTP_201_CREATED
        )


    def put(self,request,pk):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self,request,pk):
        employee = get_object_or_404(Employee,pk=pk)
        employee.delete()
        return Response({"message":"Employee delete successfully"},status=status.HTTP_204_NO_CONTENT)
            

