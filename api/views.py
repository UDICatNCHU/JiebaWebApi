from django.shortcuts import render
from django.http import JsonResponse
import jieba
# Create your views here.

def cut(request):
	if request.POST and request.method == 'POST':
		data = request.POST
		data = data.dict()
		print(data)
		return JsonResponse(jieba.lcut(data['sentence']), safe=False)
	return JsonResponse({'result':False}, safe=False)