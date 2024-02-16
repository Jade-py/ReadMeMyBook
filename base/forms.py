from django import forms

class ImageUploadForm(forms.Form):
    class Meta:
        fields = ['image_file']