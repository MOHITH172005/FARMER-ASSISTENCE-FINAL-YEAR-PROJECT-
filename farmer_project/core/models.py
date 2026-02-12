from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

is_first_login = models.BooleanField(default=True)
safety_enabled = models.BooleanField(default=False)


class FarmerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="farmer_profile"
    )

    # 👤 BASIC FARMER INFO
    farmer_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15, unique=True)

    # 📍 LOCATION
    pincode = models.CharField(max_length=6)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    # 🌾 FARM DETAILS
    primary_crop = models.CharField(max_length=100)
    land_area = models.DecimalField(max_digits=6, decimal_places=2)

    # 🖼 PROFILE PHOTO
    photo = models.ImageField(
        upload_to="farmer_photos/",
        null=True,
        blank=True
    )

    # 🔒 AI MISUSE BLOCKING (CRITICAL)
    is_blocked = models.BooleanField(default=False)
    block_reason = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    blocked_at = models.DateTimeField(null=True, blank=True)

    # 🟢 SAFETY PERMISSION (ONE-TIME FOR ALL USERS)
    safety_consent_given = models.BooleanField(default=False)
    safety_consent_at = models.DateTimeField(null=True, blank=True)

    # 🚨 EMERGENCY / PROTECTION MODE (NEW)
    emergency_active = models.BooleanField(default=False)
    last_checkin = models.DateTimeField(null=True, blank=True)

    # 🕒 METADATA
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer_id} - {self.full_name}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
class AIRequestLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.feature}"
class Farmer(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    is_blocked = models.BooleanField(default=False)
    block_reason = models.TextField(null=True, blank=True)
    blocked_at = models.DateTimeField(null=True, blank=True)
class MisuseLog(models.Model):
    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="misuse_logs"
    )

    message = models.TextField()
    category = models.CharField(max_length=50)
    confidence_score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer.farmer_id} - {self.category}"
# core/models.py

class UnblockRequest(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )

    farmer = models.ForeignKey(
        "FarmerProfile",
        on_delete=models.CASCADE,
        related_name="unblock_requests"
    )
    message = models.TextField()
    promise = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.farmer.farmer_id} - {self.status}"
def unblock_request(request):
    profile = FarmerProfile.objects.filter(user=request.user).first()

    if not profile or not profile.is_blocked:
        return redirect("dashboard")

    if request.method == "POST":
        message = request.POST.get("message")

        UnblockRequest.objects.create(
            farmer=profile,
            message=message
        )

        messages.success(
            request,
            "Your unblock request has been sent to admin."
        )
        return redirect("login")

    return render(request, "unblock_request.html")
class SafetyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emergency_contact_1 = models.CharField(max_length=15)
    emergency_contact_2 = models.CharField(max_length=15, blank=True)
    family_contact = models.CharField(max_length=15)
    consent_given = models.BooleanField(default=False)
class EmergencyIncident(models.Model):
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("danger", "Danger"),
        ("resolved", "Resolved"),
        ("false", "False Alarm"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    video_saved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.farmer.farmer_id} - {self.status}"



