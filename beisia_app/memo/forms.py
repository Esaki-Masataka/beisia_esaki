from django import forms
from .models import Lists

class ListsForm(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['date', 'name','number','lists']
        labels = {
                'date':'日付',
                'name':'お名前',
                'number':'学籍番号',
                'lists':'買い物リスト',
            }
        widgets={'date':forms.TextInput(attrs={'placeholder':''})}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    
        '''def __init__(self, *args, **kwargs):
            super(ListsForm, self).__init__(*args, **kwargs)
            self.fields['date'].initial = 5'''