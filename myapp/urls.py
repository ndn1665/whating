from django.views.static import serve
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.index),

    path('kakaoLoginLogic/', views.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect),
    path('kakaoLogout/', views.kakaoLogout), 

    path('home/',views.home, name='home'),
    path('matching/',views.matching,name='matching'),
    path('matching2/',views.matching2,name='matching2'),
    path('matching3/',views.matching3,name='matching3'),
    path('error/',views.error,name='error'), #08.22 새로만든 html
    path('result/',views.result,name='result'),
    path('menu/',views.menu,name='menu'),
    path('meeting/',views.meeting,name='meeting'),
    path('meeting2/',views.meeting2,name='meeting2'),
    path('good/',views.good,name='good'),
    path('fail/',views.fail,name='fail'),
    path('go/',views.go,name='go'),
    path('use/',views.use,name='use'),
    
    path('my/<id>/',views.my,name='my'),
    path('choose/',views.choose,name='choose'),
    path('kakaologin/',views.kakaologin,name='kakaologin'),
    path('kakao/',views.kakao,name='kakao'),
    path('alonechoose/',views.alonechoose,name='alonechoose'),
    path('alonechoose2/',views.alonechoose2,name='alonechoose2'),
    path('army/',views.army,name='army'),
    path('body/',views.body,name='body'),
    path('eyes/',views.eyes,name='eyes'),
    path('height/',views.height,name='height'),
    path('hobby/',views.hobby,name='hobby'),
    path('major/',views.major,name='major'),
    path('mbti/',views.mbti,name='mbti'),
    path('myinfo/',views.myinfo,name='myinfo'),
    path('success/',views.success,name='success'),
    path('youinfo/',views.youinfo,name='youinfo'),
    path('kakaoid/',views.kakaoid,name='kakaoid')
]