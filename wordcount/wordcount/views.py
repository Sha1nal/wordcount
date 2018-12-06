from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def count(request):
    fulltext = request.GET['fulltext']
    compare_list = fulltext.split()
    final_list = []
    found = False

    
    for x in compare_list:
        for y in final_list:
            if x == y[0]:
                y[1] += 1
                found = True
                break
        if found == False:
            final_list.append([x, 1])
        found = False
    
    for x in final_list:
        print(x)
    
    return render(request, 'count.html', {'fulltext': fulltext, 'list': final_list})

def about(request):
    return render(request, 'about.html')

