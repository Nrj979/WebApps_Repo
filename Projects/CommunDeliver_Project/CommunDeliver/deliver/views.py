from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.db.models import *      
from .models import *
import time

from django.db.models import Q
from datetime import date, datetime

import googlemaps
from geopy.geocoders import Nominatim       
from geopy.distance import geodesic         



GOOGLE_MAPS_API_KEY = "SDGGDeukjaknk"

gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
# Create your views here.
@never_cache
def login_page(request):        # login page
    return render(request, 'login.html')

never_cache
@csrf_exempt
def login(request):     # login 
    email = request.POST.get('email')
    password = request.POST.get('password')

    if email == 'admin@mail.com' and password == 'Admin@123':
        # g = Partner.objects.get(partnername='adam')
        # print(g)
        get_partners = Partner.objects.all()
        print(get_partners)
        return render(request,'admin_home.html',{'partners':get_partners})
    elif Partner.objects.filter(partnermail=email, partnerpassword=password).exists():
        name = Partner.objects.get(partnermail=email)
        if name.status == 'verified':
            name = name.partnername.capitalize()
            request.session['mail'] = email
            print('done')
            return render(request,'partner_home.html',{'user':name})
        else:
            print('not verified')
            # return HttpResponse("<script>alert('Login Failed!!...\n Not verified user!..');window.location.assign('')'/login_page/'</script>")
           
            return HttpResponse("<script>alert('Login Failed!!...\\nNot verified user!..');window.location.href='/login_page/'</script>")

    elif Customer.objects.filter(custmail=email, custpassword=password).exists():
        name = Customer.objects.get(custmail=email)
        name = name.custname.capitalize()
        request.session['mail'] = email
        return render(request,'customer_home.html',{'user':name})
    else:
        return HttpResponse("<script>alert('Login Failed!!...');window.location.href='/login_page/'</script>")
        pass

@never_cache     
def logout(request):        # logout
    if 'mail' in request.session:
        del request.session['mail']
        # del request.session['request_id']
    return render(request,'login.html')
    


def customer_register_page(request):        
    return render(request,'customer_register.html')

@csrf_exempt
def register_customer(request):     
    name = request.POST.get('name')
    email = request.POST.get('mail')
    password = request.POST.get('password')
    phone = request.POST.get('phone')

    print(f'Name: {name}, Mail: {email}, Password: {password}, Phone: {phone}')
    data = {}
    reg_ob1 = Customer.objects.filter(custmail=email)
    print('Customer: ', reg_ob1)
    if reg_ob1.count() > 0:
        print('yes')
        data['result']='no'
        return HttpResponse("<script>alert('Email already Exist);</script>")
    else:
        reg_ob2 = Customer(custname=name, custmail=email, custpassword=password,custcontact=phone)
        print(reg_ob2)
        reg_ob2.save()
        data["result"] ="yes"
        print('response data:',data)
        saved_customer = Customer.objects.get(pk=reg_ob2.pk)
        print(f'Name: {saved_customer.custname}, Mail: {saved_customer.custmail}, Password: {saved_customer.custpassword}, Phone: {saved_customer.custcontact}')
        return JsonResponse(data,safe=False)

        return HttpResponse("<script>alert('Account created successfully');window.location.href='/login_page/';</script>")



def partner_register_page(request):     
    return render(request,'partner_register.html')


@csrf_exempt
def register_partner(request):      
    name = request.POST.get('name')
    email = request.POST.get('mail')
    password = request.POST.get('password')
    prooftype = request.POST.get('proof')
    proofid = request.POST.get('proofid')
    phone = request.POST.get('phone')
    umodel = request.POST.get('umodel')
    vehicle = request.POST.get('vehicle')

    print(f'Name: {name}, Mail: {email}, Password: {password}, Phone: {phone}, VehicleType: {umodel}, Vehicle: {vehicle}, ProofType: {prooftype}, Proofid: {proofid}')

    data = {}
    reg_p1 = Partner.objects.filter(partnermail=email)
    if(reg_p1.count() > 0):
        data['result']='no'
        return HttpResponse("<script>alert('Email already Exist);</script>")
    else:
        reg_p2 = Partner(partnername=name, partnermail=email, partnerpassword=password,partneridproof=prooftype, partneridno=proofid, partnercontact=phone, partnervehicle=umodel, partnervehicleno=vehicle)
        print(reg_p2)
        reg_p2.save()
        data['result'] = 'yes'
        print('Response data: ',data)
        saved_partner = Partner.objects.get(pk=reg_p2.pk)
        print(f'Name: {saved_partner.partnername}, Mail: {saved_partner.partnermail}, Password: {saved_partner.partnerpassword}, Phone: {saved_partner.partnercontact}, VehicleType: {saved_partner.partnervehicle}, Vehicle: {saved_partner.partnervehicleno}, ProofType: {saved_partner.partneridproof}, Proofid: {saved_partner.partneridno}')
        return JsonResponse(data,safe=False)


 

