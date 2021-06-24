// const togglePassword = document.querySelector('#togglePassword');
// const password = document.querySelector('#id_password');
var eye_toggled1 = true;
var eye_toggled2 = true;
var eye_toggled3 = true;
var toggle_id_name1 = '#id_old_password';
var toggle_id_name2 = '#id_new_password1';
var toggle_id_name3 = '#id_new_password2';
var div_id_name1 = '#togglePassword';
var div_id_name2 = '#togglePassword2';
var div_id_name3 = '#togglePassword3';

function clear_text (is_eye_icon, field_name, div_id_name) {
    // toggle the type attribute
    if(is_eye_icon){
        $(div_id_name).removeClass("fa-eye-slash");
        $(div_id_name).addClass("fa-eye");
        type = 'text'
        $(field_name).attr('type', type);
        return false;
    } else{
        $(div_id_name).removeClass("fa-eye");
        $(div_id_name).addClass("fa-eye-slash");
        type = 'password'
        $(field_name).attr('type', type);
        return true;
    }
}

togglePassword.addEventListener('click', function (){
    eye_toggled1 = clear_text(eye_toggled1, toggle_id_name1, div_id_name1);
});

togglePassword2.addEventListener('click', function (){
    eye_toggled2 = clear_text(eye_toggled2, toggle_id_name2, div_id_name2);
});

togglePassword3.addEventListener('click', function (){
    eye_toggled3 = clear_text(eye_toggled3, toggle_id_name3, div_id_name3);
});