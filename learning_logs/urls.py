from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_notes/<topic_id>', views.new_notes, name='new_notes'),
    path('edit_notes/<notes_id>', views.edit_notes, name='edit_notes'),
]