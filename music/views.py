from django.http import HttpResponse
from .models import  Album, Song
from django.shortcuts import render, get_object_or_404


def index(request):
    all_albums = Album.objects.all() #getting all album objects from the database
    #template=loader.get_template('music/index.html')  #loading the template from music
    context = {
        'all_albums': all_albums, # this is a dictionary to pass data to the template
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    #return HttpResponse("<h2> Album id is " + str(album_id) + "</h2>")
    album=get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album' : album})


def favorite(request, album_id):
    album = get_object_or_404(Album , pk=album_id)
    try:
        select_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request,'music/detail.html',
                      {'album': album ,
                       'error_message': 'You did not selet a valid song', }
                      )
    else:
        select_song.is_favorite = True
        select_song.save()
        return render(request, 'music/detail.html', {'album': album} )