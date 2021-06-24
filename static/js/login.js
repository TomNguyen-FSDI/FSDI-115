// const togglePassword = document.querySelector('#togglePassword');
// const togglePassword2 = document.querySelector('#togglePassword2')
// const password = document.querySelector('#id_password');
var eye_toggled = true;
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
    $('#id_password').attr('type', type);
});

