from .models import Jop
from .serializers import JobSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def joblistapi(request):
    all_jobs =  Jop.objects.all()
    data = JobSerializers(all_jobs, many = True).data
    return Response({'data' : data})
    
@api_view(['GET'])
def job_detailes_api(request, id):
    job = Jop.objects.get(id = id)
    data = JobSerializers(job).data
    return Response({'data':data})