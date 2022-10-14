from django.urls import path
from . import views

urlpatterns=[
    path('home',views.baabtra_home,name='home'),
    path('page2',views.page2,name='page2'),
    path('about',views.aboutus,name='aboutus'),
    path('css',views.css,name='css'),
    path('css2',views.css2,name='css2'),
    path('grid',views.grid,name='grid'),
    path('grid2',views.grid2,name='grid2'),
    path('flex',views.flex,name='flex'),
    path('bootstp',views.bootstp,name='flex'),
    path('homenew',views.homenew,name='homenew'),
    path('bootstrapgrid',views.bootstrpgrd,name='bootstrapgrid'),
    path('baabtranew',views.baabtra_newhome,name='baabtranewhome'),

]