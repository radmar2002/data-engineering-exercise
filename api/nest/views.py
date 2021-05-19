from django.shortcuts import render

# Create your views here.
import json
import pandas as pd

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated

from .throttles import LimitedRateThrottle, BurstRateThrottle
from collections import defaultdict


def list_nester(input_df, n_levels):

    gr_els = list(n_levels)
    n_levels.append("amount")
    df_reduced = input_df[n_levels]
    grouped_reduced = df_reduced.groupby(gr_els).sum()
    #grouped_reduced_toparse = grouped_reduced.to_dict(orient='index')

    results = defaultdict(lambda: defaultdict(dict))

    for index, value in grouped_reduced.itertuples():
        for i, key in enumerate(index):
            if i == 0:
                nested = results[key]
            elif i == len(index) - 1:
                nested[key] = [{'amount': value}]
            else:
                nested = nested[key]

    res = json.dumps(results, indent=4)
    return res


class NestedAmountsView(APIView):

    permission_classes = [IsAuthenticated]
    throttle_classes = [LimitedRateThrottle]

    def post(self, request, format=None):

        inputdata = request.data
        idata = pd.DataFrame(inputdata)
        nl = ["country", "city", "currency"]
        response_dict = json.loads(list_nester(idata, nl))
        return Response(response_dict, status=200)

    def get(self, request, format=None):
        """
        Return: OK, paste your 'to-be-nested' list here.
        """
        usernames = ""
        return Response("OK, paste your 'to-be-nested' list here.")
