from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1

        if main_count > 1:
            raise ValidationError("Невозможно определить более 1 ключевого раздела")


# class ScopeInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             # В form.cleaned_data будет словарь с данными
#             # каждой отдельной формы, которые вы можете проверить
#             #articles = Article.objects.all()
#             #print(form.cleaned_data.get("is_main"))
#             #if form.cleaned_data.get("is_main"):
#             # вызовом исключения ValidationError можно указать админке о наличие ошибки
#             # таким образом объект не будет сохранен,
#             # а пользователю выведется соответствующее сообщение об ошибке
#             raise ValidationError('Невозможно определить более 1 ключевого раздела')
#         return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeFormSet


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
