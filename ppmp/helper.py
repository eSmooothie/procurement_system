def page_context(title = "PPMP", **kwargs ) -> dict:
    '''Map the data to be displayed in the template.'''
    context = kwargs # Retrieve all passed parameters .
    context['PAGE_TITLE'] = title # Add page_title key.
    return context