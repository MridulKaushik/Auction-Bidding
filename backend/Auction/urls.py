from django.urls import path, include
from .views import *

app_name = 'auction'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('auction/', UsersAuctionStatusView.as_view(), name='all'),
    path('auction/create/', CreateAuction.as_view(), name='createAuction'),
    path('auction/update/<int:pk>/', AuctionUpdateView.as_view(), name='updateAuction'),
    path('auction/delete/<int:pk>/', DeleteAuctionView.as_view(), name='deleteAuction'),
    path('auction/bid/<int:pk>/', PlaceBid.as_view(), name='placeBid'),
    path('auction/results/<int:pk>/', Results.as_view(), name='results'),
    path('auction/results/<int:pk>/winner/', AnnounceWinner.as_view(), name="declareWinner"),
]