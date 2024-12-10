from django.contrib import admin
from django.urls import path
from lists import views

urlpatterns = [
    path('', views.showActiveLists, name="lists"),
    path('archive', views.showArchivedLists, name="lists-archive"),
    path('add/list', views.addListForm, name="create-list"),
    path('edit/list/<str:item_id>', views.editListForm, name="edit-list"),
    path('view/list/<str:item_id>', views.showList, name="view-list"),
    path('delete/list/<str:item_id>', views.deleteList, name="delete-list"),
    path('add/list-item/<str:item_id>', views.addListItemForm, name="create-list-item"),
    path('edit/list-item/<str:item_id>', views.editListItemForm, name="edit-list-item"),
    path('toggle-status/list-item/<str:item_id>', views.toggleStatusListItemForm, name="edit-list-item"),
    path('delete/list-item/<str:item_id>', views.deleteListItem, name="delete-list-item"),
]   