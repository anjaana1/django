from django.db import models


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=10)
    doc = models.DateTimeField()
    dom = models.DateTimeField()
    state_status = models.CharField(max_length=10,choices=(('1','active'),('0','inactive')))


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    city_code = models.CharField(max_length=10)
    state_id = models.ForeignKey(State,on_delete=models.CASCADE)
    doc = models.DateTimeField()
    dom = models.DateTimeField()
    city_status = models.CharField(max_length=10,choices=(('1','active'),('0','inactive')))


class Center(models.Model):
    center_id = models.AutoField(primary_key=True)
    center_name = models.CharField(max_length=100)
    center_code = models.CharField(max_length=10)
    city_id = models.ForeignKey(City,on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.TextField()
    doc = models.DateTimeField()
    dom = models.DateTimeField()
    desc = models.TextField()
    center_status = models.CharField(max_length=10,choices=(('1','active'),('0','inactive')))


class Block(models.Model):
    block_id = models.AutoField(primary_key=True)
    center_id = models.ForeignKey(Center,on_delete=models.CASCADE)
    block_name = models.CharField(max_length=100)
    block_code = models.CharField(max_length=10)
    doc = models.DateTimeField()
    dom = models.DateTimeField()
    block_status = models.CharField(max_length=10,choices=(('1','active'),('0','inactive')))


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    center_id = models.ForeignKey(Center,on_delete=models.CASCADE)
    room_code = models.CharField(max_length=10)
    block_name = models.ForeignKey(Block, on_delete=models.CASCADE)
    floor_no = models.CharField(max_length=10,choices=(('0','Ground Floor'),('1','First Floor'),('2','Second Floor'),('3','Third Floor')))
    capacity = models.IntegerField()
    doc = models.DateTimeField()
    dom = models.DateTimeField()
    room_status = models.CharField(max_length=10,choices=(('1','active'),('0','inactive')))


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    center = models.ForeignKey(Center,on_delete=models.CASCADE)
    doc = models.DateTimeField()
    dom = models.DateTimeField()
    course_status = models.CharField(max_length=10,choices=(('1','active'),('0','inactive')))


class Department(models.Model):
    dep_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=100)
    dep_code = models.CharField(max_length=10,null=True)
    doc = models.DateTimeField()
    dom = models.DateTimeField()
    dep_status = models.CharField(max_length=10,choices=(('1','active'),('0','inactive')))


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    registration_number = models.IntegerField()
    student_name = models.CharField(max_length=200)
    student_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    doc = models.DateTimeField()


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    doc = models.DateTimeField()
    teacher_status = models.CharField(max_length=10,choices=(('1','active'),('0','inactive')))


class SeatingArrangement(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE)
    center_id = models.ForeignKey(Center,on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
