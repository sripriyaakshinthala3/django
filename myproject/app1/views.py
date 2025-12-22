from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def view1(request):
    return HttpResponse("hello world ,iam from view1")

def view2(request):
    return HttpResponse("hello world, iam from view2")   
def view3(request):
    return  JsonResponse({"name":"sri","message":"hello world"})  
def view4(request):
    return JsonResponse({"status":"success","response":"welcome"})  

def dynamicview(request):
    qp1=request.GET.get("name","world")
    return HttpResponse(f"hello {qp1}")

def personinfo(request):
    name=request.GET.get("name","sri")
    city=request.GET.get("city","nrml")
    role=request.GET.get("role","learner")
    info={"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":info})

def ticketbooking(request):
    movie=request.GET.get("movie","Billa")   
    showtime=request.GET.get("showtime","6pm")
    ticket_cost=request.GET.get("ticket_cost","200")
    total_no_of_tickets=request.GET.get("total_no_of_tickets","4")
    total_amount=request.GET.get("total_amount","800") 
    details={"movie":movie,"showtime":showtime," ticket_cost":ticket_cost,"total_no_of_tickets":total_no_of_tickets,"total_amount":total_amount}
    return JsonResponse({"status":"success","data":details})

def temp1(request):
    return render(request,"./first.html")    

def temp2(request):
    return render(request,"./second.html")    

products =[
  {
    "id": 1,
    "name": "Laptop",
    "category": "Electronics",
    "price": 55000,
    "brand": "Dell",
    "stock": 10,
    "rating": 4.5
  },
  {
    "id": 2,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 25000,
    "brand": "Samsung",
    "stock": 15,
    "rating": 4.3
  },
  {
    "id": 3,
    "name": "Headphones",
    "category": "Accessories",
    "price": 2000,
    "brand": "Boat",
    "stock": 30,
    "rating": 4.1
  },
  {
    "id": 4,
    "name": "Office Chair",
    "category": "Furniture",
    "price": 8000,
    "brand": "Ikea",
    "stock": 5,
    "rating": 4.0
  },
  {
    "id": 5,
    "name": "Water Bottle",
    "category": "Kitchen",
    "price": 500,
    "brand": "Milton",
    "stock": 50,
    "rating": 4.2
  }
]




def  get_productby_category(request):
    category = request.GET.get("category")
    
    if not category:
        return JsonResponse(
            {"error": "category query parameter is required"},
            status=400
        )

 
    filtered_data =[]
    for product in products:
        if product["category"].lower() == category.lower():

            filtered_data.append(product)


    return JsonResponse(filtered_data, safe=False)    