def page_context(title = "PPMP", **kwargs ) -> dict:
    '''Map the data to be displayed in the template.'''
    context = kwargs
    context['PAGE_TITLE'] = title
    return context

def has_user(request):
    '''check user exist'''
    return request.user.is_authenticated