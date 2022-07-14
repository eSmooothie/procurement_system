$(document).ready(function(e){
    $("#id_username").addClass("bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5");
    $("#id_password").addClass("bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5");

    $('#toggle_password').on('click', function(e){
        e.preventDefault();
        $(this).empty();
        var password_input_field = document.getElementById('id_password');
        if(password_input_field.type === "password"){
            password_input_field.type = "text";
            $(this).append("<img src=\"/static/images/icon/eye-slash-solid.svg\" class=\" h-4 w-4\" alt=\"eye-slash-solid\">");
        }else{
            password_input_field.type = "password";
            $(this).append("<img src=\"/static/images/icon/eye-solid.svg\" class=\" h-4 w-4\" alt=\"eye-solid\">")
        }
    });
});