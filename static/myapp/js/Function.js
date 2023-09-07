function validateForm(count) {
    const elem = document.getElementById("form");

    var checkboxes = document.getElementsByName("hobby");
        var submit_hobby = [];

        for (var i = 0; i < checkboxes.length; i++) {
          if (checkboxes[i].checked) {
            submit_hobby.push(checkboxes[i].value);
          }
        }

        document
          .getElementById("submit_hobby")
          .value = submit_hobby.join(",");
    
    if (count === 1) {
        const ageInput = document.getElementById("input1");
        if (ageInput.value>30) {
            alert("나이를 입력해주세요.");
            return false;
        }
    } else if (count === 2) {
        const sexInputs = document.querySelectorAll("[name='sex']");
        let selectedSex = false;
        sexInputs.forEach(input => {
            if (input.checked) {
                selectedSex = true;
            }
        });
        if (!selectedSex) {
            alert("성별을 선택해주세요.");
            return false;
        }
    } else if (count === 3) {
        const jobInputs = document.querySelectorAll("[name='job']");
        let selectedJob = false;
        jobInputs.forEach(input => {
            if (input.checked) {
                selectedJob = true;
            }
        });
        if (!selectedJob) {
            alert("직업을 선택해주세요.");
            return false;
        }
    } else if (count === 4) {
        const schoolInput = document.querySelector("[name='school']");
        const majorInputs = document.querySelectorAll("[name='major']");
        
        if (!schoolInput.value) {
            alert("학교를 입력해주세요.");
            return false;
        }
        
        let selectedMajor = false;
        majorInputs.forEach(input => {
            if (input.checked) {
                selectedMajor = true;
            }
        });
        if (!selectedMajor) {
            alert("전공을 선택해주세요.");
            return false;
        }
    } else if (count === 5) {
        const mbtiInput1 = document.querySelectorAll("[name='mbti1']");
        const mbtiInput2 = document.querySelectorAll("[name='mbti2']");
        const mbtiInput3 = document.querySelectorAll("[name='mbti3']");
        const mbtiInput4 = document.querySelectorAll("[name='mbti4']");
    
        let selectedmbti1 = false;
        let selectedmbti2 = false;
        let selectedmbti3 = false;
        let selectedmbti4 = false;
    
        mbtiInput1.forEach(input => {
            if (input.checked) {
                selectedmbti1 = true;
            }
        });
    
        mbtiInput2.forEach(input => {
            if (input.checked) {
                selectedmbti2 = true;
            }
        });
    
        mbtiInput3.forEach(input => {
            if (input.checked) {
                selectedmbti3 = true;
            }
        });
    
        mbtiInput4.forEach(input => {
            if (input.checked) {
                selectedmbti4 = true;
            }
        });
    
        if (!(selectedmbti1 && selectedmbti2 && selectedmbti3 && selectedmbti4)) {
            alert("MBTI를 입력해주세요.");
            return false;
        }
    } else if (count === 6) {
        const armyInputs = document.querySelectorAll("[name='army']");
        let selectedArmy = false;
        armyInputs.forEach(input => {
            if (input.checked) {
                selectedArmy = true;
            }
        });
        if (!selectedArmy) {
            alert("군필 여부를 선택해주세요.");
            return false;
        }
    } else if (count === 7) {
        const heightInput = document.getElementById("input1");
        if (heightInput.value<140) {
            alert("키를 입력해주세요.");
            return false;
        }
    } else if (count === 8) {
        const bodyInputs = document.querySelectorAll("[name='body']");
        let selectedBody = false;
        bodyInputs.forEach(input => {
            if (input.checked) {
                selectedBody = true;
            }
        });
        if (!selectedBody) {
            alert("체형을 선택해주세요.");
            return false;
        }
    } else if (count === 9) {
        const eyesInputs = document.querySelectorAll("[name='eyes']");
        let selectedEyes = false;
        eyesInputs.forEach(input => {
            if (input.checked) {
                selectedEyes = true;
            }
        });
        if (!selectedEyes) {
            alert("눈동자 형태를 선택해주세요.");
            return false;
        }
    } else if (count === 10) {
        const faceInputs = document.querySelectorAll("[name='face']");
        let selectedFace = false;
        faceInputs.forEach(input => {
            if (input.checked) {
                selectedFace = true;
            }
        });
        if (!selectedFace) {
            alert("얼굴 형태를 선택해주세요.");
            return false;
        }
    } else if (count === 11) {
        const hobbyInputs = document.querySelectorAll("[name='hobby']");
        let selectedHobbyCount = 0;
        hobbyInputs.forEach(input => {
            if (input.checked) {
                selectedHobbyCount++;
            }
        });
        if (selectedHobbyCount === 0) {
            alert("취미를 최소한 하나 이상 선택해주세요.");
            return false;
        }
        else if (selectedHobbyCount > 3) {
            alert("취미는 3개까지만 선택할 수 있습니다.");
            return false;
        }
    } else if (count === 12) {
        const freeTextarea = document.getElementById("input2");
        if (!freeTextarea.value) {
            alert("자기소개를 입력해주세요.");
            return false;
        }
    } 
    // 다른 질문에 대한 유효성 검사도 추가하세요

    return true;
}

