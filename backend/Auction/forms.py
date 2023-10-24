from django.forms import ModelForm, DateTimeInput
from .models import Auction, Bid

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ('start_time', 'end_time', 'price', 'item_name')
        widgets = {
         'start_time': DateTimeInput(format='%m/%d/%y %H:%M', attrs={'type':'datetime-local'}),
         'end_time': DateTimeInput(format='%m/%d/%y %H:%M', attrs={'type':'datetime-local'})  
        }

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']