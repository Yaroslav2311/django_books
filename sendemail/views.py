from django.shortcuts import redirect
from django.shortcuts import render

from .forms import FormEmail
from .tasks import send_email as celery_send_email


def create_form(request):
    if request == 'POST':
        form = FormEmail(request.POST)
        if form.is_valid():
            subject = 'reminder'
            from_email = 'yaroslav.boyko.2311@gmail.com'
            email = list(form.cleaned_data('email'))
            text = form.cleaned_data('text')
            date = form.cleaned_data('date')
            # celery_send_email.delay(subject, text, from_email, email)
            celery_send_email.apply_async((subject, text, from_email, email), eta=date)
            return redirect('send')

    else:
        form = FormEmail()
        return render(request, 'sendemail/sendemail.html', {'form': form})
