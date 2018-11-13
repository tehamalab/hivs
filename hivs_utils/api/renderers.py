from rest_framework import renderers


class BrowsableAPIRenderer(renderers.BrowsableAPIRenderer):
    """Browsable API render without HTML forms."""

    def get_rendered_html_form(self, *args, **kwargs):
        """
        Don't render HTML forms.
        """
        return ""

    def get_filter_form(self, data, view, request):
        """Don't render the filter form"""
        return None
