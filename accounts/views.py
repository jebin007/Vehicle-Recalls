from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
from accounts.forms import UserForm
from django.contrib import messages

def register_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Thank you! You are now registered!</h2>')
    return render(request, 'accounts/registration_form.html', {'form': form})

# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'accounts/registration_form.html'
#
#     #display blank form
#     def get(self,request):
#         form = self.form_class(None)
#         return render(request,self.template_name,{'form': form})
#     #process form data
#     def post(self,request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False) #this saves the form locally but not into the database for further validation
#             #cleaned (normalized) data
#             # username = form.cleaned_data['username']
#             # email = form.cleaned_data['email']
#             user.save() #this saves the user to the database.
#             return HttpResponse('<h1> You are now successfully registered! </h1>')


