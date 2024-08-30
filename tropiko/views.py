from django.shortcuts import render
from .forms import TropikoConfig

def tropikoview(request):
    form = TropikoConfig
    if request.method == 'POST':
        form = TropikoConfig(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {'form': form})

