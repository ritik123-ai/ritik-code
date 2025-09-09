from rest_framework import serializers
from service.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model =Employee
        fields = "__all__"


    def validate_salary(self,value):
        if value < 20000:
            raise serializers.ValidationError("salary at least 20000")
        return value
    
    def validate_designation(self,value):
        allow_designation =["developer","HR"]
        if value not in allow_designation:
            raise serializers.ValidationError(f"Department from this only")
        return value







    


    

    
    
    