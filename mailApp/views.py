from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
from django import forms

class ContactForm(forms.Form):
	email = forms.EmailField()
	subject = forms.CharField( widget=forms.Textarea(attrs={'cols': 80, 'rows': 1}))
	message = forms.CharField( widget=forms.Textarea(attrs={'cols': 80, 'rows': 5}))



def contact(request, mail_id):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get('email')
		form_subject = form.cleaned_data.get('subject')
		form_message = form.cleaned_data.get('message')

		print(form)
		subject = form_subject
		from_email = settings.EMAIL_HOST_USER
		to_email = [ from_email, form_email ]
		contact_message = form_message

		send_mail(	subject,	
					contact_message,
					'Dhruv'+'<'+from_email+'>',
					to_email,
					fail_silently=False
				)

	context = { "form": form,   }
	return render(request, "forms.html", context)





# Create your views here.
