from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from .models import Quote
from .forms import QuoteForm


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})


def quote_detail(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    return render(request, 'quotes/quote_detail.html', {'quote': quote})


@login_required
def quote_new(request):
    form = QuoteForm(request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        messages.success(request, 'Added quote')
        return redirect('quotes:quote_list')

    return render(request, 'quotes/quote_form.html', {'form': form})


@login_required
def quote_edit(request, pk):
    quote = get_object_or_404(Quote, pk=pk, user=request.user)
    form = QuoteForm(request.POST or None, instance=quote)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        messages.success(request, 'Updated quote')
        return redirect('quotes:quote_list')

    return render(request, 'quotes/quote_form.html', {'quote': quote,
                                                      'form': form})


@login_required
def quote_delete(request, pk):
    quote = get_object_or_404(Quote, pk=pk, user=request.user)

    if request.method == 'POST':
        quote.delete()
        messages.success(request, 'Deleted quote')
        return redirect('quotes:quote_list')

    return render(request, 'quotes/quote_confirm_delete.html', {'quote': quote})
