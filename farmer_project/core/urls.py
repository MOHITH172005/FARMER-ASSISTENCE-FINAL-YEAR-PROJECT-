from django.urls import path
from . import views
from .views import admin_reset_password
from .views import admin_splash, admin_login
from .views import admin_dashboard
from . import views   # ✅ IMPORTANT

urlpatterns = [
    # ===== AUTH & BASIC =====
    path("", views.splash, name="splash"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

    # ===== PASSWORD RESET =====
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("reset-password/", views.reset_password, name="reset_password"),

    # ===== DASHBOARD =====
    path("dashboard/", views.dashboard, name="dashboard"),

    # ===== NOTIFICATIONS =====
    path("notifications/count/", views.notification_count, name="notification_count"),

    # ===== FEATURES =====
    path("crop-recommendation/", views.crop_recommendation, name="crop_recommendation"),
    path("disease-detection/", views.disease_detection, name="disease_detection"),
    path("plant-doctor/", views.plant_doctor, name="plant_doctor"),
    path("weather/", views.weather_forecast, name="weather_forecast"),
    path("market-prices/", views.market_prices, name="market_prices"),
    path("fertilizer-advice/", views.fertilizer_advice, name="fertilizer_advice"),
    path("irrigation/", views.irrigation, name="irrigation"),
    path("govt-schemes/", views.govt_schemes, name="govt_schemes"),
    path("ai-assistant/", views.chatbot_view, name="chatbot"),
    path("trouble-login/", views.trouble_login, name="trouble_login"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
    path("contact-doctor/", views.contact_doctor, name="contact_doctor"),
    path("secure-control-228x1a3149/login/", admin_login, name="admin_login"),
    path(
    "secure-panel-228x1a3149/",
    views.admin_dashboard,
    name="admin_dashboard"
),
    path(
    "secure-control-228x1a3149/forgot/",
    views.admin_forgot_password,
    name="admin_forgot_password"
),
    path(
    "secure-control-228x1a3149/reset/",
    views.admin_reset_password,
    name="admin_reset_password"
),
    path("secure-control-228x1a3149/verify/", views.admin_verify_otp, name="admin_verify_otp"),
    path(
    "secure-control-228x1a3149/forgot/",
    views.admin_forgot_password,
    name="admin_forgot_password"
),
    path("secure-control-228x1a3149/reset/", admin_reset_password, name="admin_reset_password"),


    # ===== PROFILE =====
    path("profile/", views.profile, name="profile"),

    # ===== FARMER ID (AJAX) =====
    path(
        "generate-farmer-ids/",
        views.generate_farmer_ids_view,
        name="generate_farmer_ids"
    ),
    path("secure-control-228x1a3149/", admin_splash, name="admin_splash"),
    path("secure-panel-228x1a3149/", admin_dashboard, name="admin_dashboard"),
    path("admin/farmers/", views.admin_farmers, name="admin_farmers"),
    path("admin/farmers/<int:id>/toggle/", views.toggle_farmer, name="toggle_farmer"),
    path("admin/farmers/<int:id>/delete/", views.delete_farmer, name="delete_farmer"),
    path("ai-assistant/", views.chatbot_view, name="chatbot"),
    path("admin/unblock-requests/", views.admin_unblock_requests, name="admin_unblock_requests"),
    path("admin/unblock/approve/<int:req_id>/", views.approve_unblock, name="approve_unblock"),
    path("admin/unblock/reject/<int:req_id>/", views.reject_unblock, name="reject_unblock"),
    path("unblock-request/", views.unblock_request, name="unblock_request"),
    path("unblock/approve/<int:pk>/", views.approve_unblock, name="approve_unblock"),
    path("unblock/reject/<int:pk>/", views.reject_unblock, name="reject_unblock"),
    path(
        "unblock-request/<int:pk>/approve/",
        views.approve_unblock_request,
        name="approve_unblock",
    ),
    path(
        "unblock-request/<int:pk>/reject/",
        views.reject_unblock_request,
        name="reject_unblock",
    ),
    path('safety-consent/', views.safety_consent, name='safety_consent'),
    path("emergency/trigger/", views.trigger_emergency, name="trigger_emergency"),
    path("emergency/resolve/", views.resolve_emergency, name="resolve_emergency"),
    




    

]
