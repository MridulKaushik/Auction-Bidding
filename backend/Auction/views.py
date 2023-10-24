from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Auction, Bid
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .forms import *
User = get_user_model()


class HomePage(TemplateView):
    template_name = 'base.html'


class UsersAuctionStatusView(ListView):
    model = Auction
    template_name = 'auction_list.html'
    context_object_name = 'auctions'

    def get_queryset(self):
        return Auction.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # now = timezone.localtime().strftime('%b. %d, %Y, %I:%M %p')
    #     # if (now[21:] == 'PM' or now[21:] == 'pm') and int(now[15:17])!= 12:
    #     #     now = now[:15] + str(int(now[15:17]) + 12) + now[17:]
    #     # print(now)
    #     context['now'] = timezone.localtime().strftime('%b. %d, %Y, %I:%M %p')
    #     print(timezone.localtime())
    #     print(timezone.now())
    #     return context


class CreateAuction(CreateView):
    model = Auction
    form_class = AuctionForm
    template_name = 'auction_Form.html'
    success_url = reverse_lazy('auction:all')


class AuctionUpdateView(UpdateView):
    model = Auction
    form_class = AuctionForm
    template_name = 'update_auction.html'
    success_url = reverse_lazy('auction:all')


class DeleteAuctionView(DeleteView):
    model = Auction
    template_name = 'delete_auction.html'
    success_url = reverse_lazy('auction:all')


class PlaceBid(CreateView):
    model = Bid
    form_class = BidForm
    template_name = 'bid_form.html'

    def form_valid(self, form):
        auction_item = get_object_or_404(Auction, pk=self.kwargs['pk'])

        bid = form.save(commit=False)
        bid.auction = auction_item
        bid.bidder = self.request.user
        bid.save()

        if bid.amount > auction_item.price:
            auction_item.price = bid.amount
            auction_item.agent = self.request.user
            auction_item.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('auction:all')


class Results(DetailView):
    model = Auction

    def get_queryset(self):
        auction = Auction.objects.get(pk=self.kwargs['pk'])
        if auction is not None:
            return reverse_lazy('auction:declareWinner', auction)


class AnnounceWinner(DetailView):
    model = User
    template_name = "announce_winner.html"
    context_name = "user_won"