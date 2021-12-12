from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Track,Genre
import json
import requests

# Create your views here.

class TrackView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,id=0):
        if(id>0):
            tracks = list(Track.objects.filter(id=id).values() )
            if len(tracks) > 0:
                track = tracks[0]
                track['genres'] = []
                query_track = Track.objects.filter(id=id).all()
                track_genres = list(query_track[0].genres.all())
                for g in track_genres:
                    genre = {
                        'genreId': g.genreId,
                        'url': g.url,
                        'name': g.name,
                        }
                    track['genres'].append(genre)

                datos = {'message': "Success",'Track': track}
            else:
                datos = {'message': "Track not found ..."}
            return JsonResponse(datos)
        else:
            tracks = list(Track.objects.values())
            if len(tracks) > 0:
                for t in tracks:
                    t['genres'] = []
                    query_track = Track.objects.filter(id=t['id']).all()

                    track_genres = list(query_track[0].genres.all())
                    for g in track_genres:
                        genre = {
                            'genreId': g.genreId,
                            'url': g.url,
                            'name': g.name,
                        }
                        t['genres'].append(genre)

                datos = {'message': "Success",'tracks': tracks}
            else:
                datos = {'message': "tracks not found ..."}
            return JsonResponse(datos)

    def post(self, request):

        jd = json.loads(request.body)

        track = Track(
        name=jd['name'],
        artistName=jd['artistName'],
        id=jd['id'],
        releaseDate=jd['releaseDate'],
        kind=jd['kind'],
        artistId=jd['artistId'],
        artistUrl=jd['artistUrl'],
        contentAdvisoryRating=jd['contentAdvisoryRating'] if 'contentAdvisoryRating' in jd else "",
        artworkUrl100=jd['artworkUrl100'],
        url=jd['url'],)

        track.save()

        for genre in list(jd['genres']):
            g = Genre(
            genreId=genre['genreId'],
            url=genre['url'],
            name=genre['name'],)

            g.save()
            track.genres.add(g)

        
        datos = {'message':"Success"}
        return JsonResponse(datos)


    def delete(self, request,id):
        #tracks = list(Track.objects.filter(id=id).values() )
        track = Track.objects.filter(id=id)
        if track:
            track.delete() 
            datos = {'message':"Success"}
        else:
            datos = {'message': "Track not found ..."}
        return JsonResponse(datos)


class TopTrackView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,top):
        response = requests.get('https://rss.applemarketingtools.com/api/v2/us/music/most-played/'+str(top)+'/songs.json')
        
        return JsonResponse({'message':"Success",'results':response.json()['feed']['results']})


