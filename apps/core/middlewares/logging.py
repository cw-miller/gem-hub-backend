import logging, time 

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_resposne = get_response

    def __call__(self, request):

        start_time = time.time()

        request_data = {
            'method': request.method,
            'ip_address': request.META.get('REMOTE_ADDR'),
            'path': request.path
        }

        logger.info(request_data)

        response = self.get_resposne(request)
        duration = time.time() - start_time

        response_dict = {
            'status_code': response.status_code,
            'duration' : duration
        }

        logger.info(response_dict)

        return response

