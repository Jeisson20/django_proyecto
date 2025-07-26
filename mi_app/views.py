from django.shortcuts import render, redirect   
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def dashboard(request):
    return render(request, 'index.html', {'section': 'dashboard'})

def index2_view(request):
    return render(request, 'index2.html')

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
      
def widgets_view(request):
    return render(request, 'pages/widgets.html')

def top_nav_view(request):
    return render(request, 'pages/layout/top-nav.html')

def top_nav_sidebar_view(request):
    return render(request, 'pages/layout/top-nav-sidebar.html')

def boxed_view(request):
    return render(request, 'pages/layout/boxed.html')

def fixed_sidebar_view(request):
    return render(request, 'pages/layout/fixed-sidebar.html')

def fixed_sidebar_custom_view(request):
    return render(request, 'pages/layout/fixed-sidebar-custom.html')

def fixed_topnav_view(request):
    return render(request, 'pages/layout/fixed-topnav.html')

def fixed_footer_view(request):
    return render(request, 'pages/layout/fixed-footer.html')

def collapsed_sidebar_view(request):
    return render(request, 'pages/layout/collapsed-sidebar.html')

def chartjs_view(request):
    return render(request, 'pages/charts/chartjs.html')

def flot_view(request):
    return render(request, 'pages/charts/flot.html')

def inline_view(request):
    return render(request, 'pages/charts/inline.html')

def uplot_view(request):
    return render(request, 'pages/charts/uplot.html')

def general_view(request):
    return render(request, 'pages/UI/general.html')

def buttons_view(request):
    return render(request, 'pages/UI/buttons.html')

def icons_view(request):
    return render(request, 'pages/UI/icons.html')

def sliders_view(request):
    return render(request, 'pages/UI/sliders.html')

def modals_view(request):
    return render(request, 'pages/UI/modals.html')

def navbar_view(request):
    return render(request, 'pages/UI/navbar.html')

def timeline_view(request):
    return render(request, 'pages/UI/timeline.html')

def ribbons_view(request):
    return render(request, 'pages/UI/ribbons.html')

def fgeneral_view(request):
    return render(request, 'pages/forms/general.html')

def advanced_view(request):
    return render(request, 'pages/forms/advanced.html')

def editors_view(request):
    return render(request, 'pages/forms/editors.html')

def validation_view(request):
    return render(request, 'pages/forms/validation.html')

def table_simple_view(request):
    return render(request, 'pages/tables/simple.html')

def data_view(request):
    return render(request, 'pages/tables/data.html')

def jsgrid_view(request):
    return render(request, 'pages/tables/jsgrid.html')

def calendar_view(request):
    return render(request, 'pages/calendar.html')

def gallery_view(request):
    return render(request, 'pages/gallery.html')

def kanban_view(request):
    return render(request, 'pages/kanban.html')

def mailbox_view(request):
    return render(request, 'pages/mailbox/mailbox.html')

def compose_view(request):
    return render(request, 'pages/mailbox/compose.html')

def read_mail_view(request):
    return render(request, 'pages/mailbox/read-mail.html')

def invoice_view(request):
    return render(request, 'pages/examples/invoice.html')

def invoice_print_view(request):
    return render(request, 'pages/examples/invoice-print.html')

def profile_view(request):
    return render(request, 'pages/examples/profile.html')

def recover_password_view(request):
    return render(request, 'pages/examples/recover-password.html')

def e_commerce_view(request):
    return render(request, 'pages/examples/e-commerce.html')

def projects_view(request):
    return render(request, 'pages/examples/projects.html')

def project_add_view(request):
    return render(request, 'pages/examples/project-add.html')

def project_edit_view(request):
    return render(request, 'pages/examples/project-edit.html')

def project_detail_view(request):
    return render(request, 'pages/examples/project-detail.html')

def contacts_view(request):
    return render(request, 'pages/examples/contacs.html')

def faq_view(request):
    return render(request, 'pages/examples/faq.html')

def contact_us_view(request):
    return render(request, 'pages/examples/contact-us.html')

def lockscreen_view(request):
    return render(request, 'pages/examples/lockscreen.html')

def legacy_user_menu_view(request):
    return render(request, 'pages/examples/legacy-user-menu.html')

def language_menu_view(request):
    return render(request, 'pages/examples/language-menu.html')

def E404_view(request):
    return render(request, 'pages/examples/404.html')

def E500_view(request):
    return render(request, 'pages/examples/500.html')

def pace_view(request):
    return render(request, 'pages/examples/pace.html')

def blank_view(request):
    return render(request, 'pages/examples/blank.html')

def starter_view(request):
    return render(request, 'starter.html')

def simple_view(request):
    return render(request, 'pages/search/simple.html')

def enhanced_view(request):
    return render(request, 'pages/search/enhanced.html')

def enhanced_results_view(request):
    return render(request, 'pages/search/enhanced-results.html')

def iframe_view(request):
    return render(request, 'iframe.html')

def iframe_dark_view(request):
    return render(request, 'iframe-dark.html')

def simple_results_view(request):
    return render(request, 'pages/search/simple-results.html')