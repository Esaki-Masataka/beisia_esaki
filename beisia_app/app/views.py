import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from . import mixins
from .forms import BS4ScheduleForm
from .models import Schedule
'''from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ListsForm
from .models import Lists'''
...
...

def index(request):
    params = {
            'title':'ベイシア便オンラインサービス',
    }
    return render(request, 'app/home.html', params)


class MyCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'app/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """week_calendar_context = self.get_week_calendar()"""
        month_calendar_context = self.get_month_calendar()
        """context.update(week_calendar_context)"""
        context.update(month_calendar_context)
        return context

    def form_valid(request, self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.save()
        return redirect('memo:create', year=date.year, month=date.month, day=date.day)
        
'''def test(request, year, month, day):
    params = {
            'year1' : year,
            'month1' : month,
            'date1' : day,
    }
    return render(request, 'app/test.html', params)'''


    
    
# Create your views here.
