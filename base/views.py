from django.shortcuts import render
from .forms import MemberForm

def index(request):
    form = MemberForm()
    if request.method == 'POST':
        print(request.POST)
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'base/index.html', context)
