import jwt
from django.conf import settings
from django.http import JsonResponse

class SupabaseAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get("Authorization")

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

            try:
                payload = jwt.decode(
                    token,
                    settings.SUPABASE_JWT_SECRET,
                    algorithms=["HS256"],
                    audience="authenticated"
                )

                request.supabase_user = payload

            except jwt.ExpiredSignatureError:
                return JsonResponse({"error": "Token expired"}, status=401)

            except jwt.InvalidTokenError:
                return JsonResponse({"error": "Invalid token"}, status=401)

        else:
            request.supabase_user = None

        return self.get_response(request)