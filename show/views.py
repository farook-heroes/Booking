from django.shortcuts import render
from django.core import serializers
from book.models import Booking
# Create your views here.
import json
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    bookings = Booking.objects.all()  # Query all booking instances
    # json_data = serializers.serialize("json", bookings)
    # json_data = json.dumps(list(json_data), indent=2)
    s=dict()
    print(bookings)
    p=[]
    
    for i in bookings:
        k=dict()
        formatted_date =i.date.strftime('%Y-%m-%d')
        k={"title":i.name,"date":formatted_date}
        
        p.append(k)
    s={"events":p}
    s=json.dumps(s, indent=4)
    json_file_path = os.path.join(BASE_DIR, 'static')
    with open(json_file_path+'/booking.json', 'w') as json_file:
        json_file.write(s)
        
    return render(request,"index.html")