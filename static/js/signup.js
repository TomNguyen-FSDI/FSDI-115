// const togglePassword = document.querySelector('#togglePassword');
// const password = document.querySelector('#id_password');
var eye_toggled = true;
var eye_toggled2 = true;
type = 'password';

togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    if(eye_toggled){
        $('#togglePassword').removeClass("fa-eye-slash");
        $('#togglePassword').addClass("fa-eye");
        type = 'text'
        eye_toggled=false;
    } else{
        $('#togglePassword').removeClass("fa-eye");
        $('#togglePassword').addClass("fa-eye-slash");
        type = 'password'
        eye_toggled=true;
    }
    $('#id_password1').attr('type', type);
});

togglePassword2.addEventListener('click', function (e) {
    // toggle the type attribute
    if(eye_toggled2){
        $('#togglePassword2').removeClass("fa-eye-slash");
        $('#togglePassword2').addClass("fa-eye");
        type = 'text'
        eye_toggled2=false;
    } else{
        $('#togglePassword2').removeClass("fa-eye");
        $('#togglePassword2').addClass("fa-eye-slash");
        type = 'password'
        eye_toggled2=true;
    }
    $('#id_password2').attr('type', type);
});