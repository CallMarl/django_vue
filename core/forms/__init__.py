from hashlib import md5
from hashlib import sha256
from itertools import chain

from django import forms
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _

from core.utils import model_to_json


class MultiFormException(Exception) :
    pass

class MultiForm :

    '''
    This function is used to generate the id of the form. Base of the form class
    name and the salt you want.
    '''
    @staticmethod
    def get_id(name, salt) :
        hash = md5(salt.encode("utf-8")).hexdigest() \
             + md5(name.encode("utf-8")).hexdigest()
        return sha256(hash.encode("utf-8")).hexdigest()

    forms   = {}

    data    = None

    id      = ""

    def __init__(self, data = None) :
        self.forms  = {}
        self.data   = data

    '''
    This function is used to adding form into the multiform manager.
    '''
    def add_form(self, form, salt, *args, **kwargs) :
        id  = MultiForm.get_id(form.__name__, salt)

        if id in self.forms :
            raise MultiFormException(""
                + _("Id already exist. Please check salt + form name are \
                    different for each form added :\n"
                    ) \
                + "form_name : " + form.__name__ + "\n"
                + "salt : " + salt + "\n"
                )

        if self.data and self.data.get('multiform') == id :
            form = form(data = self.data, *args, **kwargs)
        else :
            form = form(*args, **kwargs)
        self.forms[id] = form
        self.forms[id].fields['multiform'] = forms.CharField(
            max_length  = 256,
            widget      = forms.HiddenInput(
                attrs = {
                    'value' : id,
                    }
                )
            )

    '''
    This function return the current form dependending of the form class and the
    salt used to generate the id.
    '''
    def get_form(self, form, salt) :
        id = MultiForm.get_id(form.__name__, salt)
        if self.forms.get(id) :
            return self.forms.get(id)
        return None

    '''
    This function return the current form in post view.
    '''
    def get_current_form(self) :
        if self.id :
            return self.forms.get(self.id)
        return None

    '''
    This function give the current form error message.
    '''
    def get_form_error(self) :
        return self.get_current_form().errors

    '''
    This function give the current form success message.
    '''
    def get_form_success(self) :
        current_form = self.get_current_form()
        if isinstance(current_form, MultiFormMixin) :
            return current_form.success
        return MultiFormMixin()

    '''
    This is multiform override of the default form `is_valid` method. Working
    like the default default form function.
    '''
    def is_valid(self) :
        id = self.data.get('multiform')

        if self.forms.get(id) :
            self.id = id
            if self.forms.get(id).is_valid() :
                return True
        else :
            raise MultiFormException(""
                + _("Try to validate without multiform id.")
                )
        return False

    '''
    This is multiform override of the default form `render` method. Working like
    the default default form function.
    '''
    def render(self) :
        i       = 1
        forms   = {}

        for key, value in self.forms.items() :
            forms['form_' + str(i)] = value
            i += 1
        return forms

    '''
    This is multiform override of the default form `save` method. Working like
    the default default form function.
    '''
    def save(self, commit = True) :
        if not self.id :
            raise MultiFormException(""
                + _("No form selected please make sure you check form before \
                    save it."
                    )
                )
        return self.forms.get(self.id).save(commit = commit)

'''
Multiform view should extends this mixin to automaticly check the post
submistion.
'''
class MultiFormViewMixin :

    '''
    Multiform class. This is the multiform manager
    '''
    multiform       = None

    template_name   = ""

    '''
    The default multiforme mixin post view.
    '''
    def post(self, request, context = {}) :
        if not self.multiform :
            return render(request, self.template_name, context)
        if hasattr(request, 'is_ajax') and request.is_ajax() :
            if self.multiform.is_valid() :
                self.multiform.save()
                return JsonResponse({
                    'state' : 'success',
                    'form'  : self.multiform \
                        .get_form_success().success.get_json_data()
                    })
            return JsonResponse({
                'state' : 'error',
                'form'  : self.multiform. \
                    get_current_form().errors.get_json_data()
                },
                status = 400
                )
        else :
            if self.multiform.is_valid() :
                self.multiform.save()
            context.update({'multiform' : self.multiform.render()})
            return render(request, self.template_name, context)

'''
Form used in multiform should extends this views to work with XHR query.
'''
class MultiFormMixin :

    _success = _("Default multiform success message")

    '''
    This is a representation of instance in case of model.
    '''
    instance = None

    def __init__(self, *args, **kwargs) :
        self.success = self

    '''
    This function could be override in form to change instance values just befor
    the render.
    '''
    def pre_render(self) :
        return self.instance

    '''
    This function could be override in form to change rendered value just after
    the render
    '''
    def post_render(self, json) :
        return json

    '''
    This function is used by the multiform view mixin to render XHR requests.
    '''
    def get_json_data(self) :
        return self.post_render({
            'message'   : self._success,
            'data'      : model_to_json(self.pre_render()) if self.instance else None
        })

    def __str__(self) :
        return str(self._success)
