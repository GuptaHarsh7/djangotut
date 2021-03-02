from django import forms
from django.core import validators #needed for validation

# A self made validator, if we want to construct one
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name Needs to Start with Z")

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again:")
    text = forms.CharField(widget=forms.Textarea)

    #TO clean The entire form at once
    def clean(self):
        all_clean_data = super().clean()
        #to verify emails
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Make sure Emails Match!")

    #TO catch bots
    # botcatcher = forms.CharField(required=False,
    #                              widget = forms.HiddenInput,
    #                              validators = [validators.MaxLengthValidator(0)])

    #USED WHEN BUILDING FOR FUN
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

