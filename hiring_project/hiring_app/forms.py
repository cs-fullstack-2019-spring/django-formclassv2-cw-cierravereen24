from django import forms


class EmployeeApplication(forms.Form):
    name = forms.CharField()
    dateOfBirth = forms.DateField()
    position = forms.CharField()
    salary = forms.IntegerField

    def __str__(self):
        return self.name
