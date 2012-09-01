from django.contrib import admin
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.http import HttpResponseForbidden
from django import forms
from models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'update_date')
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'update_date')
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry)
admin.site.register(MUser)
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

CHOICES = (('red', 'Red'), ('green', 'Green'))
SINGLE_CHOICES = (('unknown', 'unknown',),
                  ('yes', 'Yes'),
                  ('no', 'No'))

class FakeEntryAdminForm(forms.ModelForm):
    class Meta:
        model = FakeEntry
        fields = ('blog', 'headline', 'authors')
    demo_select  = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    demo_boolselect = forms.ChoiceField(widget=forms.NullBooleanSelect,
                                        choices=SINGLE_CHOICES)
    demo_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    demo_select_multi = forms.MultipleChoiceField(widget=forms.SelectMultiple,
                                          choices=CHOICES)
    demo_multi_choice = forms.MultipleChoiceField(choices=CHOICES)
    demo_multi_choice1 = forms.MultipleChoiceField(
        widget=CheckboxSelectMultiple, choices=CHOICES)

class FakeEntryAdmin(admin.ModelAdmin):
    form = FakeEntryAdminForm

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_detail')

class StudyOrderAdmin(admin.ModelAdmin):
    list_display = ('author', 'update_date')
admin.site.register(Forum, ForumAdmin)
admin.site.register(Message_forum)
admin.site.register(FakeEntry, FakeEntryAdmin)
admin.site.register(Blogpost)
admin.site.register(Post, PostAdmin)
admin.site.register(StudyOrder, StudyOrderAdmin)