@never_cache
@csrf_exempt
def admin_page(request):
    get_partners = Partner.objects.all()
    print(get_partners)
    return render(request,'admin_home.html',{'partners':get_partners})


@never_cache
@csrf_exempt
def verify_partner(request):      
    print('inside verify func')
    partnerid = request.POST.get('partner_id')
    status = request.POST.get('current_status')
    print(partnerid,status)

    try:
        partner = Partner.objects.get(partnerid=partnerid)
        print(partner)
        if status == 'pending':
            partner.status = 'verified'
            partner.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Partner is already verified.'})
    except Partner.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Partner not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


@never_cache
def home_page(request):   
    if 'mail' in request.session:
        email = request.session['mail']
        ob = Customer.objects.get(custmail=email)
        return render(request,'customer_home.html',{'user':ob.custname.capitalize()})
    
@never_cache
def partner_home_page(request):
    if 'mail' in request.session:
        email = request.session['mail']
        p_ob = Partner.objects.get(partnermail=email)
        return render(request, 'partner_home.html', {'user':p_ob.partnername.capitalize()})


@never_cache
@csrf_exempt
def add_request(request):   
    return render(request,'add_request.html')


def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="deliver")
    location = gmaps.geocode(location_name)
    if location:
        print("got location")
        return (location[0]['geometry']['location']['lat'], location[0]['geometry']['location']['lng'])
    else:
        print(f"Could not find coordinates for '{location_name}'.")
        return None
    

def calculate_route_distance(start_point, end_point):
    return geodesic(start_point, end_point).miles


@csrf_exempt
def get_partners_in_range(pickup_location, dropping_location,cid,package_size):
    print(type(package_size))
    partners_in_range = []
    all_partners = PostAvailability.objects.all()

    amount = 0
    cnt = 1
    for partner in all_partners:
        
        start_location = (partner.startlatitude, partner.startlongitude)
        end_location = (partner.endlatitude, partner.endlongitude)

       
        print('in distance check')
        print(start_location)
        print(end_location)
        
       

        print('pl->',pickup_location)
        print('dl -> ',dropping_location)
        print(geodesic(pickup_location, start_location).km)
        print(geodesic(dropping_location, end_location).km)

        deliver_distance = gmaps.directions(pickup_location, dropping_location, mode="driving")
        if deliver_distance:
            print("distance:",deliver_distance[0]['legs'][0]['distance']['value'])
        else:
            pass
        pick_distance = gmaps.directions(pickup_location, start_location,mode="driving")
        drop_distance = gmaps.directions(dropping_location, end_location,mode="driving")
        
        print("....................pickkkk",pick_distance)
       

        if(len(pick_distance) == 0 and len(drop_distance) == 0):
            pass
        else:
        # print("####",pick_distance)
        # print("*****",drop_distance)
            # print("PICK distance:>>>>>>>>",pick_distance[0]['legs'][0]['distance']['value'])
            # print("DROP distance:>>>>>>>>",drop_distance[0]['legs'][0]['distance']['value'])
            if (pick_distance[0]['legs'][0]['distance']['value']/1000 <= 1.6 and drop_distance[0]['legs'][0]['distance']['value']/1000<= 1.6):
                print('in condition')
                if(deliver_distance[0]['legs'][0]['distance']['value']/1000 <= 5):
                    amount = 2
                elif(deliver_distance[0]['legs'][0]['distance']['value']/1000 > 5 and deliver_distance[0]['legs'][0]['distance']['value']/1000 < 15):
                    amount = 5
                else:
                    amount = 10
        
                if package_size <= 0.5:
                    amount += 0.3
                elif package_size > 0.5 and package_size <= 1:
                    amount += 0.75
                elif package_size > 1 and package_size <5:
                    amount += 1.5
                else:
                    amount += 2.75
                
                print("cnt:>>>>>>>>>>>>>>>>",cnt)
                cnt+=1
                print('similar')
                print('Amount',amount)
                partner_data = {
                    'cid':cid,
                    'id':partner.partner_id.partnerid,
                    'name': partner.partner_id.partnername.capitalize(),
                    'contact_number': partner.partner_id.partnercontact,
                    'from': partner.startlocation.capitalize(),
                    'to': partner.endlocation.capitalize(),
                    'fare':amount,
                    'rating': partner.partner_id.rating
                    
                }
                partners_in_range.append(partner_data)
                
            else:
                print("No Partners Available")
                
            # print('fare:', amount)
            # if (geodesic(pickup_location, start_location).km <= 10 and geodesic(dropping_location, end_location).km <= 10):
            #     if(geodesic(pickup_location,dropping_location).km <= 5):
            #         amount = 2
            #     elif(geodesic(pickup_location,dropping_location).km > 5 and (geodesic(pickup_location,dropping_location).km < 15)):
            #         amount = 5
            #     else:
            #         amount = 10

            # print('similar')
                # partner_data = {
                #     'cid':cid,
                #     'id':partner.partner_id.partnerid,
                #     'name': partner.partner_id.partnername.capitalize(),
                #     'contact_number': partner.partner_id.partnercontact,
                #     'from': partner.startlocation.capitalize(),
                #     'to': partner.endlocation.capitalize(),
                #     'fare':amount,
                #     'rating': partner.partner_id.rating
                    
                # }
            

    return partners_in_range


