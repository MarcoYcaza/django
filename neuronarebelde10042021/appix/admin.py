from django.contrib import admin
from appix.models import (
    SimpleCard,
    Tag,
    InLineImagexCard,
    ImageCard,
    Subject,
    InLineChoicexCard,
    MultipleChoiceCard,
)

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    fields = ("tagName",)


class SubjectAdmin(admin.ModelAdmin):
    fields = ("subjectName", "description")


class SimpleCardAdmin(admin.ModelAdmin):
    fields = ("question", "answer", "counter", "subject", "tag")


class InLineImagexCardAdmin(admin.StackedInline):
    model = InLineImagexCard


class ImageCardAdmin(admin.ModelAdmin):
    fields = ("question", "counter", "subject", "tag")
    inlines = [InLineImagexCardAdmin]

    class Meta:
        model = ImageCard


class InLineChoicexCardAdmin(admin.StackedInline):
    model = InLineChoicexCard


class MultipleChoiceCardAdmin(admin.ModelAdmin):
    fields = ("question", "counter", "subject", "tag")
    inlines = [InLineChoicexCardAdmin]

    class Meta:
        model = ImageCard


admin.site.register(SimpleCard, SimpleCardAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(MultipleChoiceCard, MultipleChoiceCardAdmin)
admin.site.register(ImageCard, ImageCardAdmin)
admin.site.register(Tag, TagAdmin)
