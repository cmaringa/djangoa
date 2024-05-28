# myapp/views.py
from django.shortcuts import render
from django.db import connection
from .models import IndexTS
from .forms import FilterForm

def item_list(request):
    form = FilterForm(request.GET or None)
    selected_symbol = None
    selected_date = None
    data = []

    if form.is_valid():
        selected_symbol = form.cleaned_data['index_symbol']
        selected_date = form.cleaned_data['date']
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT ts.Date, ts.Index_Symbol, ts.ISIN, ts.Shares, 
                ts.Free_Float, ts.Capfactor, ts.Price, 
                    (ts.Shares * ts.Free_Float * ts.Capfactor * ts.Price) as Market_Cap,
                ts.load_time, s.Instrument_Name
                FROM index_ts ts
                LEFT JOIN (select distinct(ISIN), Instrument_Name from 
                index_static) 
                s ON 
                ts.ISIN = s.ISIN
                WHERE ts.Index_Symbol = %s and (ts.Date) = %s
            ''', [selected_symbol, selected_date])
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in rows]

            # Calculate the total sum of the Product
            total_product = sum(item['Market_Cap'] for item in data)

            # Add Weight to each item
            for item in data:
                item['Weight'] = item['Market_Cap'] / total_product * 100 \
                    if (total_product) else 0

    return render(request, 'myapp/item_list.html', {'form': form, 'data': data})
