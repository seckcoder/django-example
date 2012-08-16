from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.http import HttpResponseForbidden
from django import forms
from models import *

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(User)
admin.site.register(Message)

class ForumAdminForm(forms.ModelForm):
    class Meta:
        model = Forum
    messages = forms.ModelMultipleChoiceField(
        queryset = Message.objects.all(), required=False,
        widget = FilteredSelectMultiple('Messages', False))
    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            initial = kwargs.setdefault('initial', {})
            initial['messages'] = [t.message.pk for t in kwargs['instance'].message_forum_set.all()]
        super(ForumAdminForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        if not self.is_valid():
            raise HttpResponseForbidden
        #instance = super(ForumAdminForm, self).save(self, commit)
        instance = forms.ModelForm.save(self, commit)
        old_save_m2m = self.save_m2m
        def save_m2m():
            #old_save_m2m()
            messages = [s for s in self.cleaned_data['messages']]
            for mf in instance.message_forum_set.all():
                if mf.message not in messages:
                    mf.delete()
                else:
                    messages.remove(mf.message)
            for message in messages:
                Message_forum.objects.create(message=message, forum=instance)

        self.save_m2m = save_m2m
            
        return instance

class ForumAdmin(admin.ModelAdmin):
    form = ForumAdminForm

admin.site.register(Forum, ForumAdmin)
admin.site.register(Message_forum)
