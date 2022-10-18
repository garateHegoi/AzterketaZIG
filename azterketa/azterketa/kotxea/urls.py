from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('kotxelista/',views.kotxelista,name='kotxea'),
    path('kotxelista/add/',views.add,name='add'),
    path('kotxelista/add/addrecord/',views.addrecord,name='addrecord'),
    path('kotxelista/delete/<int:id>',views.delete,name='delete'),
    path('kotxelista/update/<int:id>',views.update,name='update'),
    path('kotxelista/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('kotxelista/addPer/',views.addPer,name='addPer'),
    path('kotxelista/addPer/addrecordPer/',views.addrecordPer,name='addrecordPer'),
    path('kotxelista/deletePer/<int:id>',views.deletePer,name='deletePer'),
]