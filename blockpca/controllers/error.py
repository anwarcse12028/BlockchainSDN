# -*- coding: utf-8 -*-
"""Error controller"""
from tg import request, expose
from blockpca.lib.base import BaseCtller

__all__ = ['ErrorController']


class ErrorController(BaseCtller):


    @expose('blockpca.templates.error')
    def document(self, *args, **kwargs):
        """Render the error document"""
        resp = request.environ.get('tg.original_response')
        try:
            # tg.abort exposes the message as .detail in response
            message = resp.detail
        except:
            message = None

        if not message:
            message = ("<p>We're sorry but we weren't able to process "
                       " this request.</p>")

        values = dict(prefix=request.environ.get('SCRIPT_NAME', ''),
                      code=request.params.get('code', resp.status_int),
                      message=request.params.get('message', message))
        return values
