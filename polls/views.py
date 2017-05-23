from django.shortcuts import render,redirect, render_to_response
#from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
#from social_auth.backends import get_backend
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib.auth import login as auth_login
#from social_django.views import auth, complete, disconnect, _do_login
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import authenticate
from social.backends.facebook import FacebookOAuth2
from polls.models import course
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth

# Create your views here.dfbdf
def home(request):
	print "I am here"
	
	return render(request,'home.html')
def signup(request):
	
	if request.method == 'POST':
		print "signup post"
		first_name = request.POST.get('username', None)
		username = request.POST.get('email',None)
		print username
		email = request.POST.get('email',None)
		print email
		password = request.POST.get('password',None)
		gender = request.POST.get('gender',None)
		intrest = request.POST.getlist('intrest',None)
		print intrest		
		intrest=[int(i) for i in intrest]
		print intrest
		#intr="intrest" in request.POST
		country = request.POST.get('country',None)
		print username
		print email
		print password
		if username and email !='':
			print "save"
			emailcount=User.objects.filter(email=email).count()
			
			if  emailcount>0:
				print"duplicate"
				data="email is already taken"
				context={'data':data}
				return render(request,'signup.html',context)
			else:
				user = User.objects.create_user(username,email,password)
				register = course(first_name=first_name,name=first_name, email=email, password=password, gender=gender, intrest=intrest,country=country)
				register.save()	
				user.username=email
				user.first_name =first_name			
				user.save()
				messages.success(request, "Successfully Registered")

				print "success"
				return redirect('/login/')
	else:
		return render(request,'signup.html')
def login(request):
	if request.user.is_authenticated():
		return redirect('/userpage/')
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		print user
		if user is not None:
			auth_login(request, user)
			return redirect('/userpage/')
		else:
			print "bye"
			#field="please check your email/password"
			#context={'field':field};
			messages.success(request, "please check your email/password")
			return HttpResponseRedirect(request.path)
			 
	else:    
		return render(request,'login.html')

def forgot(request):

		if request.method == 'POST':
			print "hello"
			email = request.POST['email']
			user=authenticate(username=email)
			print user
			emailcount=User.objects.filter(email=email).count()
			if  emailcount>0 and email!='':
	            
				send_mail('hello','<a href="http://127.0.0.1:8000/reset/"' ,'rashokmpi@gmai.com',[email], fail_silently=False)
				print "hhhh"
				return redirect('/login/')
			else:	
				print"duplicate"
				
				data="please enter a correct email"
				context={'data':data} 
				return render(request,'forgotpassword.html',context)

		else:			
			return render(request,'forgotpassword.html')

def reset(request):
	
	if request.method == 'POST':
		password=request.POST.get('password',None)
		resetpassword=request.POST.get('repassword',None)
		
		if password==resetpassword and password!=''and resetpassword!='':
			u = User.objects.get(username='rashokmpi@gmail.com')
			u.set_password(password)
			u.save()
			print password
			print u
			return redirect('/login/')

		else:
			return redirect('/signup/')
        
	else:
		return render(request,'resetpassword.html')


def userpage(request):
	if request.user.is_authenticated(): 
		return render(request,'userpage.html')
	else:
	    return redirect('/login/')	
def logout(request):
	print "logout"
	auth_logout(request)
	return render(request,'logout.html')


def loginfb(request):
	return render(request,'loginfb.html')

def privacy(request):
	return render(request,'privacy.html')	


#session_key = '8cae76c505f15432b48c8292a7dd0e54'
#session = Session.objects.get(session_key=session_key)

#if request.user.is_authenticated():
#	    	return render(request,'userpage.html')