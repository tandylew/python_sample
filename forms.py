from django import forms
import datetime

class DateForm(forms.Form):
    todo = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class' : 'todo'}), required=False)
    date = forms.DateField(label='Date: ', widget=forms.SelectDateWidget,required=False)
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput(),
        required=False
    )

class SqlForm(forms.Form):
    sql = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class' : 'sql'}),required=False)
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput(),
        required=False
    )

class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254,required=False)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput,required=False)

#    def clean(self):
#        cleaned_data = super(DateForm, self).clean()
#        cleaned_data = super(SqlForm, self).clean()
#        todo = cleaned_data.get('todo')
#        date = cleaned_data.get('date')
#        sql = cleaned_data.get('sql')
#        #raise forms.ValidationError('You have to write something!')