def find_available_drivers(request_pickup, request_delivery, drivers):
    available_drivers = []

    print("in find availableity")

    for driver in drivers:
        driver_name = driver["Driver_Name"]
        driver_start = driver["Start_Location"]
        driver_end = driver["End_Location"]
        direct_route_distance = calculate_route_distance(get_coordinates(driver_start), get_coordinates(driver_end))

        diversion_distance = (
            calculate_route_distance(get_coordinates(driver_start), request_pickup) +
            calculate_route_distance(request_pickup, request_delivery) +
            calculate_route_distance(request_delivery, get_coordinates(driver_end))
        )

        if diversion_distance <= 1.2 * direct_route_distance:
            available_drivers.append((driver_name, driver_start, driver_end))

    return available_drivers



@csrf_exempt
def delivery_request(request): 
    if 'mail' in request.session:

        email = request.session['mail']
        c_ob = Customer.objects.get(custmail=email)
        cid = c_ob.custid
        
        package_size = request.POST.get('packageSize')
   
        package_pickup = request.POST.get('pickup')
        package_drop = request.POST.get('drop')
        print(type(package_drop))        

        package_pickup = get_coordinates(package_pickup)
        package_drop = get_coordinates(package_drop)
        print('in request()')
        print(package_pickup)
        print(package_drop)

        if package_pickup and package_drop:
        
            partners = get_partners_in_range(package_pickup, package_drop,cid,float(package_size))
            return JsonResponse(partners, safe=False)



@never_cache
@csrf_exempt
def view_request(request):     
    if 'mail' in request.session:
    
        requests = []
        req_ob = DeliveryRequest.objects.exclude(Q(status='package delivered') | Q(status='rejected'))
        
        for req in req_ob:
            request_data={
                    "id":req.customer.custid,
                    "request_id":req.requestid,
                    "name":req.customer.custname.capitalize(),
                    "contact":req.customer.custcontact,
                    "package":req.package_name.capitalize(),
                    "packageType":req.package_type.capitalize(),
                    "packageSize":req.package_size,
                    "pick":req.pickup_point.capitalize(),
                    "drop":req.drop_point.capitalize(),
                    "deliveryinfo":req.deliveryinfo.capitalize(),
                    "fare":req.amount,
                    "status":req.status,
            }
            requests.append(request_data)
        
        return render(request, 'view_requests.html',{'requests':requests})
    
