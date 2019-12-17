from django.conf.urls import url

from furniture import views

urlpatterns = [

    url(r'^index/', views.index, name="index"),

    url(r'^register/', views.register, name='register'),

    url(r'^login/', views.login, name="login"),

    url(r'^logout/', views.logout, name='logout'),

    url(r'^mine/', views.mine, name="mine"),

    url(r'^mycart/', views.mycart, name="mycart"),

    url(r'^store/', views.store, name='store'),

    url(r'^AFurn/(?P<id>\d+)', views.AFurn, name='AFurn'),

    url(r'^myFurn/', views.myFurn, name='myFurn'),

    url(r'^addFurn/', views.addFurn, name='addFurn'),

    url(r'^editFurn/(?P<id>\d+)', views.editFurn, name='editFurn'),

    url(r'^editf/(?P<id>\d+)', views.editf, name='editf'),

    url(r'^deleteFurn/(?P<id>\d+)', views.deleteFurn, name='deleteFurn'),

    url(r'^showBed/', views.showBed,name='showBed'),

    url(r'^showFood/', views.showFood,name='showFood'),

    url(r'^showRobe/', views.showRobe,name='showRobe'),

    url(r'^showLocker/', views.showLocker,name='showLocker'),

    url(r'^addOrderitem/(?P<fid>\d+)', views.addOrderitem, name='addOrderitem'),

    url(r'^deleteorderitem/(?P<id>\d+)', views.deleteorderitem, name='deleteorderitem'),

    url(r'^addData/', views.addData,name='addData'),

    url(r'^pay/', views.pay,name='pay'),

    url(r'^sale/', views.sale,name='sale'),

    url(r'^look/', views.look,name='look'),

    url(r'^paySuccess/', views.paySuccess,name='paySuccess'),


]
