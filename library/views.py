from django.utils import timezone
from django.views.generic import \
    ListView, DetailView
from .models import (
    Book,
    Category,
    Author,
    Language,
    Publisher,
    Editor,
    Translator,

)
from django.db.models import Q
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "books/book_lists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Book.objects.all()[:5]


class BookList(ListView):
    model = Book
    context_object_name = 'book_list'
    #template_name = 'books/book_lists.html'
    template_name = 'boighor/index.html'
    paginate_by = 6
    extra_context = {
        'category_list': Category.objects.all(),
        'author_list': Author.objects.all(),
        'language_list': Language.objects.all(),
        'publisher': Publisher.objects.all(),
        'editors': Editor.objects.all(),
        'translators': Translator.objects.all(),
    }

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                Q(name_of_the_book__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(category__name__icontains=query)
            )
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context.update(self.extra_context)
        return context


class SingleCategoryView(DetailView):
    model = Category
    template_name = 'books/single_category.html'
    paginate_by = 12
    extra_context = {
        'category_list': Category.objects.all(),
        'author_list': Author.objects.all(),
        'language_list': Language.objects.all(),
        'publisher': Publisher.objects.all(),
        'editors': Editor.objects.all(),
        'translators': Translator.objects.all(),

    }


class SingleAuthorView(DetailView):
    model = Author
    template_name = 'books/single_author.html'
    extra_context = {
        'category_list': Category.objects.all(),
        'author_list': Author.objects.all(),
        'language_list': Language.objects.all(),
        'publisher': Publisher.objects.all(),
        'editors': Editor.objects.all(),
        'translators': Translator.objects.all(),
    }


class SinglePublisher(DetailView):
    model = Publisher
    template_name = 'books/single_publisher.html'
    extra_context = {
        'category_list': Category.objects.all(),
        'author_list': Author.objects.all(),
        'language_list': Language.objects.all(),
        'publisher': Publisher.objects.all(),
        'editors': Editor.objects.all(),
        'translators': Translator.objects.all(),
    }


class SingleLanguage(DetailView):
    model = Language
    template_name = 'books/single_language_list.html'
    extra_context = {
        'category_list': Category.objects.all(),
        'author_list': Author.objects.all(),
        'language_list': Language.objects.all(),
        'publisher': Publisher.objects.all(),
        'editors': Editor.objects.all(),
        'translators': Translator.objects.all(),
    }


class SingleEditor(DetailView):
    model = Editor
    template_name = 'books/single_editor.html'
    extra_context = {
        'category_list': Category.objects.all(),
        'author_list': Author.objects.all(),
        'language_list': Language.objects.all(),
        'publisher': Publisher.objects.all(),
        'editors': Editor.objects.all(),
        'translators': Translator.objects.all(),
    }


class SingleTranslator(DetailView):
    model = Translator
    template_name = 'books/single_translator.html'
    extra_context = {
        'category_list': Category.objects.all(),
        'author_list': Author.objects.all(),
        'language_list': Language.objects.all(),
        'publisher': Publisher.objects.all(),
        'editors': Editor.objects.all(),
        'translators': Translator.objects.all(),
    }


class BookDetails(DetailView):
    model = Book
    template_name = 'books/book_details.html'
    extra_context = {
        'category_list': Category.objects.all(),
        'author_list': Author.objects.all(),
        'language_list': Language.objects.all(),
        'publisher': Publisher.objects.all(),
        'editors': Editor.objects.all(),
        'translators': Translator.objects.all(),
    }

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context.update(self.extra_context)
        print(context)
        return context
