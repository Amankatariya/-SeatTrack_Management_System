from django.db import models
from django.utils import timezone
class AbstractTime(models.Model):
    created_at=models.DateTimeField("Created_Date", auto_now_add=True)
    updated_at=models.DateTimeField("Updated_Date", auto_now=True)

    class Meta:
        abstract=True


class Seat(AbstractTime):
    seat_no=models.IntegerField()

    def __str__(self):
        return f"{self.seat_no}"
    
class Classroom(AbstractTime):
    name=models.CharField(max_length=100)    

    def __str__(self):
        return self.name

class Student(AbstractTime):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    #did student count for that it is here...onetomany() and manytoone
    classroom=models.ForeignKey(Classroom,related_name='students',on_delete=models.CASCADE) #this-<
    seat_id=models.ForeignKey(Seat,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class SeatAllocation(AbstractTime):
    student=models.ForeignKey(Student,related_name='seat_history',on_delete=models.CASCADE)
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    seat_id=models.ForeignKey(Seat,on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
#  1
    # class Meta:
    #     unique_together = ('student', 'seat_id')
        
    def __str__(self):
        return str(self.start_date)
    

