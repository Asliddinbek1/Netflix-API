from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from film.models import Actor, Comment, Movie
from film.serializers import ActorSerializers, CommentSerializers, MovieSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import filters


class ActorViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers    


# class CommentViewSet(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializers
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]


class CommentAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializers(comment, many=True)
        return Response(data = serializer.data)
    
    def post(self, request):
        request.data['user_id'] = self.request.user.id
        serializer = CommentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Added"})
        else:
            return Response({"status":"Error"})

    def delete(self, request, id):
        comment = Comment.objects.all().filter(id = id)
        if comment and comment[0].user_id.id == self.request.user.id :
            comment.delete()
            return Response({"status": 'deleted'})
        elif comment:
            return Response({"status": 'Error: Bu komentariyani siz o`chira olmaysiz'})

        else:
            return Response({"status": 'Error: Buday komentariya mavjud emas'})

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["imdb"]
    search_fields = ["name", "year", "imdb", "genre"]

    @action(detail = True, methods = ["GET"])
    def actors(self, request, *args, **kwargs):
        
        movie = self.get_object()
        serializer = ActorSerializers(movie.actors.all(), many = True)
        return Response(serializer.data)


    @action(detail=True, methods=['post'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        a = Actor.objects.filter(id=request.data['id'])
        if len(a) != 0:
            movie.actors.add(a[0])
            movie.save()
            return Response({'satus' : 'added'})
        else:
            return Response({'satus' : 'Error: Bunday id dagi actor mavjud emas'})
    

    @action(detail=True, methods=["delete"])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        a = Actor.objects.filter(id = request.data["id"]) 
        try:
            movie.actors.remove(a[0])
            movie.save()
            return Response({"status": "Removed"})
        except:
            return Response({"status": "Error: Bunday actor, Movie da mavjud emas"})



class MovieActorAPIView(ModelViewSet):
    serializer_class = MovieSerializers
    queryset = Movie.objects.all()