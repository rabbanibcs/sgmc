from django.db import models
from department.models import Department

exams = (('HY', 'Half Yearly'), ('Y', 'Yearly'),
         ('PT', 'Pre Test'), ('T', 'Test'), ('O', 'Others'))


class Examination(models.Model):
    year = models.PositiveIntegerField()
    term = models.CharField(choices=exams, max_length=2)
    session = models.CharField(max_length=9)
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        unique_together = ['year', 'term']
        
    def __str__(self):
        return str(self.year) + '_' + self.term

class Grade(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.DO_NOTHING)
    session = models.CharField(max_length=9)
    subject = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    roll = models.PositiveIntegerField(null=True)
    cq_marks = models.PositiveIntegerField(default=0, blank=True)
    mcq_marks = models.PositiveIntegerField(default=0, blank=True)
    practical_marks = models.PositiveIntegerField(default=0, null=True, blank=True)
    total_marks = models.PositiveIntegerField(null=True, blank=True)
    grade = models.CharField(max_length=2, null=True, blank=True)
    point = models.FloatField(default=0,)

    def __str__(self):
        return 'Roll-'+str(self.roll)


    def save(self, *args, **kwargs):
        result=self.get_grade(self.total_marks)
        self.grade=result['grade']
        self.point=result['point']

        super(Grade, self).save(*args, **kwargs)

        
    def get_grade(self,total):
        if total >= 80:
            grade = 'A+'
            point = 5
        elif total >= 70:
            grade = 'A'
            point = 4
        elif total >= 60:
            grade = 'A-'
            point = 3.5
        elif total >= 50:
            grade = 'B'
            point = 3
        elif total >= 40:
            grade = 'C'
            point = 2
        elif total >= 33:
            grade = 'D'
            point = 1
        else:
            grade = 'F'
            point=0
        result={'grade':grade,'point':point}
        return result


    def get_dict(self):
        return {

            'cq_marks':self.cq_marks,
            'mcq_marks':self.mcq_marks,
            'practical_marks':self.practical_marks,

        }