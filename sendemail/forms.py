from datetime import datetime, timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
# from bootstrap_datepicker_plus.widgets import DateTimePickerInput
# from django.contrib.admin.widgets import AdminSplitDateTime


class FormEmail(forms.Form):
    email = forms.EmailField(label='Email')
    text = forms.CharField(widget=forms.Textarea)
    # date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    date = forms.DateTimeField(initial=datetime.now())
    # date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    # date = forms.DateTimeField(widget=DateTimePickerInput())
    # date = forms.SplitDateTimeField()

    def clean_date(self):
        # date = datetime.strptime(self.cleaned_data['date'], '%d/%m/%y %H:%M:%S')
        date = self.cleaned_data['date'], '%d/%m/%y %H:%M:%S'
        now = timezone.now()
        if (now + timedelta(days=+2)) >= date and date >= now:
            return date
        else:
            raise ValidationError('This date is not correct')
