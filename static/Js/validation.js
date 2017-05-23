$(document).ready(function(){
$("form").submit(function(){
  
var x=0;


var username_length=$("#username").val().length;

$("#username").keyup(function() {
    var text = $(this).val();
    text = processText(text);
    $("#email").val(text);
});
  qwer=$("#username").val();
   console.log(name);

  if($("#username").val()=='')
  { 
      $("#username_errormessage").text("please enter your name");
      $("#username_errormessage").show()
      x++;
  } 
  else if(username_length < 5 || username_length >20)
  {
      $("#username_errormessage").text("should be betweet 5 to 20 characters");
      $("#username_errormessage").show();
      x++;
  } 
  else
  {
      $("#username_errormessage").hide();
  }
 
var pattern= new RegExp(/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/);
  if($("#email").val()=='')
  { 
      $("#email_errormessage").text("please enter your email");
      $("#email_errormessage").show();
      x++;
  } 
    else if(pattern.test($("#email").val()))
  {
      $("#email_errormessage").hide();

  }  
  else
  {
      $("#email_errormessage").text("invalid email address");
      $("#email_errormessage").show();
      x++;
  };

  var password=$("#password").val().length;
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
  }
     
  else
  {
       $("#password_errormessage").hide(); 
  }

   function check_password()  
  {
   var password=$("#password").val().length;
  if(password < 8)
  {
    $("#password_errormessage").text("password contain atleast 8 characters");
    $("#password_errormessage").show();
    x++;
  
    if(password==''){


      $("#password_errormessage").html("please enter your password");
      $("#password_errormessage").show();
      x++;
  }
  }
  else
  {
      $("#password_errormessage").hide(); 
  }
  
  } 

var gen=$('input[name=gender]:checked').val();

    if (gen==undefined)
    {
        $("#radio").html("please select gender");
        $("#radio").show();
        x++;
    }
    if($('input[name=gender]:checked').length>0)  
    {
        $("#radio").hide();
   
    }



    if($('input[type=checkbox]:checked').length == 0)
    {
       $("#int").text("select the field");
       $("#int").show();
       x++;
    }
    else
    {
       $("#int").hide(); 
    }

mydropdown = $('#country').val();
//alert(mydropdown);
    if (mydropdown == '')
    {
       $("#cou").text("select your country");
       $("#cou").show();
       x++
     }
    else
    {
       $("#cou").hide();
    }
 
    if (x > 0) 
    {
       return false;
    }
    else
    {
       return true;
    }

});

});
 


 