function createStr(count) {
    if(count==1) document.write("나이를 입력해주세요");
    else if(count==2) document.write("성별을 입력해주세요");
    else if(count==3) document.write("직업을 입력해주세요"); //대학생, 대학원생, 취준생, 직장인
    else if(count==4) document.write("학교와 학과를 입력해주세요"); //학교 인증 시스템 넣기
    else if(count==5) document.write("mbti를 입력해주세요");
    else if(count==6) document.write("군/미필 여부를 입력해주세요");
    else if(count==7) document.write("키를 입력해주세요"); //범위로(5단위)
    else if(count==8) document.write("체형을 입력해주세요"); //탭으로(마름, 보통, 통통, 근육)
    else if(count==9) document.write("유/무쌍을 입력해주세요"); //탭으로
    else if(count==10) document.write("얼굴상을 입력해주세요"); //뚜렷, 두부
    else if(count==11) {
        document.write("관심사를 선택해주세요<br>");
        document.write("최대 3가지까지만 선택 가능합니다.");
     } //탭으로
    else if(count==12) {
        document.write("자유로운 자기소개<br>");
        document.write("최소 10자의 자기소개를 적어주세요.<br>");
        document.write("자기소개를 길게 쓸수록 <br> 매칭확률이 높아집니다.");
    }
}

