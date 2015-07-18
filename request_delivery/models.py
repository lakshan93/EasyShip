from django.db import models

class Request_delivery (models.Model):
	item_name = models.CharField(max_length=100)
	item_size = models.CharField(max_length=25)
	item_image = models.ImageField(upload_to='images/', null=True)
	item_weight = models.PositiveIntegerField()
	from_location = models.CharField(max_length=100)
	to_location = models.CharField(max_length=100)
	date = models.DateField()


class Delivery_details(models.Model):
	request_delivery_info = models.ForeignKey(Request_delivery)
	request_user_id = models.ForeignKey(User_auth)
	picked_user_id = models.ForeignKey(User_auth)
	picked_date = models.DateField()
	delivered_date = models.DateField()