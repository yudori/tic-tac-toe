from rest_framework import serializers

from tic_tac_toe.utils import board_is_valid, is_correct_turn


class BoardSerializer(serializers.Serializer):
    board = serializers.CharField(max_length=11, allow_blank=True)

    def validate_board(self, value):
        """
        Check that the board is valid.
        """
        value = value[1:-1]
        print (value)
        if not value or not board_is_valid(value):
            raise serializers.ValidationError("Invalid Board")
        elif not is_correct_turn(value):
            raise serializers.ValidationError("Oops, someone missed a turn")
        return value
