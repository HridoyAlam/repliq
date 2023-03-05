from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})



class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_detail.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'

class DeviceDetailView(DetailView):
    model = Device
    template_name = 'device_detail.html'

class CheckoutFormView(FormView):
    template_name = 'checkout_form.html'
    form_class = CheckoutForm

    def form_valid(self, form):
        pass
