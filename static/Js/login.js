$(document).ready(function(){
$("form").submit(function(){
  
  
  
 //$("#form").val(){

  var x=0;
 var pattern= new RegExp(/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/);
  if($("#email").val()==''){ 
    //alert("enter email")
     $("#email_errormessage").text("please enter your email");
      $("#email_errormessage").show();
      x++;
   } 
    else if(pattern.test($("#email").val())){
      $("#email_errormessage").hide();


  }  else{
    $("#email_errormessage").html("invalid email address");
    $("#email_errormessage").show();
    //error_mail=true;
    x++;
  }
     
if($("#password").val()=='')
  { 
    $("#password_errormessage").text("please enter your password");
    $("#password_errormessage").show();
    x++;
  }//alert("enter password")
    else if(password < 8)
    {
      $("#password_errormessage").text("password contain atleast 8 characters");
      $("#password_errormessage").show();
      x++;
     //err_password=true;
     //check_password();
    }
     
    else
  {
       $("#password_errormessage").hide(); 
  }

    
  if (x > 0) {
    return false;
  }
  else{
     return true;
  }
});

});


