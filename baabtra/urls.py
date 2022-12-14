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
    path('chegg',views.chegg,name='chegg'),
    path('javascript',views.javascript,name='javascript'),
    path('while1',views.while1,name='while1'),
    path('doc',views.document,name='doc'),
    path('operator',views.operator,name='ope'),
    path('array',views.array,name='array'),
    path('todo',views.todo,name='todo'),
    path('qury',views.jquery,name='query'),
    path('j_add',views.jadd,name='jadd'),
    path('jqury2',views.jquery2,name='jqury2'),
    path('traverse',views.traverse,name='traverse'),
    path('jquerysignup',views.j_query_signup,name='jquerysignup'),
    path('test_css',views.test_css,name='test_css'),
    path('test_images',views.test_images,name='test_images'),
    path('test_about',views.test_about,name='test_about'),

]