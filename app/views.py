from rest_framework.response import Response
from .serializers import *
from . models import *
from django.db.models import Count
from rest_framework.views import APIView
from django.db import transaction


class ListOfStudentAPIView(APIView):
    def get(self,request,classroom_name=None):
        if classroom_name:
            obj = Student.objects.filter(classroom__name=classroom_name)
        else:
            obj = Student.objects.all()

        Serializer=StudenSerializer(obj,many=True)
        return Response(Serializer.data)

    def post(self,request):
        data=request.data
        Serializer=StudenSerializer(data=data)

        if Serializer.is_valid():

            inst=Serializer.save()   

            classroom_id=Serializer.validated_data.get('classroom')
            seat_id=Serializer.validated_data.get('seat_id')

            SeatAllocation.objects.create(
                student=inst,
                seat_id=seat_id,
                classroom=classroom_id,
                start_date=timezone.now().date()
            )


            return Response({'SUCCESS':'YOUR DATA IS SAVED..'})
        else:
            return Response(Serializer.errors)

class ClassListAPIView(APIView):
    def get(self,request):
        #take what you want to as query_params
        x=request.query_params.get('x',0)

        try:
            x=int(x)
        except ValueError:
            return Response({"error":"something went wrong.."})
        
        classrooms = Classroom.objects.annotate(student_count=Count('students')).filter(student_count__gte=x)

        serializer=ClassRoomSerializer(classrooms,many=True)

        return Response(serializer.data)
    

class ChangeRoomAPIView(APIView):
    @transaction.atomic
    def put(self, request):
        serializer = ChangeRoomSerializer(data=request.data)
        if serializer.is_valid():
            student_name = serializer.validated_data.get('student_name')
            new_classroom = serializer.validated_data.get('new_classroom')
            new_seat = serializer.validated_data.get('new_seat')

            student = Student.objects.filter(name=student_name).first()
            if not student:
                return Response({'error': 'Student does not exist.'})

            # Update student details
            student.classroom = new_classroom
            student.seat_id = new_seat
            student.save()
            # st=serializer.save()allocation history
          
            return Response({'message': 'Student room updated successfully.'})

        return Response(serializer.errors)

class SeatAllocationAPIView(APIView):
    def get(self, request):
        allocations = SeatAllocation.objects.all()
        serializer = StudentSeatAllocationHistory(allocations, many=True)
        return Response(serializer.data)
    

#  =====================FOR UNDERSTANT WHAT IS HAPPING IN ABOVE LINE =================================================
        # now take the class and where you want to record that count and use (annotate) :-
#         BatchModel.objects.annotate(student_count=Count('students')):
        
        # student is a related name of the field

# Here, the annotate() method is adding a new field called student_count to each BatchModel instance.
# The value of student_count is the result of counting the number of related students for each batch. This is done using the Count function, which counts the number of related students for each BatchModel.
# .filter(student_count__gte=x):

# After the annotation, the queryset is filtered to only include batches (or classrooms) where the student_count is greater than or equal to the value of x (which defaults to 15 unless specified in the query parameters).
# ====================================================================================================================
    # http......./
# def get(self,request,pk=None):
#         if pk is None:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu, many=True) 
#             return Response(serializer.data)
#         else:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)