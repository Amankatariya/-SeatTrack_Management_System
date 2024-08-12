from rest_framework import serializers
from .models import *

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seat
        fields='__all__'

class StudenSerializer(serializers.ModelSerializer):
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
    seat_id = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all())
    # student=serializers.CharField(max_length=100)

    classroom_name=serializers.PrimaryKeyRelatedField(source='classroom.name',read_only=True)
    # seat_no = serializers.SerializerMethodField()

    class Meta:
        model=Student
        fields=['name','email','classroom_name','seat_id','classroom','seat_id']

    def get_seat_id(self,obj):
        return obj.seat_id.seat_no

class ClassRoomSerializer(serializers.ModelSerializer):
    student_count = serializers.IntegerField(read_only=True)

    class Meta:
        model=Classroom
        fields=['name','student_count']
# ==========================================================================================================
# class ChangeRoomSerializer(serializers.Serializer):
#     new_classroom_id = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
#     student_name = serializers.CharField(max_length=100)
#     new_seat_id = serializers.IntegerField()

#     class Meta:
#         fields = ['student_name', 'new_classroom_id','new_seat_id']

#     def validate_student_name(self, value):
#         obj=Student.objects.filter(name=value).exists()
#         if obj:
#             return value
#         else:
#             raise serializers.ValidationError("class Does not Exists..")
                        # =========== OR =========
class ChangeRoomSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=100)
    new_classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
    new_seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all())

    class Meta:

        fields = ['student_name', 'new_classroom', 'new_seat']

    def validate(self, obj):
        student_name = obj.get('student_name')
        new_classroom = obj.get('new_classroom')
        new_seat = obj.get('new_seat')

        if  Student.objects.filter(name=student_name).exists():

            student_instance = Student.objects.get(name=student_name)
            
            SeatAllocation.objects.create(
                student=student_instance,
                seat_id=new_seat,
                classroom=new_classroom,
                start_date=timezone.now().date()
            )
            return obj
        else:
            raise serializers.ValidationError("This Student Not Exists..")
# =================================================================================================================


class StudentSeatAllocationHistory(serializers.ModelSerializer):
    student =serializers.PrimaryKeyRelatedField(source='student.name',read_only=True)
    classroom =serializers.PrimaryKeyRelatedField(source='classroom.name',read_only=True)
    class Meta:
        model=SeatAllocation
        fields=['student','classroom','seat_id','start_date']

