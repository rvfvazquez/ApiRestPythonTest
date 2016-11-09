# coding=utf-8

import datetime
import logging
logger = logging.getLogger('backend')

from django.views.debug import CLEANSED_SUBSTITUTE
from django.conf import settings
from django.db import connection
from tastypie.serializers import Serializer

import time

class ResponseLoggingMiddleware(object):
    def process_request(self, request):
        self.start_time = time.time()

    def process_response(self, request, response):
        try:    
            remote_addr = request.META.get('REMOTE_ADDR')    
            if remote_addr in getattr(settings, 'INTERNAL_IPS', []):
                remote_addr = request.META.get('HTTP_X_FORWARDED_FOR') or remote_addr
            user_email = "-" 
            extra_log = ""
            if hasattr(request,'user'):
                user_email = getattr(request.user, 'email', '-')
            req_time = time.time() - self.start_time
            content_len = len(response.content)
            if settings.DEBUG:
                sql_time = sum(float(q['time']) for q in connection.queries) * 1000
                extra_log += " (%s SQL queries, %s ms)" % (len(connection.queries), sql_time)

            if request.path.startswith('/api/'):
                try:
                    s = Serializer()
                    if request.method == 'POST':
                        body = s.deserialize(request.body, 'application/json')
                    elif request.method == 'PUT':
                        body = s.deserialize(request.body, 'application/json')
                    elif request.method == 'GET':
                        body = ""
                except Exception as e:
                    logging.error("Deserialization error: %s" % e)
            else:
                body = ""
            logger.info("%s %s %s %s %s %s %s (%.02f seconds)%s" % (remote_addr, user_email, request.method, request.get_full_path(), body, response.status_code, content_len, req_time, extra_log))
        except Exception as e:
            logger.error("LoggingMiddleware Error: %s" % e)
        return response