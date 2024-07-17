from rest_framework import serializers
from .models import City, Attraction, Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only=True
    )

    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset=Attraction.objects.all(),
        source='attraction'
    )

    class Meta:
        model = Review
        fields = ('id', 'atttraction', 'attraction_id', 'title', 'description', 'photo_url')


class AttractionSerializer(serializers.HyperLinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )

    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )

    class Meta:
        model = Attraction
        fields = ('id', 'city', 'city_id', 'name', 'price', 'photo_url')
  

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        many=True,
        read_only=True
    )

    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'
    )

    class Meta:
        model = City
        fields = ('id', 'name', 'population', 'photo_url')

