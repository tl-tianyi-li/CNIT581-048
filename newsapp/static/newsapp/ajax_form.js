function getCookie(name) {
	// source: https://docs.djangoproject.com/en/3.2/ref/csrf/
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


if (!csrftoken || csrftoken== ""){
	alert("It seems like your browser doesn't have cookie enabled.")
}

// Default settings can be set globally by using the $.ajaxSetup() function.
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});




$(document).ready(function(){
	$("#signup_submit").click(function(e){
    console.log("clicked");
		// e.preventDefault();
		let mydata = {username: $("input[name=username]").val()};
		$.post(".",mydata,function(data, status){
			$("#response_server").text(data.post_data+" Status:"+ status);
      if(data.username_inuse){
        $("#signup_status").text("Username already in use, please try a different one.");
        console.log("user name in use")
        return false;
      }else{
        $("#signup_status").text("");
        console.log("user name not in use.");
        $('#signup_form').submit();
      }
		});
	});
	
});