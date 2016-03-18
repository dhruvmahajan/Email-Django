from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
from django import forms

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()


def contact(request, mail_id):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_name = form.cleaned_data.get('name')
		form_email = form.cleaned_data.get('email')
		print(form)
		subject = 'django Mail test'
		from_email = settings.EMAIL_HOST_USER
		to_email = [ from_email, 'dhruvemahajan@yahoo.com' ]
		contact_message = "Hello %s,\nIts working\nRegards Dhruv Mahajan\nvia: %s"%(form_name, form_email)

		send_mail(	subject,	
					contact_message,
					'Dhruv'+'<'+from_email+'>',
					to_email,
					fail_silently=False
				)

	context = { "form": form,   }
	return render(request, "forms.html", context)





# Create your views here.
