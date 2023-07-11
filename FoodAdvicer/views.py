from django.http import HttpResponse
from django.shortcuts import render
from FoodAdvicer import foodFilter

def index(request):
    if request.method == 'POST':
        # Get the string from the form
        diet=request.POST.get("diet")
        course=request.POST.get("course")
        cuisine=request.POST.get("cuisine")
        time=request.POST.get("time")
        # Use an if-else statement to redirect to the appropriate page
        df = foodFilter.mainFilter(diet,course,cuisine,time)
        #df = df.to_html(buf=None, columns=None, col_space=None, header=True, index=False, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify="center", max_rows=None, max_cols=None, show_dimensions=False, decimal='.', bold_rows=True, classes=None, escape=True, notebook=False, border=1, table_id=None, render_links=True, encoding=None)
        return render(request, 'suggestions.html',{"table":df})
        #return HttpResponse(result)
    else:
        # Render the input form
        return render(request, 'index.html')

def receipe(request,foodid):
    df = foodFilter.receipeShower(foodid)
    return render(request, 'receipe.html',{"table":df})
