import logging

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('middlewares')


class RequestStatisticMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response=get_response

        # def __call__(self, request):
        #
        #     logger.info(f"Request to {request.path} was made")
        #     response=self.get_response(request)
        #     return response

        def __call__(self, request):
            logger.debug('Called BEFORE the view an GET the RESPONSE')
            response=self.get_response(request)
            logger.debug('Called AFTER the view an GET the RESPONSE')
            return response


        def process_view(self, request, view_func, view_args, view_kwargs):
            if request.user.is_authentificated() and not request.path.startswith('/admin'):
               stats, is_created = RequestStatistics.objects.get_or_create(user=request.user)
               stats.request+=1
               stats.save()


