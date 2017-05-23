$(function(){
 
  $("#email_errormessage").hide();
  $("#password_errormessage").hide();

  var error_mail=false;
  var error_password=false;

  $("#email").focusout(function(){
     check_email();
     
});
  $("#password").focusout(function(){
     check_password();
     
});
  function check_email()  {
  var pattern= new RegExp(/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/);
  if (pattern.test($("#email").val())){
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
    $("#password_errormessage").html("wrong password");
    $("#password_errormessage").show();
    error_password=true;


  }else{
    $("#password_errormessage").hide(); 
     }
   }




         
         

});

