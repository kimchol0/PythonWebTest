from django.template import Library
register = Library()

@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)

@register.filter
def spliter(value,args):
    start,end = args.split(',')
    value = value.encode('utf-8').decode('utf-8')
    return value[int(start):int(end)]