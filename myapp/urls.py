from django.views.static import serve
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import AboutView
urlpatterns = [
    path('',views.index),

    path('kakaoLoginLogic/', views.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect),
    path('kakaoLogout/', views.kakaoLogout), 

    path('home/',views.home, name='home'),
    path('matching/', AboutView.as_view(template_name = "myapp/matching.html"),name='matching'),
    path('matching2/',AboutView.as_view(template_name = "myapp/matching2.html"),name='matching2'),
    path('matching3/',AboutView.as_view(template_name = "myapp/matching3.html"),name='matching3'),
    path('error/',AboutView.as_view(template_name = "myapp/error.html"),name='error'), #08.22 새로만든 html
    path('result/',views.result,name='result'),
    path('menu/',AboutView.as_view(template_name = "myapp/menu.html"),name='menu'),
    path('meeting/',views.meeting,name='meeting'),
    path('meeting2/',views.meeting2,name='meeting2'),
    path('good/',AboutView.as_view(template_name = "myapp/good.html"),name='good'),
    path('fail/',AboutView.as_view(template_name = "myapp/fail.html"),name='fail'),
    path('go/',AboutView.as_view(template_name = "myapp/go.html"),name='go'),
    path('use/',AboutView.as_view(template_name = "myapp/use.html"),name='use'),
    
    path('my/<id>/',views.my,name='my'),
    path('choose/',AboutView.as_view(template_name = "myapp/choose.html"),name = 'choose'),
    path('kakaologin/',views.kakaologin,name='kakaologin'),
    path('kakao/',views.kakao,name='kakao'),
    path('alonechoose/',AboutView.as_view(template_name = "myapp/alonechoose.html"),name='alonechoose'),
    path('alonechoose2/',AboutView.as_view(template_name = "myapp/alonechoose2.html"),name='alonechoose2'),
    path('army/',AboutView.as_view(template_name = "myapp/army.html"),name='army'),
    path('body/',AboutView.as_view(template_name = "myapp/body.html"),name='body'),
    path('eyes/',AboutView.as_view(template_name = "myapp/eyes.html"),name='eyes'),
    path('height/',AboutView.as_view(template_name = "myapp/height.html"),name='height'),
    path('hobby/',AboutView.as_view(template_name = "myapp/hobby.html"),name='hobby'),
    path('major/',AboutView.as_view(template_name = "myapp/major.html"),name='major'),
    path('mbti/',AboutView.as_view(template_name = "myapp/mbti.html"),name='mbti'),
    path('myinfo/',views.myinfo,name='myinfo'),
    path('success/',AboutView.as_view(template_name = "myapp/success.html"),name='success'),
    path('youinfo/',AboutView.as_view(template_name = "myapp/youinfo.html"),name='youinfo'),
    path('kakaoid/',views.kakaoid,name='kakaoid')
]