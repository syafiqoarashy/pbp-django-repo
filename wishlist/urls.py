from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_data_xml
from wishlist.views import show_data_json
from wishlist.views import show_data_xml_id
from wishlist.views import show_data_json_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_data_xml, name='show_xml'),
    path('json/', show_data_json, name='show_json'),
    path('json/<int:id>', show_data_json_id, name='show_data_jason_id'),
    path('xml/<int:id>', show_data_xml_id, name='show_data_xml_id'),
]