@never_cache
@csrf_exempt
def respond_request(request):
    if 'mail' in request.session:
        email = request.session['mail']
        req_id = request.POST.get('request_id')
        status = request.POST.get('status')
        print(status,":", req_id)
        if status != '' and req_id != '':
            if status == 'rejected':
                request_ob = DeliveryRequest.objects.get(requestid=req_id)
                request_ob.status = status
                request_ob.save()
                response_data = {'status': 'success'}
                return JsonResponse(response_data)
                return render(request,'view_requests.html')
            
            else:
                print('accpet request')
                request.session['request_id'] = req_id
                print(request.session['request_id'])
                request_ob = DeliveryRequest.objects.get(requestid=req_id)
                request_ob.status = status
                request_ob.save()
                response_data = {'status': 'success'}
                return JsonResponse(response_data)

        else:
                response_data = {'status': 'error'} 
                return JsonResponse(response_data)
        

@never_cache
@csrf_exempt
def post_avail(request):        
    if 'mail' in request.session:
        return render(request, 'post_availability.html')
    

@never_cache
@csrf_exempt
def update_status(request):
    
    if 'mail' in request.session:
        email = request.session['mail']
        requests = []

        if 'request_id' in request.session:
            request_id = request.session['request_id']
            # request_id = 3
            
            print('Update status request-id: ',request_id)
            req = DeliveryRequest.objects.get(requestid=request_id)        
            if req.payment_status == 'paid':
                del request.session['request_id']
                return render(request, 'update_status.html')
            else:

                print(req)

                status = req.status
                print("status: ",status)
                
                
                
                
                request_data={
                    "id":req.customer.custid,
                    "request_id":req.requestid,
                    "name":req.customer.custname.capitalize(),
                    "contact":req.customer.custcontact,
                    "package":req.package_name.capitalize(),
                    "packageType":req.package_type.capitalize(),
                    "packageSize":req.package_size,
                    "pick":req.pickup_point.capitalize(),
                    "drop":req.drop_point.capitalize(),
                    "deliveryinfo":req.deliveryinfo.capitalize(),
                    "fare":req.amount,
                    "status":req.status,
                }
                requests.append(request_data)

                return render(request, 'update_status.html',{'requests':requests})
        else:
            return render(request, 'update_status.html',{'requests':requests})

                
    
@never_cache
@csrf_exempt
def change_status(request):
    if 'mail' in request.session:
        email = request.session['mail']

        req_id = request.POST.get('request_id')
        new_status = request.POST.get('new_status')
        print(req_id, new_status)

        req_ob = DeliveryRequest.objects.get(requestid=req_id)
        req_ob.status = new_status
        req_ob.save()
        response_data = {'status':'success'}
        return JsonResponse(response_data)


@never_cache
@csrf_exempt
def partner_status(request):   
    if 'mail' in request.session: 
   
        requests = []

        request_id = request.session['cust_request_id']
        # request_id = 1

        print(request_id)
        req = DeliveryRequest.objects.get(requestid=request_id)
        req_data={
                "id":req.customer.custid,
                "name":req.courier_partner.partnername.capitalize(),
                "contact":req.courier_partner.partnercontact,
                "package":req.package_name.capitalize(),
                "packageType":req.package_type.capitalize(),
                "packageSize":req.package_size,
                "pick":req.pickup_point.capitalize(),
                "drop":req.drop_point.capitalize(),
                "deliveryinfo":req.deliveryinfo.capitalize(),
                "fare":req.amount,
                "status":req.status,
            

        }
        requests.append(req_data)
        return render(request,'partner_status.html',{'requests':requests})
    

@never_cache
@csrf_exempt
def payment_page(request):
    if 'mail' in request.session:
        email = request.session['mail']
        request_id = request.session['cust_request_id']
        # request_id = 1
        ob = DeliveryRequest.objects.get(requestid=request_id)
        
        return render(request,'payment.html',{'amount':ob.amount})
    
    
@never_cache
@csrf_exempt
def pay(request):
    if 'mail' in request.session:
        email = request.session['mail']
        request_id = request.session['cust_request_id']
        # request_id = 1
        pay_status = request.POST.get('pay_status')
        pay_ob = DeliveryRequest.objects.get(requestid=request_id)
        pay_ob.payment_status = pay_status
        pay_ob.save()

        
        response_data = {'status': 'success','message': 'Payment Successfull'}
        return JsonResponse(response_data)
    
def feedback_page(request):
    if 'mail' in request.session:
        email = request.session['mail']
        return render(request, 'feedback.html')

    

