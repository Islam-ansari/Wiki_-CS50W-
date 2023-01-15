from django.shortcuts import render
from django.http import HttpResponse
import markdown2, random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "heading": "All Pages"
    })

# using markdown2, to convert output of get_entry() to html syntax
def convert_HTML(title):
    entry = util.get_entry(title)
    if entry:
        html = markdown2.markdown(entry)
    else:
        return None
    return html

def entry(request, entry):
    if util.get_entry(entry) != None:
        return render(request, "encyclopedia/entry.html", {
                "entry": convert_HTML(entry),
                "title": entry.capitalize()
    })
    else:
        return render(request, "encyclopedia/error.html", {
                "heading": "404, Page not found",
                "title": entry.capitalize()
    })

def search(request):
    if request.method == 'GET':
        entry = request.GET.get('q')
        entry_content = util.get_entry(entry)
        if entry_content != None:
            return render(request, "encyclopedia/entry.html", {
                    "entry": convert_HTML(entry),
                    "title": entry        
        })
        else:
            pages = util.list_entries()
            search_pages = []

            for page in pages:
                if entry.upper() in page.upper():
                    search_pages.append(page)
                
            if len(search_pages)!=0:
                return render(request, "encyclopedia/index.html", {
                    "entries": search_pages,
                    "heading": f"Search results for '{entry}'",
                })
            else:
                return render(request, "encyclopedia/error.html", {
                        "heading": "404, Page not found",
                        "title": entry.capitalize()
                })

def new_entry(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new_entry.html")
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                        "heading": "404, Page already exists",
                        "title": title
            })
        else:
            util.save_entry(title, content)    
            return render(request, "encyclopedia/entry.html", {
                            "entry": convert_HTML(title),
                            "title": title.capitalize()
            })
    
def random_page(request):
    random_page = random.choice(util.list_entries())
    return render(request, "encyclopedia/entry.html", {
            "entry": convert_HTML(random_page),
            "title": random_page.capitalize()
    })

def edit_page(request):
    if request.method == "POST":
        title = request.POST.get('entry_title')
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "content": content
        })

def save_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(title, content)    
        return render(request, "encyclopedia/entry.html", {
                            "entry": convert_HTML(title),
                            "title": title.capitalize()
        })

