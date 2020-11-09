let state = false;  //비밀번호 보이게 하는 버튼
function toggle() {
    if (state) {
        document.getElementById("password").setAttribute("type", "password");
        document.getElementById("eye").style.color = '#7a797e';
        state = false;
    } else {
        document.getElementById("password").setAttribute("type", "text");
        document.getElementById("eye").style.color = '#5887ef';
        state = true;
    }
}
