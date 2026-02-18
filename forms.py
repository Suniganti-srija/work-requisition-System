from django import forms
from .models import WorkRequisition

class WorkRequisitionForm(forms.ModelForm):
    NATURE_OF_WORK_CHOICES = [
        ('FDM', 'FDM'),
        ('SLA', 'SLA'),
        ('PBF', 'PBF'),
        ('DED', 'DED'),
        ('FFF', 'FFF'),
    ]
    
    # Custom field for nature of work to allow multiple values
    nature_of_work = forms.MultipleChoiceField(
        choices=NATURE_OF_WORK_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Nature of work (Select all that apply)"
    )

    class Meta:
        model = WorkRequisition
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'agreed_pdc': forms.DateInput(attrs={'type': 'date'}),
            'extended_pdc': forms.DateInput(attrs={'type': 'date'}),
            'approval_date': forms.DateInput(attrs={'type': 'date'}),
            'recommendation_date': forms.DateInput(attrs={'type': 'date'}),
            'nomenclature': forms.Textarea(attrs={'rows': 3}),
            'project': forms.Select(),
        }
    
    def clean_nature_of_work(self):
        # Convert list of selected values to a comma-separated string
        data = self.cleaned_data['nature_of_work']
        return ', '.join(data)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If instance exists (edit mode), populate nature_of_work from string
        if self.instance and self.instance.pk and self.instance.nature_of_work:
            self.initial['nature_of_work'] = self.instance.nature_of_work.split(', ')

        # Add form-control class to all fields
        for field_name, field in self.fields.items():
            current_classes = field.widget.attrs.get('class', '')
            if 'form-check-input' not in current_classes: # Skip checkkboxes
                field.widget.attrs['class'] = 'form-control ' + current_classes
