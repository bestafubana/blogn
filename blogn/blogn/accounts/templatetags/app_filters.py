import hashlib
import urllib
from django import template
from django.utils.safestring import mark_safe
 
register = template.Library()
 
# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=40):
    default = "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mm&f=y"
    return "https://www.gravatar.com/avatar/%s?%s" % (hashlib.md5(email.encode('utf-8').lower()).hexdigest(), urllib.parse.urlencode({'d':default, 's':str(size)}))
 
# return an image tag with the gravatar
# TEMPLATE USE:  {{ email|gravatar:150 }}
@register.filter
def gravatar(email, size=40):
    url = gravatar_url(email.encode('utf-8'), size)
    return mark_safe('<img src="%s" height="%d" width="%d">' % (url, size, size))