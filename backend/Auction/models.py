from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Auction(models.Model):
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_name = models.CharField(max_length=255)
    agent = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=False, related_name="user_won")

    class Meta:
        ordering = ['-pk']

    def is_Auction_Completed(self):
        return timezone.localtime().strftime('%b. %d, %Y, %I:%M %p') > str(self.end_time)

class Bid(models.Model):
    auction = models.ForeignKey(
        Auction, on_delete=models.CASCADE, related_name='bid')
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bidder')
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    bid_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-amount"]

    def __str__(self):
        return f"{self.bidder.get_username()} bidding on {self.auction.item_name}"
