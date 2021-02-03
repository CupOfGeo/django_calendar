from django.shortcuts import render
import datetime
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    context = {}
    cal = HTMLCalendar()
    calendar = cal.formatmonth(datetime.date.today().year, datetime.date.today().month, withyear=True)
    calendar = calendar.replace('<td ', '<td  width="150" height="125"')
    calendar = calendar.replace('<table border="0" cellpadding="0" cellspacing="0" class="month">', '<table class="month">')
    print(calendar)

    context['calendar'] = mark_safe(calendar)

    return render(request, 'cal/index.html', context)


# <table class="month">
# <tr><th colspan="7" class="month">February 2021</th></tr>
# <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
# <tr><td  width="150" height="125"class="mon">1</td><td  width="150" height="125"class="tue">2</td><td  width="150" height="125"class="wed">3</td><td  width="150" height="125"class="thu">4</td><td  width="150" height="125"class="fri">5</td><td  width="150" height="125"class="sat">6</td><td  width="150" height="125"class="sun">7</td></tr>
# <tr><td  width="150" height="125"class="mon">8</td><td  width="150" height="125"class="tue">9</td><td  width="150" height="125"class="wed">10</td><td  width="150" height="125"class="thu">11</td><td  width="150" height="125"class="fri">12</td><td  width="150" height="125"class="sat">13</td><td  width="150" height="125"class="sun">14</td></tr>
# <tr><td  width="150" height="125"class="mon">15</td><td  width="150" height="125"class="tue">16</td><td  width="150" height="125"class="wed">17</td><td  width="150" height="125"class="thu">18</td><td  width="150" height="125"class="fri">19</td><td  width="150" height="125"class="sat">20</td><td  width="150" height="125"class="sun">21</td></tr>
# <tr><td  width="150" height="125"class="mon">22</td><td  width="150" height="125"class="tue">23</td><td  width="150" height="125"class="wed">24</td><td  width="150" height="125"class="thu">25</td><td  width="150" height="125"class="fri">26</td><td  width="150" height="125"class="sat">27</td><td  width="150" height="125"class="sun">28</td></tr>
# </table>
