from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', views.dashboard, name='dashboard'),

    path('index2/', views.index2_view, name='indice2'),

    path('index3/', views.index3_view, name='índice3'),  

    path('login/', views.custom_login, name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', views.register_view, name='register'),  

    path('forgot-password/', CustomPasswordResetView.as_view(
        template_name='pages/examples/forgot-password.html',
        subject_template_name='emails/password_reset_subject.txt',
        html_email_template_name='emails/password_reset_email.html',
        success_url='/forgot-password/done/'
    ), name='forgot_pwd'),

    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pages/examples/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='pages/examples/recover-password.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pages/examples/password_reset_complete.html'
    ), name='password_reset_complete'),

    path('widgets/', views.widgets_view, name='widgets'),

    path('top-nav/', views.top_nav_view, name='top-nav'),

    path('top-nav-sidebar/', views.top_nav_sidebar_view, name='top-nav-sidebar'),

    path('boxed/', views.boxed_view, name='boxed'),

    path('fixed-sidebar/', views.fixed_sidebar_view, name='fixed-sidebar'),

    path('fixed-sidebar-custom/', views.fixed_sidebar_custom_view, name='fixed-sidebar-custom'),

    path('fixed-topnav/', views.fixed_topnav_view, name='fixed-topnav'),

    path('fixed-footer/', views.fixed_footer_view, name='fixed-footer'),

    path('collapsed-sidebar/', views.collapsed_sidebar_view, name='collapsed-sidebar'),

    path('chartjs/', views.chartjs_view, name='chartjs'),

    path('flot/', views.flot_view, name='flot'),

    path('inline/', views.inline_view, name='inline'),

    path('uplot/', views.uplot_view, name='uplot'),

    path('general/', views.general_view, name='general'),

    path('buttons/', views.buttons_view, name='buttons'),

    path('icons/', views.icons_view, name='icons'),

    path('sliders/', views.sliders_view, name='sliders'),

    path('modals/', views.modals_view, name='modals'),

    path('navbar/', views.navbar_view, name='navbar'),

    path('timeline/', views.timeline_view, name='timeline'),

    path('ribbons/', views.ribbons_view, name='ribbons'),

    path('fgeneral/', views.ribbons_view, name='fgeneral'),

    path('advanced/', views.ribbons_view, name='advanced'),

    path('editors/', views.editors_view, name='editors'),

    path('validation/', views.validation_view, name='validation'),

    path('tables-simple/', views.table_simple_view, name='table-simple'),

    path('data/', views.data_view, name='data'),

    path('jsgrid/', views.data_view, name='jsgrid'),

    path('calendar/', views.calendar_view, name='calendar'),

    path('gallery/', views.gallery_view, name='gallery'),

    path('kanban/', views.kanban_view, name='kanban'),

    path('mailbox/', views.mailbox_view, name='mailbox'),

    path('compose/', views.mailbox_view, name='compose'),

    path('read-mail/', views.read_mail_view, name='read-mail'),

    path('invoice/', views.invoice_view, name='invoice'),

    path('invoice-print/', views.invoice_print_view, name='invoice-print'),

    path('profile/', views.profile_view, name='profile'),

    path('e-commerce/', views.e_commerce_view, name='e-commerce'),

    path('projects/', views.projects_view, name='projects'),

    path('project-add/', views.project_add_view, name='project-add'),

    path('project-edit/', views.project_edit_view, name='project-edit'),

    path('project-detail/', views.project_detail_view, name='project-detail'),

    path('contacts/', views.contacts_view, name='contacts'),

    path('faq/', views.faq_view, name='faq'),

    path('contact-us/', views.contact_us_view, name='contact-us'),

    path('lockscreen/', views.lockscreen_view, name='lockscreen'),

    path('legacy-user-menu/', views.legacy_user_menu_view, name='legacy-user-menu'),

    path('language-menu/', views.language_menu_view, name='language-menu'),

    path('404/', views.E404_view, name='404'),

    path('500/', views.E500_view, name='500'),

    path('pace/', views.pace_view, name='pace'),

    path('blank/', views.blank_view, name='blank'),

    path('starter/', views.starter_view, name='starter'),

    path('simple/', views.simple_view, name='simple'),

    path('enhanced/', views.enhanced_view, name='enhanced'),

    path('iframe/', views.iframe_view, name='iframe'),

    path('simple-results/', views.simple_results_view, name='simple-results'),

    path('iframe.dark/', views.iframe_dark_view, name='iframe-dark'),

    path('enhanced-results/', views.enhanced_results_view, name='enhanced-results'),

    path('recover-password/', views.recover_password_view, name='recover-password'),
]