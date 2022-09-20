from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from django.urls import path, include

class ApiHome(APIView):
    """
    This is the main application endpoint.
    From this endpoint you can explore each resources by clicking in each link below.
    """

    # permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        response = {
            "prode": {
                "customers-list": reverse("customer-list", request=request),
                "products-list": reverse("product-list", request=request),
                "transaction-list": reverse("transaction-list", request=request),
                "category-list": reverse("category-list", request=request),
                "tag-list": reverse("tag-list", request=request),
            },
            "user": {
                "users": reverse("users", request=request),
                # Authentication endpoints
                # "login": reverse("rest_login", request=request),
                # "user": reverse("rest_user_details", request=request),
                # "logout": reverse("rest_logout", request=request),
                # "password_reset": reverse("rest_password_reset", request=request),
                # "password_change": reverse("rest_password_change", request=request),
                # # Register endpoints
                # "register": reverse("rest_register", request=request),
                # "verify_email": reverse("rest_verify_email", request=request),
                # "resend_email": reverse("rest_resend_email", request=request),
                # # Token endpoints
                # "token_verify": reverse("token_verify", request=request),
                # "token_refresh": reverse("token_refresh", request=request),
            },
        }
        return Response(response, status=status.HTTP_200_OK)