function show_and_hide_password(id_input, img) {
    var input = document.getElementById(id_input);
    if ( input.type === "password" ) {
        input.type = "text";
        img.src = "../img/open_eye.png";
    }
    else {
	input.type = "password";
	img.src = "../img/closed_eye.png"
    }
    return ;
}