function create(count) {
    const elem= document.getElementById("form");
    if(count==1) {
        elem.innerHTML = "<input type=range min=20 max=31 name=age value=31 id=input1 size=10 required oninput=document.getElementById('output1').innerHTML=this.value;></input> \
                            <br><span id=output1></span>"
    }
    else if(count==2) {
        elem.innerHTML = "<input type=radio name=sex value=male id=1> <label for=1> 남성 </label>\
                <input type=radio name=sex value=female id=2> <label for=2> 여성 </label>"
    }
    else if(count==3) {
        elem.innerHTML = "<input type=radio name=job id=1 value=univstu> <label for = 1> 대학생 </label> \
                 <input type=radio name=job id=2 value=gradustu> <label for = 2> 대학원생 </label> \
                 <input type=radio name=job id=3 value=human > <label for = 3> 취준생 </label> \
                 <input type=radio name=job id=4 value=worker > <label for = 4> 직장인 </label> "
    }
    else if(count==4) {
        elem.innerHTML = "<input type=text name=school placeholder=OO대학교 size=10 required></input>\
        <br><br>\
        <input type=radio id=1 name=major value=liberal > <label for = 1> 문과대 </label>\
        <input type=radio id=2 name=major value=science> <label for = 2> 이과대 </label>\
        <input type=radio id=3 name=major value=education > <label for = 3> 사범대 </label>\
        <input type=radio id=4 name=major value=physical> <label for = 4> 체대 </label>\
        <input type=radio id=5 name=major value=art> <label for = 5> 미대 </label>\
        <input type=radio id=6 name=major value=entertain> <label for = 6> 예대 </label>\
        <input type=radio id=7 name=major value=music> <label for = 7> 음대 </label>\
        <input type=radio id=8 name=major value=medicine> <label for = 8> 의/약대 </label>\
        <input type=radio id=9 name=major value=special> <label for = 9> 특수대 </label> "
    }
    else if(count==5) {
        elem.innerHTML = "<input type=radio id=1 name=mbti1 value=e> <label for=1> E </label> \
        <input type=radio id=5 name=mbti1 value=i> <label for=5> I </label>\
        <input type=radio id=2 name=mbti2 value=s> <label for=2> S </label> \
        <input type=radio id=6 name=mbti2 value=n> <label for=6> N </label>\
        <input type=radio id=3 name=mbti3 value=f> <label for=3> F </label>\
        <input type=radio id=7 name=mbti3 value=t> <label for=7> T </label>\
        <input type=radio id=4 name=mbti4 value=j> <label for=4> J </label>\
        <input type=radio id=8 name=mbti4 value=p> <label for=8> P </label> "
    }
    else if(count==6) {
        elem.innerHTML = "<input type=radio id=1 name=army value=go > <label for=1> 군필 </label> \
                <input type=radio id=2 name=army value=nongo> <label for=2> 미필 </label>"
    }
    else if(count==7) {
        elem.innerHTML = "<input type=range min=139 max=200 name=height value=139 id=input1 size=10 required oninput=document.getElementById('output1').innerHTML=this.value;></input> \
        <br><span id=output1></span>"
        
    }
    else if(count==8) {
        elem.innerHTML = "<input type=radio id=1 name=body value=thin > <label for = 1> 마름 </label> \
                <input type=radio id=2 name=body value=normal> <label for = 2>  보통 </label>\
                <input type=radio id=3 name=body value=fat > <label for = 3>  통통 </label> \
                <input type=radio id=4 name=body value=muscle> <label for = 4>  탄탄 </label>"
    }
    else if(count==9) {
        elem.innerHTML = "<input type=radio id=1 name=eyes value=yes > <label for = 1> 유쌍 </label> \
        <input type=radio id=2 name=eyes value=no> <label for = 2>  무쌍 </label>"
    }
    else if(count==10) {
        elem.innerHTML = "<input type=radio id=1 name=face value=tubu > <label for = 1> 두부상 </label> \
        <input type=radio id=2 name=face value=arab> <label for = 2> 뚜렷상 </label>"
    }
   
    else if(count==11) {
        elem.innerHTML = "<input type=checkbox name=hobby id=1 value=exercise > <label for = 1> ⚽운동 </label> \
                <input type=checkbox name=hobby id=2 value=walk > <label for = 2> 🚶산책 </label>\
                <input type=checkbox name=hobby id=3 value=show > <label for = 3> 🎞️공연관람 </label> \
                <input type=checkbox name=hobby id=4 value=shopping > <label for = 4> 👜쇼핑 </label> \
                <input type=checkbox name=hobby id=5 value=money > <label for = 5> 💰재태크 </label> \
                <input type=checkbox name=hobby id=6 value=fashion > <label for = 6> 👔패션 </label>\
                <input type=checkbox name=hobby id=7 value=pet > <label for = 7> 🐈반려동물 </label> \
                <input type=checkbox name=hobby id=8 value=music > <label for = 8> 🎶음악감상 </label>\
                <input type=checkbox name=hobby id=9 value=book > <label for = 9> 📖독서 </label> \
                <input type=checkbox name=hobby id=10 value=trip > <label for = 10> ✈️여행 </label>\
                <input type=checkbox name=hobby id=11 value=cafe > <label for = 11> ☕카페 </label> \
                <input type=checkbox name=hobby id=12 value=game > <label for = 12> 🎮게임 </label>\
                <input type=checkbox name=hobby id=13 value=movie > <label for = 13> 🎥영화/드라마 </label>\
                <input type=checkbox name=hobby id=14 value=museum > <label for = 14> 🖼️전시관람 </label> \
                <input type=checkbox name=hobby id=15 value=musical > <label for = 15> 🤸‍♂️연극/뮤지컬 </label>\
                <input type=checkbox name=hobby id=16 value=drink > <label for = 16> 🍻술 </label> \
                <input type=checkbox name=hobby id=17 value=performane > <label for = 17> 🎹악기연주 </label>\
                <input type=checkbox name=hobby id=18 value=eat > <label for = 18> 🍜맛집 </label> \
                <input type=checkbox name=hobby id=19 value=cook > <label for = 19> 🍳요리 </label>"
    }
    else if(count==12) {
        elem.innerHTML = "<br> <textarea name=free id=input2 cols=40 rows=10> </textarea> \
        <p> 제출하면 자기소개가 완료됩니다! </p>"
    }
}

function major() {
    const elem= document.getElementById("form0");
    elem.innerHTML = "<input type=text id=input placeholder=학과 size=10 required></input> "
}