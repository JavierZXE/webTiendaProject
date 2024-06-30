from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def registration(request):
    today = datetime.today()
    eighteen_years_ago = today - timedelta(days=18*365 + 5)
    max_date = eighteen_years_ago.strftime('%Y-%m-%d')
    return render(request, "registration.html", {'max_date' : max_date})