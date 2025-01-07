from django import forms

class VoiceAIForm(forms.Form):
    voice = forms.CharField(label='Voice', required=True)