@never_cache
@csrf_exempt
def add_feedback(request):
    if 'mail' in request.session:
        request_id = request.session['cust_request_id']
        # request_id = 1
        rating = request.POST.get('rating')
        feedback = request.POST.get('feed')
        feed_ob = DeliveryRequest.objects.get(requestid=request_id)
        feed_ob.feedback = feedback
        feed_ob.rate = rating
        partner_mail =  feed_ob.courier_partner.partnermail
        partner_ob = Partner.objects.get(partnermail = partner_mail)
        current_rating = partner_ob.rating
        avg_rating = round((float(current_rating) + float(rating)) / 2, 1)
        partner_ob.rating = str(avg_rating)
        partner_ob.save()
        feed_ob.save()

        response_data={"status": "success"}
        return JsonResponse(response_data)
                
    

        


@csrf_exempt
def add_availability(request):      
    if 'mail' in request.session:
        email = request.session['mail']
        # print(email)
        partner_ob = Partner.objects.get(partnermail=email)
        id = partner_ob.partnerid
        print(id)
        
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        start_route = request.POST.get('start_route')
        end_route = request.POST.get('end_route')

        geolocator = Nominatim(user_agent="deliver")
        start_location = gmaps.geocode(start_route)
        if start_location:
            start_latitude, start_longitude = start_location[0]['geometry']['location']['lat'], start_location[ 0]['geometry']['location']['lng']
        print(start_latitude,start_longitude)

        # start_latitude = start_route
        # start_longitude = start_route
        end_location = gmaps.geocode(end_route)
        if end_location:
            end_latitude, end_longitude =end_location[0]['geometry']['location']['lat'], end_location[ 0]['geometry']['location']['lng']
        # end_latitude = end_route
        # end_longitude = end_route

        # print(end_time,end_time, start_route,end_route)
        print(end_latitude,end_longitude)

      
        if start_time is not None and end_time is not None and start_route is not None and end_route is not None and id is not None:
    

            start_time = datetime.strptime(start_time, '%H:%M')
            end_time = datetime.strptime(end_time, '%H:%M')

       
            start_time = start_time.strftime('%I:%M %p')
            end_time = end_time.strftime('%I:%M %p')

        
            avail_obj = PostAvailability(starttime=start_time,endtime=end_time,startlocation=start_route,endlocation=end_route,startlatitude=start_latitude,startlongitude=start_longitude,endlatitude=end_latitude,endlongitude=end_longitude,partner_id_id=int(id))        
            avail_obj.save()
            response_data = {'status': 'success', 'message': 'Added Availability Successfully'}
        else:
            response_data = {'status': 'error', 'message': 'Failed to add availability'} 

        return JsonResponse(response_data)
    

       
    

@csrf_exempt
def send_requests(request):
    if 'mail' in request.session:
        email = request.session['mail']
        c_ob = Customer.objects.get(custmail=email)
        cust_id = c_ob.custid
        partner_id = request.POST.get('partner')
        package_name = request.POST.get('package_name')
        package_type = request.POST.get('package_type')
        package_size = request.POST.get('package_size')
        package_pickup = request.POST.get('pickup')
        package_drop = request.POST.get('drop')
        delivery_info = request.POST.get('info')
        amount = request.POST.get('amount')

        print(cust_id,partner_id)

        package_pickup1 = get_coordinates(package_pickup)
        package_drop1 = get_coordinates(package_drop)


        request_ob = DeliveryRequest(   
                customer_id=int(cust_id),
                courier_partner_id= int(partner_id),
                package_name=package_name,
                package_type=package_type,
                package_size=package_size,
                amount = amount,
                pickup_point=package_pickup,
                drop_point=package_drop,
                pickup_latitude=package_pickup1[0],
                pickup_longitude=package_pickup1[1],
                drop_latitude=package_drop1[0],
                drop_longitude=package_drop1[1],
                deliveryinfo=delivery_info       

                )
        request_ob.save()
        saved_customer = DeliveryRequest.objects.get(pk=request_ob.pk)
        req_id = saved_customer.requestid
        print(req_id)
        request.session['cust_request_id'] = req_id
        print("in send request ",req_id)
        # request.session['cust_request_id'] = '1'

        response_data = {'status': 'success', 'message': 'Successfully requested for delivery!!..','req_id': req_id}
        return JsonResponse(response_data)
    

 