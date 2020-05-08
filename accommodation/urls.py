from django.urls import path,re_path
from accommodation.views import index,details,create,submit,delete,update,delete_form


app_name = 'accommodation'



urlpatterns = [
    path('', view=index, name='list'),
    path('/<int:accommodation_id>/', view=details, name='details'),
    path('create', view=create, name='create'),
    path('submit', view=submit, name='submit'),
    path('delete/<int:accommodation_id>', view=delete, name='delete'),
    path('update/<int:accommodation_id>', view=update, name='update'),
    path('delete_form/<int:accommodation_id>', view=delete_form, name='delete_form')
]