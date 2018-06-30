from rest_framework.views import APIView
from rest_framework.response import Response

from tic_tac_toe.serializers import BoardSerializer
from tic_tac_toe.utils import compute_move


class PlayMove(APIView):
    def get(self, request):
        """
        Return played move from 
        """
        board = request.query_params.get('board') or ''
        board = board.replace('+', ' ')
        serializer = BoardSerializer(data={ 'board': board })
        serializer.is_valid(raise_exception=True)
        new_board = compute_move(board)
        return Response({ 'board': new_board })
