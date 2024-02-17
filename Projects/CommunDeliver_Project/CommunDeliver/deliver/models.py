from django.db import models

# Create your models here.
class Customer(models.Model):
    custid = models.AutoField(primary_key=True)
    custname = models.CharField(max_length=100)
    custmail = models.CharField(max_length=200)
    custpassword = models.CharField(max_length=150)
    custcontact = models.CharField(max_length=25)


class Partner(models.Model):
    partnerid = models.AutoField(primary_key=True)
    partnername = models.CharField(max_length=100)
    partnermail = models.CharField(max_length=200)
    partneridproof = models.CharField(max_length=100)
    partneridno = models.CharField(max_length=30)
    partnerpassword = models.CharField(max_length=150)
    partnercontact = models.CharField(max_length=30)
    partnervehicle = models.CharField(max_length=200)
    partnervehicleno = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='pending')
    rating = models.CharField(max_length=20, default='5')


class PostAvailability(models.Model):
    postid = models.AutoField(primary_key=True)
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
    starttime = models.CharField(max_length=25)
    endtime = models.CharField(max_length=25)
    startlocation = models.CharField(max_length=100)
    endlocation = models.CharField(max_length=100)
    startlatitude = models.CharField(max_length=100)
    startlongitude = models.CharField(max_length=100)
    endlatitude = models.CharField(max_length=100)
    endlongitude = models.CharField(max_length=100)


class DeliveryRequest(models.Model):
    requestid = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    courier_partner = models.ForeignKey(Partner,on_delete=models.CASCADE,null=True, blank=True)
    package_name = models.CharField(max_length=100)
    package_type = models.CharField(max_length=70) 
    package_size = models.CharField(max_length=5)
    pickup_point = models.CharField(max_length=100)
    drop_point = models.CharField(max_length=100)
    pickup_latitude = models.CharField(max_length=200)
    pickup_longitude = models.CharField(max_length=200)
    drop_latitude = models.CharField(max_length=200)
    drop_longitude = models.CharField(max_length=200)
    deliveryinfo = models.CharField(max_length=200)
    status = models.CharField(max_length=50,default='requested')
    amount = models.CharField(max_length=5)
    payment_status = models.CharField(max_length=10)
    feedback = models.CharField(max_length=200)
    rate = models.CharField(max_length=20)





    

    







