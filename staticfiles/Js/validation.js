$("#button").click(function(){
  $("#username_errormessage").hide();
  $("#email_errormessage").hide();
  $("#password_errormessage").hide();
  var error_username=false;
  var error_mail=false;
  var error_password=false;
  $("#username").focusout(function(){
     check_username();
     
});
   $("#username").blur(function(){
            $(this).css("background-color", "#ffffff");
   });
  $("#email").focusout(function(){
     check_email();
     
});
  $("#password").focusout(function(){
     check_password();
     
});
  function check_username()  {
  var username_length=$("#username").val().length;
  if(username_length < 5 || username_length >20){
    $("#username_errormessage").html("should be betweet 5 to 20 characters");
    $("#username_errormessage").show();
    error_username=true;
      if(username_length==''){
        $("#username_errormessage").html("please enter your name");
    $("#username_errormessage").show();
      }
  }else{
     $("#username_errormessage").hide();
  }
 }

 function check_email()  {

  var pattern= new RegExp(/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/);
  if($("#email").val()==''){
      $("#email_errormessage").html("please enter your email");
      $("#email_errormessage").show();
  }
  else if (pattern.test($("#email").val())){
    $("#email_errormessage").hide();


  }else{
    $("#email_errormessage").html("invalid email address");
    $("#email_errormessage").show();
    error_mail=true;
  }
 }

 function check_password()  {
  var password=$("#password").val().length;
  if(password < 8){
    $("#password_errormessage").html("password contain atleast 8 characters");
    $("#password_errormessage").show();
    error_password=true;
    if(password=='')
      $("#password_errormessage").html("please enter your password");
      $("#password_errormessage").show();


  }else{
    $("#password_errormessage").hide(); 
     }
   }

   


});


