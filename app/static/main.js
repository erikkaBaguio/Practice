function register(){
	var valueName = $('input[name="name"]').val()
	var valueUsername = $('input[name="username"]').val()
	var valuePass = $('input[name="password"]').val()
	console.log(valueName, valueUsername, valuePass);

	$.ajax({
		type: "POST",
		url: "/",
		data: {name:valueName, username:valueUsername, pass:valuePass},
		success: function(resp){
			console.log(resp.status);

				$("#results").html('<p>successfully register ' + valueName + '</p>');

				// $("input").val("")	
			
		},
		error: function(error){
			console.log(error);
		},
	});
}