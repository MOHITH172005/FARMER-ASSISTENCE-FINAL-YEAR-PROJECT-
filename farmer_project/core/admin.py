from django.contrib import admin, messages
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect, get_object_or_404

from .models import FarmerProfile, UnblockRequest
from django.contrib import admin
from .models import EmergencyIncident, SafetyProfile

admin.site.register(EmergencyIncident)
admin.site.register(SafetyProfile)



@admin.register(UnblockRequest)
class UnblockRequestAdmin(admin.ModelAdmin):
    list_display = (
        "farmer_id_display",
        "status",
        "created_at",
        "action_buttons",
    )

    list_filter = ("status", "created_at")
    search_fields = ("farmer__farmer_id",)
    readonly_fields = ("farmer", "message", "promise", "status", "created_at")

    ordering = ("-created_at",)

    # ===============================
    # Display Farmer ID
    # ===============================
    def farmer_id_display(self, obj):
        return obj.farmer.farmer_id
    farmer_id_display.short_description = "Farmer ID"

    # ===============================
    # Action Buttons (Approve / Reject)
    # ===============================
    def action_buttons(self, obj):
        if obj.status == "pending":
            return format_html(
                '<a class="button" style="margin-right:8px" '
                'href="{}">✅ Approve</a>'
                '<a class="button" style="color:red" '
                'href="{}">❌ Reject</a>',
                f"{obj.id}/approve/",
                f"{obj.id}/reject/",
            )
        elif obj.status == "approved":
            return format_html('<span style="color:green;font-weight:600;">Approved</span>')
        else:
            return format_html('<span style="color:red;font-weight:600;">Rejected</span>')

    action_buttons.short_description = "Actions"

    # ===============================
    # Custom Admin URLs
    # ===============================
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<int:request_id>/approve/",
                self.admin_site.admin_view(self.approve_request),
                name="approve_unblock_request",
            ),
            path(
                "<int:request_id>/reject/",
                self.admin_site.admin_view(self.reject_request),
                name="reject_unblock_request",
            ),
        ]
        return custom_urls + urls

    # ===============================
    # Approve Request
    # ===============================
    def approve_request(self, request, request_id):
        unblock_request = get_object_or_404(UnblockRequest, id=request_id)

        if unblock_request.status != "pending":
            messages.warning(request, "This request is already processed.")
            return redirect("../")

        farmer_profile = unblock_request.farmer

        # Unblock farmer
        farmer_profile.is_blocked = False
        farmer_profile.save()

        # Update request status
        unblock_request.status = "approved"
        unblock_request.save()

        messages.success(
            request,
            f"Farmer {farmer_profile.farmer_id} has been unblocked successfully."
        )
        return redirect("../../")

    # ===============================
    # Reject Request
    # ===============================
    def reject_request(self, request, request_id):
        unblock_request = get_object_or_404(UnblockRequest, id=request_id)

        if unblock_request.status != "pending":
            messages.warning(request, "This request is already processed.")
            return redirect("../")

        unblock_request.status = "rejected"
        unblock_request.save()

        messages.error(
            request,
            f"Unblock request for Farmer {unblock_request.farmer.farmer_id} rejected."
        )
        return redirect("../../")
