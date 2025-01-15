from django.shortcuts import render,HttpResponse
import requests
import datetime
from django.contrib import messages

def Home(request):
  
  if 'city' in request.POST:
    city= request.POST['city']
  else:
    city='lucknow'
  url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5fb36033e709619bcd680c66e2b3273d'

  PARAMS={'units':'metric'}
  API_KEY='AIzaSyBSpnUOiRVovPGuPQuwZGkT6_jEX4q9JzU'
  SEARCH_ENGINE_ID = 'b00ae9c6c6cfd4455'

  q= city + "1920x1080"
  page=1
  start= (page-1) * 10 +1
  searchtype='image'
  city_url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={q}&start={start}&searchType={searchtype}&imgSize=xlarge'
  data = requests.get(city_url).json()
  count=1
  search_items= data.get("items",[])
  if search_items:
    image_url=search_items[0]['link']
  else:
    image_url=''

  try:
    data=requests.get(url,PARAMS).json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp=data['main']['temp']
    day = datetime.date.today()
    return render(request,'Home.html',{'description':description.capitalize(),'icon':icon,'temp':temp,'day':day,'city':city.capitalize() ,'exception_occured':False,'image_url': image_url})

  except requests.exceptions.RequestException as e:
    exception_occured=True
    messages.error(request,'Enter data is not available in the API')
    day=datetime.date.today()
    return render(request,'Home.html',{'description':'The sky is blue','icon':'01d','temp':'25','day':day,'city':'Lucknow','exception_occured':False})

  
