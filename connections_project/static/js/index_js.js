$().ready(function(){
	$("#user_form").validate({
		rules: {
			firstname: "required",
			lastname: "required",
			email: {
				required: true,
				email: true
			},
			username: {
				required: true,
				minlength:2
			},
			password: {
				required: true,
				minlength:5
			},
			confirm_password: {
				required:true,
				minlength:5,
				equalTo: "#password"
			}
		},
		messages : {
			firstname: "Please enter the firstname",
			lastname: "Please enter the lastname",
			username: {
				required: "Please enter a username",
				minlength: "username should be atleast 2 characters long"
			},
			password: {
				required: "Please enter the password",
				minlength: "Password must be atleast 5 characters long"
			},
			confirm_password: {
				required: "Please enter the confirm password",
				minlength: "Password must be atleast 5 characters long",
				equalTo: "passwords do not match"
			}
		}
	});
});