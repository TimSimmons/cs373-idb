from django.core.serializers.json import Serializer

class JSONSerializer(Serializer):

    def end_serialization(self):
        for i, ob in enumerate(self.objects):
            self.objects[i] = ob.get('fields', {})
        return super(JSONSerializer, self).end_serialization()