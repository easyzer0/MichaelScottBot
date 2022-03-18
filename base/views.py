from django.shortcuts import render
from .forms import MemberForm
from django.contrib import messages
from rest_framework import viewsets
from base.serializers import MemberSerializer
from base.models import Member

def index(request):
    form = MemberForm()
    if request.method == 'POST':
        print(request.POST)
        form = MemberForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Phone number successfully added!')
            form.save()
    context = {'form':form}
    return render(request, 'base/index.html', context)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
