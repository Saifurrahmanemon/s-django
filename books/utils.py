
# logic for ratings

def average_rating(rating_list):
    if not rating_list:
        return 0
    return round(sum(rating_list) / len(rating_list))


# this logic is for review section more specifically dealing with formMixin

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['form'] = ReviewForm(initial={'book': self.book_id})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        item = form.save(commit=False)
        item.author = self.request.user
        form.instance.book_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        item.save()
        return super(BookDetailView, self).form_valid(form)
