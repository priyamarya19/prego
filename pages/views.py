from django.shortcuts import render,HttpResponseRedirect
from .models import Contact
from django.template.context_processors import csrf
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
	context={
		'message':"Hello there!! You have reached our page. Welcome!!"
	}
	return render(request,'homepage.html',context)

def why(request):
	context={
		'message':"Hello there!! You have reached why page. Welcome!!"
	}
	return render(request,'why.html',context)

def how(request):
	context={}
	return render(request,'how.html',context)

def home2(request):
	context={
		'message':"Hello there!! You have reached our page. Welcome!!"
	}
	return render(request,'home.html',context)

def home3(request):
	context={
		'message':"Hello there!! You have reached our page. Welcome!!"
	}
	return render(request,'home3.html',context)

def contact_entry(request):
	#import ipdb; ipdb.set_trace()
	context={}
	user=request.user
	try:
		if request.method == "POST":
			number= request.POST.get("number")
			if not Contact.objects.filter(number=number).exists():
				instance=Contact(
					number=number,
					count=1,
					)
				instance.save()
				subject = "user contacted"
				message =  (number + " has requested contact")
				from_email = settings.EMAIL_HOST_USER
				to_email = [settings.EMAIL_RECEIVER]
				send_mail(
					subject,
					message,
					from_email,
					to_email,
					fail_silently=False,
				)
				# subject = "no-reply"
				# message =  "Thank you for contacting us. We will get back to you as soon as possible."
				# from_email = settings.EMAIL_HOST_USER
				# to_email = [email]
				# send_mail(
				# 	subject,
				# 	message,
				# 	from_email,
				# 	to_email,
				# 	fail_silently=False,
				# )
			else:
				numb=Contact.objects.get(number=number)
				numb.count+=1
				numb.save()
				subject = "user contacted"
				message =  (number + " has requested contact ")
				from_email = settings.EMAIL_HOST_USER
				to_email = [settings.EMAIL_RECEIVER]
				send_mail(
					subject,
					message,
					from_email,
					to_email,
					fail_silently=False,
				)
	except:
		print(number)
		context={
			'message':'please enter a valid no.'
		}
		context.update(csrf(request))
		return HttpResponseRedirect('/')

	context.update(csrf(request))
	return HttpResponseRedirect('/')


def contact_entry2(request):
	#import ipdb; ipdb.set_trace()
	context={}
	user=request.user
	try:
		if request.method == "POST":
			number= request.POST.get("number")
			if not Contact.objects.filter(number=number).exists():
				instance=Contact(
					number=number,
					count=1,
					)
				instance.save()
				subject = "user contacted"
				message =  (number + " has requested contact")
				from_email = settings.EMAIL_HOST_USER
				to_email = [settings.EMAIL_RECEIVER]
				send_mail(
					subject,
					message,
					from_email,
					to_email,
					fail_silently=False,
				)
				# subject = "no-reply"
				# message =  "Thank you for contacting us. We will get back to you as soon as possible."
				# from_email = settings.EMAIL_HOST_USER
				# to_email = [email]
				# send_mail(
				# 	subject,
				# 	message,
				# 	from_email,
				# 	to_email,
				# 	fail_silently=False,
				# )
			else:
				numb=Contact.objects.get(number=number)
				numb.count+=1
				numb.save()
				subject = "user contacted"
				message =  (number + " has requested contact ")
				from_email = settings.EMAIL_HOST_USER
				to_email = [settings.EMAIL_RECEIVER]
				send_mail(
					subject,
					message,
					from_email,
					to_email,
					fail_silently=False,
				)
	except:
		print(number)
		context={
			'message':'please enter a valid no.'
		}
		context.update(csrf(request))
		return HttpResponseRedirect('/')
	context.update(csrf(request))
	return HttpResponseRedirect('/2')