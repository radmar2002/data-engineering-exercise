from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated

from .throttles import LimitedRateThrottle, BurstRateThrottle


class NestedAmountsView(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [LimitedRateThrottle]

    def post(self, request, format=None):
        data = request.data
        response_dict = {"nested_amounts": data}
        return Response(response_dict, status=200)

    def get(self, request, format=None):
        """
        Return: OK, paste your 'to-be-nested' list here.
        """
        usernames = ""
        return Response("OK, paste your 'to-be-nested' list here.")
