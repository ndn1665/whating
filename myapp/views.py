from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Info
from myproject import settings
import requests
from django.template import loader
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden

# Create your views here.
  
count = 0
@csrf_exempt
def index(request):
   return redirect("/home")



def kakaologin(request):
    context = {'check':False}
    if request.session.get('access_token'): #만약 세션에 access_token이 있으면(==로그인 되어 있으면)
        return redirect("/home") #로그인 되어있으면 home페이지로

    return render(request,"myapp/kakaologin.html",context)#로그인 안되어있으면 로그인페이지로

def kakaoLoginLogic(request):
    _restApiKey = '60010e5242c371826d538b43def648c3' # 입력필요
    _redirectUrl = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = '60010e5242c371826d538b43def648c3' # 입력필요
    _redirect_uri = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    print()
    print(_result)
    print()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    
    return redirect("/home") #로그인 완료 후엔 home페이지로

def kakaoLogout(request):
    
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    
    print(_result.get('id'))#액세스 토큰은 바뀌어도 id값은 안바뀌니 이것으로 조회 가능
    if _result.get('id'):
        
        del request.session['access_token']
        return render(request, 'myapp/loginoutsuccess.html')
    else:
        return render(request, 'myapp/logouterror.html')


@csrf_exempt
def home(request):
    logged = 0
    
    access_token = request.session.get("access_token",None)
    if access_token:
        logged = 1

    context = {'logged':logged}
    return render(request, "myapp/home.html",context)

@csrf_exempt
def meeting(request):
    #만약 자기소개 정보가 없으면
    #return redirect('/my/1')
    access_token = request.session.get("access_token",None)
    if access_token == None: #로그인 안돼있으면
        return render(request,"myapp/kakaologin.html") #로그인 시키기
    global count
    if request.method == "POST": # /home/meeting페이지로 인원 선택한 정보 전달
        peoplenum = ''
        peoplenum = request.POST.get('submit_peoplenum') #인원 선택 정보 추출
        q = Info.objects.create(peoplenums=peoplenum)
        q.save()
        count = q.id
        print(count)
        return redirect("/meeting2")# /home/meeting2로 페이지 전달
    return render(request, "myapp/meeting.html")


@csrf_exempt
def meeting2(request):
    
    access_token = request.session.get("access_token",None)
    if access_token == None: #로그인 안돼있으면
        return render(request,"myapp/kakaologin.html") #로그인 시키기
    global count
    if request.method == "POST": # /home/meeting2 로 선호 직업, 장소, 나이 전달
        job = request.POST.get('submit_job')
        age = request.POST.get('submit_age')
        print(job)
        print(age)
        q = Info.objects.latest('id')
        q.jobs = job
        q.ages = age
        q.save()
        return redirect("/good/")

    count += 1
    return render(request, "myapp/meeting2.html")

@csrf_exempt
def good(request):

    return render(request, "myapp/good.html")

@csrf_exempt
def go(request):

    return render(request, "myapp/go.html")


@csrf_exempt
def alonechoose(request):

    return render(request, "myapp/alonechoose.html")
@csrf_exempt
def alonechoose2(request):

    return render(request, "myapp/alonechoose2.html")
@csrf_exempt
def army(request):

    return render(request, "myapp/army.html")
@csrf_exempt
def body(request):

    return render(request, "myapp/body.html")
@csrf_exempt
def eyes(request):

    return render(request, "myapp/eyes.html")
@csrf_exempt
def height(request):

    return render(request, "myapp/height.html")
@csrf_exempt
def hobby(request):

    return render(request, "myapp/hobby.html")
@csrf_exempt
def kakao(request):
    #db에서 매칭된 상대방 카카오아이디 가져오기
    return render(request, "myapp/kakao.html")
@csrf_exempt
def major(request):

    return render(request, "myapp/major.html")
@csrf_exempt
def mbti(request):

    return render(request, "myapp/mbti.html")

myinfo_arr = {}
@csrf_exempt
def myinfo(request):
    access_token = request.session.get("access_token",None)
    if access_token == None: #로그인 안돼있으면
        return render(request,"myapp/kakaologin.html") #로그인 시키기
    
    account_info = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"}).json()
    email = account_info.get("kakao_account", {}).get("email") # email이 있으면 email반환 없으면 빈칸 반환
    nickname = account_info.get("kakao_account", {}).get("nickname")
    context = {'email' : email, 'nickname':nickname}
    context.update(myinfo_arr)
    print(email)
    print(nickname)
    
    return render(request, "myapp/myinfo.html",context)
@csrf_exempt
def success(request):

    return render(request, "myapp/success.html")

