from django import template

register = template.Library()

@register.simple_tag

def hello_world(username):
    return f"Hi {username}"

# register = template.Library()

# @register.filter(name= "transform")
# @stringfilter
# def first_char(value):
#     return value[0]

# @register.filter(name= "lengthis",expects_localtime = True, is_safe = True)
# def checkstrlen(value, size):
#     return len(value) == size