# from .pydiff import diff
#
#
# for line in diff(iter(['a', 'b', 'c']), iter(['a', 'c'])):
#     print(line)

class A():
    """
    This is A class
    """

    def __init__(self):
        """
        This is __init__ method of A class
        """
        self.p1 = 1

    def __call__(self, *args, **kwargs):
        """
        This is :py:meth:`__call__` method of :class:`A` class Return HeavySelect2Mixin.

        Args:
            data_view (str): URL pattern name
            data_url (str): URL
            dependent_fields (List[str]): List of dependent parent fields.

        Raises:
            Http404: If if the widget can not be found or no id is provided.

        Returns:
            ModelSelect2Mixin: Widget from cache.


        Example usage::

            class MyModelForm(forms.ModelForm):
                class Meta:
                    model = MyModel
                    fields = ('my_field', )
                    widgets = {
                        'my_field': Select2Widget
                    }

        or::

            class MyForm(forms.Form):
                my_choice = forms.ChoiceField(widget=Select2Widget)

        """
        return args, kwargs

    def simple(self, *args, **kwargs):
        """
        This is `simple` method of A class
        """
        return args, kwargs


a = A()
