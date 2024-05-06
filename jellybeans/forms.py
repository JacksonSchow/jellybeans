from django import forms
from .models import JellybeanFlavor

# Form used for adding and editing jellybean flavors. Includes widgets for form elements styling
class AddFlavorForm(forms.ModelForm):
    class Meta:
        model = JellybeanFlavor
        fields = ['flavor', 's3_image']
        widgets = {
            'flavor': forms.TextInput(attrs={'class': 'flavor-input', 'placeholder': 'Enter flavor'}),
            's3_image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def save(self, commit=True):
        instance = super(AddFlavorForm, self).save(commit=False)
        if self.cleaned_data.get('delete_image'):
            instance.s3_image.delete(save=False)
        if commit:
            instance.save()
            self.save_m2m()
        return instance
