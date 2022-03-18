from rest_framework import serializers

from base.models import Member

class MemberSerializer(serializers.ModelSerializer):
   class Meta:
       model = Member
       fields = ('first_name', 'number')