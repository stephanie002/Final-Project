def registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(login, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        # I've tried both ways, but it not write anything in to the table
        # user.key = ''.join(random.choice(string.digits) for i in range(12))
        # user.get_profile().key = ''.join(random.choice(string.digits) for i in range(12))

        user.save()