@csrf_exempt
def fail(request):

    return render(request, "myapp/fail.html")

@csrf_exempt
def youinfo(request):

    return render(request, "myapp/youinfo.html")


def is_valid_transition(current_page, requested_page):
    # 요청한 페이지가 현재 페이지에서의 올바른 다음 페이지인지 확인
    requested_page_int = int(requested_page)
    if requested_page_int == current_page + 1 or current_page == requested_page_int :
        return True
    return False

@csrf_exempt
def my(request,id):
    access_token = request.session.get("access_token",None)
    if access_token == None: #로그인 안돼있으면
        return render(request,"myapp/kakaologin.html") #로그인 시키기
    
    if request.method == "GET":
        if int(id) == 1:
            if request.session.get('current_page'):
                del request.session['current_page']
        
        current_page = request.session.get('current_page', 0)
        if int(id) < current_page:
            current_page = int(id)

        if not is_valid_transition(current_page, id):
            # 올바른 페이지 이동이 아니면 거부
            return HttpResponseForbidden("Forbidden")

        # 페이지 이동을 허용하고, 세션 업데이트
        request.session['current_page'] = int(id)

    
    #자기소개 한거 있으면 자기소개 내용 불러오고 choose페이지로 넘어가게
    global myinfo_arr
    index = int(id) + 1
    if request.method == "GET" and int(id) == 13: #13페이지까지 이동하고 14페이지면 choose로 이동
        return redirect("/go") 
    if request.method == "POST":
        if int(id) == 1:
            age = request.POST.get("age")
            myinfo_arr['age'] = age
        elif int(id) == 2:
            sex = request.POST.get("sex")
            myinfo_arr['sex'] = sex
        elif int(id) == 3:
            job = request.POST.get("job")
            myinfo_arr['job'] = job
        elif int(id) == 4:
            school = request.POST.get("school")
            major =  request.POST.get("major")
            graduate = school + major
            myinfo_arr['graduate'] = graduate
        elif int(id) == 5:
            mbti = request.POST.get("mbti")
            myinfo_arr['mbti'] = mbti
        elif int(id) == 6:
            army = request.POST.get("army")
            myinfo_arr['army'] = army
        elif int(id) == 7:
            height = request.POST.get("height")
            myinfo_arr['height'] = height
        elif int(id) == 8:
            body = request.POST.get("body")
            myinfo_arr['body'] = body
        elif int(id) == 9:
            eyes = request.POST.get("eyes")
            myinfo_arr['eyes'] = eyes
        elif int(id) == 10:
            face = request.POST.get("face")
            myinfo_arr['face'] = face
        elif int(id) == 11:
            hobby = request.POST.get("hobby")
            myinfo_arr['hobby'] = hobby
        elif int(id) == 12:
            free = request.POST.get("free")
            myinfo_arr['free'] = free
        else:
            index = 1
        
        return redirect(f"/my/{index}") #다음페이지로 이동
    #if db에 자기소개 정보있으면 return redirect("/choose")
    
    context = {'count':int(id)}

    return render(request, "myapp/my.html",context)
    
'''
이런 방식을 사용해도 된다
def my(request):
    article = 'my'
    template = loader.get_template(myapp/my.html)
    context = {"article":article}
    return HttpResponse(template.render(context,request))

'''
@csrf_exempt
def you(request):
    article = 'you'
    context = {"article":article}
    return render(request, "myapp/you.html", context)

@csrf_exempt
def choose(request):
    #홍대축제에서 만나기 누르면 choose에서는 무조건 meeting으로 redirect
    return render(request, "myapp/choose.html")
      
@csrf_exempt
def matching(request):
    article = 'matching'
    context = {"article":article}
    return render(request, "myapp/matching.html", context)
    
@csrf_exempt
def matching2(request):

    return render(request, "myapp/matching2.html")
@csrf_exempt
def matching3(request):

    return render(request, "myapp/matching3.html")
@csrf_exempt
def error(request):

    return render(request, "myapp/error.html")

@csrf_exempt
def use(request):

    return render(request, "myapp/use.html")

@csrf_exempt
def result(request):
    #db에서 신청한 매칭인원 정보를 받아와서 html에 넘겨서 특정 매칭만 결과확인할 수 있도록 하기
    context = {'matched' : 1}#매칭되면 matched 값 1 안되면 None
    access_token = request.session.get("access_token",None)
    if access_token == None: #로그인 안돼있으면
        return render(request,"myapp/kakaologin.html") #로그인 시키기
    return render(request,"myapp/result.html",context)
    
@csrf_exempt
def menu(request):

    return render(request,"myapp/menu.html")