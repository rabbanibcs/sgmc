from .models import *
from student.models import *

def save_form_data(request,examination,department,grade,student):
    grade.examination_id = examination.id
    grade.cq_marks = int(request.POST.get('cq_marks'))
    grade.mcq_marks = int(request.POST.get('mcq_marks'))
    grade.subject_id = department.id
    grade.roll = student.class_roll
    grade.session=student.session

    if request.POST.get('practical_marks'):
        grade.practical_marks = int(request.POST.get('practical_marks'))
        grade.total_marks = grade.practical_marks + grade.cq_marks + grade.mcq_marks
    else:
        grade.total_marks = grade.cq_marks + grade.mcq_marks
    grade.save()


def get_grade_object(examination,department,student):
    try:
        grade = Grade.objects.get(examination=examination, subject=department,session=student.session, roll=student.class_roll)
        # print('grade',grade)
    except:
        grade = Grade()
    return grade



def get_exam(year, term,session=None):
    examinations = Examination.objects.filter(year=year,term=term)
    for examination in examinations:
        if examination.term == term:
            return examination
    else:
        return None


# def sudent_has_this_subject(subCode,student):

#     subjects = student.subjects
#     subjects = subjects.split(',')
#     # print(subjects)
#     for subject in subjects:
#         if subject==subCode[0]:
#             # print(subject,subCode[0])
#             return True
#     return False


# def student_exists(roll,session):
#     try:
#         student = Student.objects.get(class_roll=roll,session=session)
#         return student
#     except:
#         return None

# def next_student_exists(roll,session):
#     roll+=1
#     student=student_exists(roll,session)
#     return student

# def get_next_student(subCode,roll,session):
#     student=next_student_exists(roll,session)
#     if student:
#         check=student.sudent_has_this_subject(subCode)
#         if check:
#             print(f'roll-{student.class_roll} has subject- {subCode}')
#             return student
#         else:
#             roll+=1
#             print(roll,'roll')
#             return get_next_student(subCode, roll,session)
#     else:
#         print('Next student does not exists')
#         return student








