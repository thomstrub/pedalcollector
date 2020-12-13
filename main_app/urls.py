from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('boards/', views.boards_index, name='index'),
    path('boards/<int:board_id>/', views.boards_detail, name='detail'),
    path('boards/create/', views.BoardCreate.as_view(), name='boards_create'),
    path('boards/<int:pk>/update/', views.BoardUpdate.as_view(), name='boards_update'),
    path('boards/<int:pk>/delete/', views.BoardDelete.as_view(), name='boards_delete'),
    path('boards/<int:board_id>/add_session/', views.add_session, name='add_session'),
    path('boards/<int:board_id>/assoc_pedal/<int:pedal_id>/', views.assoc_pedal, name='assoc_pedal'),
    path('boards/<int:board_id>/delete_assoc_pedal/<int:pedal_id>/', views.delete_assoc_pedal, name='delete_assoc_pedal'),
    path('pedals/', views.PedalList.as_view(), name='pedals_index'),
    path('pedals/<int:pk>/', views.PedalDetail.as_view(), name='pedals_detail'),
    path('pedals/create/', views.PedalCreate.as_view(), name='pedals_create'),
    path('pedals/<int:pk>/update/', views.PedalUpdate.as_view(), name='pedals_update'),
    path('pedals/<int:pl>/delete/', views.PedalDelete.as_view(), name='pedals_delete'),
]