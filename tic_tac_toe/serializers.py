from rest_framework import serializers

from tic_tac_toe.utils import board_is_valid, is_correct_turn


class BoardSerializer(serializers.Serializer):
    board = serializers.CharField(min_length=9, max_length=9)

    def validate_board(self, value):
        """
        Check that the board is valid.
        """
        if not board_is_valid(value):
            raise serializers.ValidationError("Invalid Board")
        elif not is_correct_turn(value):
            raise serializers.ValidationError("Oops, someone missed a turn")
        return value
