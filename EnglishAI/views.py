from django.http import JsonResponse
from django.views import View

from EnglishAI import forms
from django import forms
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
#class indexView(View):
 #   def hello_world(request):
  #      return JsonResponse({'message': 'Hello, World!'})
class VoiceForm(forms.Form):
    voice = forms.CharField(max_length=1000)
@csrf_exempt
def get_voice(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = VoiceForm(data)
            print(form.cleaned_data if form.is_valid() else form.errors, "+++++++++")

            if form.is_valid():
                voice = form.cleaned_data['voice']
                return JsonResponse({'voice': voice})
            else:
                #form = VoiceForm()
                return JsonResponse({'errors': form.errors})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON Decode Error'})

    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    #return JsonResponse({'message': 'Hello, World! mc'})


class indexView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Hello, World! mc'})



