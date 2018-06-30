from rest_framework import serializers

from tic_tac_toe.utils import board_is_valid


class BoardSerializer(serializers.Serializer):
    board = serializers.CharField(min_length=9, max_length=9)

    def validate_board(self, value):
        """
        Check that the board is valid.
        """
        if not board_is_valid:
            raise serializers.ValidationError("Invalid Board")
        return value
