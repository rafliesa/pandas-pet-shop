from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'Pandas Pet Store',
        'nama' : 'Muhammad Rafli Esa Pradana',
        'class' : 'PBP-D'
    }

    return render(request, "main.html", context)