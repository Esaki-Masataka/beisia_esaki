from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ListsForm
from .models import Lists


class ListsCreateView(CreateView):
    template_name = 'memo/create.html'
    form_class = ListsForm
    model = Lists
    success_url = reverse_lazy('memo:thanks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.kwargs.get('year')
        context['month'] = self.kwargs.get('month')
        context['day'] = self.kwargs.get('day')
        context['form'] = ListsForm( initial = {'date':str(context['year']) + '/' + str(context['month']) + '/' + str(context['day'])} )
        return context
    
    
    def form_valid(self, form):
        ctx = {'form': form }
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'memo/confirm.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'memo/create.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('memo:create'))
        
def thanks(request):
    return render(request, 'memo/thanks.html')

def index(request):
    data = Lists.objects.all()
    params = {
            'title' : 'Hello',
            'data' : data,
    }
    return render(request, 'memo/record.html', params)

def okaimono(request, num): 
    obj = Lists.objects.get(id=num)
    params = {
            'id':num,
            'form':ListsForm(instance=obj),
            }
    return render(request, 'memo/okaimono.html', params)
