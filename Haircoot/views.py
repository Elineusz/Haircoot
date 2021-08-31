from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic, View



from .forms import LoginForm, RegisterForm, NewService
from .models import Service


class IndexView(View):

    def get(self, request):
        context = {

        }
        return render(request, 'Haircoot/index.html', context)


class LoginView(View):

    def get(self, request):
        ctx = {
            'form': LoginForm,
            }
        return render(request, 'Haircoot/login.html', ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                url = request.GET.get('next')
                if url:
                    return redirect(url)
                return HttpResponseRedirect(reverse('index'))

            form.add_error(field=None, error='Zły login lub hasło!')

        ctx = {
            'form': form,
            }
        messages.error(request, 'Zły login lub hasło.')
        return render(request, 'login.html', ctx)


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        ctx = {
            'form': form,
        }
        return render(request, 'Haircoot/register.html', ctx)

    def post(self, request):
        message = None
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_confirmation']:
                username_selected = form.cleaned_data['username']
                email_selected = form.cleaned_data['email']
                user = False
                try:
                    user = User.objects.get(username=username_selected)
                    message = "User exist."
                except ObjectDoesNotExist:
                    pass
                try:
                    user = User.objects.get(email=email_selected)
                    message = "Email exist."
                except ObjectDoesNotExist:
                    pass
                if user:
                    messages.error(request, message)
                    return HttpResponseRedirect(reverse('register'))
                else:
                    user = User.objects.create_user(
                        username=username_selected,
                        email=email_selected,
                        password=form.cleaned_data['password']
                    )
                    messages.success(request, 'Your user was created.')
                    return HttpResponseRedirect(reverse('login'))
            else:
                message = "Passwords are not the same."
                messages.error(request, message)
                return HttpResponseRedirect(reverse('register'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "Haircoot/logout.html")


class PolicyView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'Haircoot/policy.html', context)


class RegulationsView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'Haircoot/regulations.html', context)


class ReservationView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'Haircoot/reservation.html', context)
# TODO rezerwacja na usługę


class ReservationOneTimeView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'Haircoot/onetime.html', context)
# TODO rezerwacja jeśli nie użytkowik


class ReservationConfirmedView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'Haircoot/onetime.html', context)
# TODO rezerwacja potwierdzona


class EmployeeView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'Haircoot/employee.html', context)
# TODO urlopy, grafik


class ServicesView(View):
    def get(self, request):
        services_list = Service.objects.order_by()
        # employeeskills = .objects.filter(is_staff='1')
        context = {
        'services_list':services_list,
        # 'employee_list': employee
        }
        return render(request, 'Haircoot/services.html', context)
# TODO lista usług z opisem i kto robi


class NewserviceView(PermissionRequiredMixin, View):
    permission_required = 'Haircoot.add_service'
    raise_exception = True

    def get(self, request):
        form = NewService()
        ctx = {
            'form': form,
        }
        return render(request, 'Haircoot/newservice.html', ctx)

    def post(self, request):
        message = None
        form = NewService(request.POST)
        if form.is_valid():
            service_name_selected = form.cleaned_data['service_name']
            service_detailed_selected = form.cleaned_data['service_detailed']
            service_duration_selected = form.cleaned_data['service_duration']
            service_price_selected = form.cleaned_data['service_price']

            service_name = False
            try:
                service_name = Service.objects.get(service_name=service_name_selected)
                message = "Usługa o podanej nazwie już istnieje."
            except ObjectDoesNotExist:
                pass
            if service_name:
                messages.error(request, message)
                return HttpResponseRedirect(reverse('newservice'))
            else:
                service = Service.objects.create(
                    service_name=service_name_selected,
                    service_detailed=service_detailed_selected,
                    service_duration=service_duration_selected * 60,
                    service_price=service_price_selected
                )
                messages.success(request, 'Usługa dodana.')
                return HttpResponseRedirect(reverse('newservice'))
