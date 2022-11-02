from rest_framework import serializers
from .models import SlackDeveloper

class SlackDeveloperSerializers(serializers.ModelSerializer):

    class Meta:
        model = SlackDeveloper
        fields = ['slackUsername', 'backend', 'age', 'bio',]