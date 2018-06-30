from rest_framework.views import APIView
from django.http import HttpResponse

from tic_tac_toe.serializers import BoardSerializer
from tic_tac_toe.utils import compute_move, BoardNotValidException


class PlayMove(APIView):
    def get(self, request):
        """
        Return played move from board 
        """
        board = request.query_params.get('board') or ''
        serializer = BoardSerializer(data={ 'board': '[{}]'.format(board) })
        serializer.is_valid(raise_exception=True)
        new_board = compute_move(board)
        return HttpResponse(new_board)
