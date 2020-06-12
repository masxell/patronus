from django.shortcuts import render
from .models import Reference
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
@login_required
def reference_list(request):
    # references = Reference.objects.all()
    object_list = Reference.objects.all()

    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')

    try:
        references = paginator.page(page)
    except PageNotAnInteger:
        references = paginator.page(1)
    except EmptyPage:
        references = paginator.page(paginator.num_pages)

    return render(request, 'reference/post/list.html', {'page':page, 'references' : references})

# class ReferenceListView(LoginRequiredMixin, ListView):
#     queryset = Reference.published.all()
#     context_object_name = 'references'
#     paginate_by = 2
#     template_name = 'reference/post/list.html'

#     def get_queryset(self):
#         qs = super().get_queryset()
        
#         return qs
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.tag:
#             context['tag'] = self.tag
#         return context

class ReferenceCreateView(LoginRequiredMixin, CreateView):
    model = Reference
    # fields = ['title', 'slug', 'author', 'body', 'tags', 'status']
    fields = ['title', 'description', 'link']
    template_name = 'reference/post/reference_form.html'
    success_url = reverse_lazy('reference:reference_list')

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class ReferenceUpdateView(LoginRequiredMixin, UpdateView):
    model = Reference
    fields = ['title', 'description', 'link']
    template_name = 'reference/post/reference_form.html'
    success_url = reverse_lazy('reference:reference_list')

    query_pk = True

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author = self.request.user)

    def form_valid(self, form):
        return super().form_valid(form)

class ReferenceDeleteView(LoginRequiredMixin, DeleteView):
    model = Reference
    template_name = 'reference/post/reference_confirm_delete.html'
    success_url = reverse_lazy('reference:reference_list')
    query_pk = True

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author = self.request.user)    