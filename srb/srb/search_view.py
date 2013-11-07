from srb.models import Library, Read_alignment
from rest_framework import serializers, viewsets, renderers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class AlignSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many =True, view_name ="snippet-detail")
    class Meta:
        model = Read_alignment
        fields = ('chr','start','stop','NormRead')
    
class AlignViewSet(viewsets.ReadOnlyModelViewSet):
<<<<<<< Updated upstream
    queryset = Read_alignment.objects.all()
    serializer_class = AlignSerializer

=======
    model = Read_alignment
    serializer_class = AlignSerializer
    queryset = Read_alignment.objects.select_related().filter(chr='chr3L')
    
>>>>>>> Stashed changes
class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        
    
class AlignRetrieveAPIView(RetrieveUpdateAPIView):
    model = Read_alignment
    serializer_class = AlignSerializer
    queryset = Read_alignment.objects.select_related().filter(chr='chr3L')
