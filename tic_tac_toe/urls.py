from django.conf.urls import include, url

import tic_tac_toe.views as base_views

urlpatterns = [
    url(r'^$', base_views.PlayMove.as_view(), name='play_move'),
]
