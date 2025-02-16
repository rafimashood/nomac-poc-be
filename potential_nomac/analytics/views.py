"""This module contains the api's based on analytics data"""
from pathlib import Path

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .redis_utils import get_all_cache_data

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


@api_view(['GET'])
def analyze_data_blocks(request):
    """
    API to fetch data for given blocks within a date range.
    Example request: /api/user/blocks/?blocks=A,B,C&from_date=2024-01-01&to_date=2024-01-31
    Returns: Sample Data OR read from cache
    """
    try:
        cleaning_event = int(request.GET.get('cleaning_event', 0))
        blocks = request.GET.getlist('blocks')
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')

        if not blocks or not from_date or not to_date:
            return Response(
                {"error": "Missing required parameters from: blocks, from_date, to_date"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data, ploty_data = get_all_cache_data(blocks,from_date,to_date,cleaning_event)
        response_data = {
            "data": {"chartData": ploty_data},
            "cached_data": data,
            "message": f"Fetched data for blocks {blocks} from {from_date} to {to_date}."
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
