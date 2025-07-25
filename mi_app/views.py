from django.shortcuts import render, redirect   
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.conf import settings



@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, 'index.html', {'section': 'dashboard'})

@login_required(login_url=settings.LOGIN_URL)
def index2_view(request):
    return render(request, 'index2.html')

@login_required(login_url=settings.LOGIN_URL)  
def index3_view(request):
    return render(request, 'index3.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember_me')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if not remember:
                request.session.set_expiry(0)  
            else:
                request.session.set_expiry(3600)  

            return redirect(request.GET.get('next') or 'dashboard')
        else:
            messages.error(request, 'Incorrect username or password.')
            return redirect('login')
    return render(request, 'pages/examples/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username or not email or not password or not password2:
            messages.error(request, 'All fields are required.')
            return redirect('register')

        if password != password2:
            messages.error(request, 'The passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'The username is already in use.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with that email already exists.')
            return redirect('register')
        
        if request.POST.get('terms') != 'agree':
            messages.error(request, 'You must accept the terms to register.')
            return redirect('register')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Successfully registered user.')
        return redirect('login')

    return render(request, 'pages/examples/register.html')

class CustomPasswordResetView(PasswordResetView):
    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        subject = render_to_string(subject_template_name, context).strip()
        html_content = render_to_string(html_email_template_name, context)

        email = EmailMultiAlternatives(subject, '', from_email, [to_email])
        email.attach_alternative(html_content, "text/html")
        email.send()

@login_required(login_url=settings.LOGIN_URL)       
def widgets_view(request):
    return render(request, 'pages/widgets.html')

@login_required(login_url=settings.LOGIN_URL)
def top_nav_view(request):
    return render(request, 'pages/layout/top-nav.html')

@login_required(login_url=settings.LOGIN_URL)
def top_nav_sidebar_view(request):
    return render(request, 'pages/layout/top-nav-sidebar.html')

@login_required(login_url=settings.LOGIN_URL)
def boxed_view(request):
    return render(request, 'pages/layout/boxed.html')

@login_required(login_url=settings.LOGIN_URL)
def fixed_sidebar_view(request):
    return render(request, 'pages/layout/fixed-sidebar.html')

@login_required(login_url=settings.LOGIN_URL)
def fixed_sidebar_custom_view(request):
    return render(request, 'pages/layout/fixed-sidebar-custom.html')

@login_required(login_url=settings.LOGIN_URL)
def fixed_topnav_view(request):
    return render(request, 'pages/layout/fixed-topnav.html')

@login_required(login_url=settings.LOGIN_URL)
def fixed_footer_view(request):
    return render(request, 'pages/layout/fixed-footer.html')

@login_required(login_url=settings.LOGIN_URL)
def collapsed_sidebar_view(request):
    return render(request, 'pages/layout/collapsed-sidebar.html')

@login_required(login_url=settings.LOGIN_URL)
def chartjs_view(request):
    return render(request, 'pages/charts/chartjs.html')

@login_required(login_url=settings.LOGIN_URL)
def flot_view(request):
    return render(request, 'pages/charts/flot.html')

@login_required(login_url=settings.LOGIN_URL)
def inline_view(request):
    return render(request, 'pages/charts/inline.html')

@login_required(login_url=settings.LOGIN_URL)
def uplot_view(request):
    return render(request, 'pages/charts/uplot.html')

@login_required(login_url=settings.LOGIN_URL)
def general_view(request):
    return render(request, 'pages/UI/general.html')

@login_required(login_url=settings.LOGIN_URL)
def buttons_view(request):
    return render(request, 'pages/UI/buttons.html')

@login_required(login_url=settings.LOGIN_URL)
def icons_view(request):
    return render(request, 'pages/UI/icons.html')

@login_required(login_url=settings.LOGIN_URL)
def sliders_view(request):
    return render(request, 'pages/UI/sliders.html')

@login_required(login_url=settings.LOGIN_URL)
def modals_view(request):
    return render(request, 'pages/UI/modals.html')

@login_required(login_url=settings.LOGIN_URL)
def navbar_view(request):
    return render(request, 'pages/UI/navbar.html')

@login_required(login_url=settings.LOGIN_URL)
def timeline_view(request):
    return render(request, 'pages/UI/timeline.html')

@login_required(login_url=settings.LOGIN_URL)
def ribbons_view(request):
    return render(request, 'pages/UI/ribbons.html')

@login_required(login_url=settings.LOGIN_URL)
def fgeneral_view(request):
    return render(request, 'pages/forms/general.html')

@login_required(login_url=settings.LOGIN_URL)
def advanced_view(request):
    return render(request, 'pages/forms/advanced.html')

@login_required(login_url=settings.LOGIN_URL)
def editors_view(request):
    return render(request, 'pages/forms/editors.html')

@login_required(login_url=settings.LOGIN_URL)
def validation_view(request):
    return render(request, 'pages/forms/validation.html')

@login_required(login_url=settings.LOGIN_URL)
def table_simple_view(request):
    return render(request, 'pages/tables/simple.html')

@login_required(login_url=settings.LOGIN_URL)
def data_view(request):
    return render(request, 'pages/tables/data.html')

@login_required(login_url=settings.LOGIN_URL)
def jsgrid_view(request):
    return render(request, 'pages/tables/jsgrid.html')

@login_required(login_url=settings.LOGIN_URL)
def calendar_view(request):
    return render(request, 'pages/calendar.html')

@login_required(login_url=settings.LOGIN_URL)
def gallery_view(request):
    return render(request, 'pages/gallery.html')

@login_required(login_url=settings.LOGIN_URL)
def kanban_view(request):
    return render(request, 'pages/kanban.html')

@login_required(login_url=settings.LOGIN_URL)
def mailbox_view(request):
    return render(request, 'pages/mailbox/mailbox.html')

@login_required(login_url=settings.LOGIN_URL)
def compose_view(request):
    return render(request, 'pages/mailbox/compose.html')

@login_required(login_url=settings.LOGIN_URL)
def read_mail_view(request):
    return render(request, 'pages/mailbox/read-mail.html')

@login_required(login_url=settings.LOGIN_URL)
def invoice_view(request):
    return render(request, 'pages/examples/invoice.html')

@login_required(login_url=settings.LOGIN_URL)
def invoice_print_view(request):
    return render(request, 'pages/examples/invoice-print.html')

@login_required(login_url=settings.LOGIN_URL)
def profile_view(request):
    return render(request, 'pages/examples/profile.html')

@login_required(login_url=settings.LOGIN_URL)
def recover_password_view(request):
    return render(request, 'pages/examples/recover-password.html')

@login_required(login_url=settings.LOGIN_URL)
def e_commerce_view(request):
    return render(request, 'pages/examples/e-commerce.html')

@login_required(login_url=settings.LOGIN_URL)
def projects_view(request):
    return render(request, 'pages/examples/projects.html')

@login_required(login_url=settings.LOGIN_URL)
def project_add_view(request):
    return render(request, 'pages/examples/project-add.html')

@login_required(login_url=settings.LOGIN_URL)
def project_edit_view(request):
    return render(request, 'pages/examples/project-edit.html')

@login_required(login_url=settings.LOGIN_URL)
def project_detail_view(request):
    return render(request, 'pages/examples/project-detail.html')

@login_required(login_url=settings.LOGIN_URL)
def contacts_view(request):
    return render(request, 'pages/examples/contacs.html')

@login_required(login_url=settings.LOGIN_URL)
def faq_view(request):
    return render(request, 'pages/examples/faq.html')

@login_required(login_url=settings.LOGIN_URL)
def contact_us_view(request):
    return render(request, 'pages/examples/contact-us.html')

@login_required(login_url=settings.LOGIN_URL)
def lockscreen_view(request):
    return render(request, 'pages/examples/lockscreen.html')

@login_required(login_url=settings.LOGIN_URL)
def legacy_user_menu_view(request):
    return render(request, 'pages/examples/legacy-user-menu.html')

@login_required(login_url=settings.LOGIN_URL)
def language_menu_view(request):
    return render(request, 'pages/examples/language-menu.html')

@login_required(login_url=settings.LOGIN_URL)
def E404_view(request):
    return render(request, 'pages/examples/404.html')

@login_required(login_url=settings.LOGIN_URL)
def E500_view(request):
    return render(request, 'pages/examples/500.html')

@login_required(login_url=settings.LOGIN_URL)
def pace_view(request):
    return render(request, 'pages/examples/pace.html')

@login_required(login_url=settings.LOGIN_URL)
def blank_view(request):
    return render(request, 'pages/examples/blank.html')

@login_required(login_url=settings.LOGIN_URL)
def starter_view(request):
    return render(request, 'starter.html')

@login_required(login_url=settings.LOGIN_URL)
def simple_view(request):
    return render(request, 'pages/search/simple.html')

@login_required(login_url=settings.LOGIN_URL)
def enhanced_view(request):
    return render(request, 'pages/search/enhanced.html')

@login_required(login_url=settings.LOGIN_URL)
def enhanced_results_view(request):
    return render(request, 'pages/search/enhanced-results.html')

@login_required(login_url=settings.LOGIN_URL)
def iframe_view(request):
    return render(request, 'iframe.html')

@login_required(login_url=settings.LOGIN_URL)
def iframe_dark_view(request):
    return render(request, 'iframe-dark.html')

@login_required(login_url=settings.LOGIN_URL)
def simple_results_view(request):
    return render(request, 'pages/search/simple-results.html')