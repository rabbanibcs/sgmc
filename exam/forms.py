from django import forms


class MarksFormScience(forms.Form):
    cq_marks = forms.IntegerField(max_value=50, min_value=0)
    mcq_marks = forms.IntegerField(max_value=25, min_value=0)
    practical_marks = forms.IntegerField(max_value=25, min_value=0, required=False)


class MarksForm(forms.Form):
    cq_marks = forms.IntegerField(max_value=60, min_value=0)
    mcq_marks = forms.IntegerField(max_value=40, min_value=0)


exams = (('half yearly', 'Half Yearly'), ('yearly', 'Yearly'),
         ('pre test', 'Pre Test'), ('test', 'Test'), ('others', 'Others'))


class ExamCreation(forms.Form):
    year = forms.IntegerField(min_value=2020, max_value=2050)
    term = forms.ChoiceField(choices=exams)
