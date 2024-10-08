from unittest.mock import patch
from script import guess_number_game


##Test for winning on first attempt
@patch('builtins.input', side_effect=["John", "5", "7", "9"])
def test_user_wins_on_first_attempt(mock_input):
    result = guess_number_game(random_number=5)
    assert result is True

##Test for winning on second attempt
@patch('builtins.input', side_effect=["John", "5", "7", "9"])
def test_user_wins_on_second_attempt(mock_input):
    result = guess_number_game(random_number=7)
    assert result is True
    
##Test for winning on third attempt
@patch('builtins.input', side_effect=["John", "5", "7", "9"])
def test_user_wins_on_third_attempt(mock_input):
    result = guess_number_game(random_number=9)
    assert result is True
    
# Test for losing the game
@patch('builtins.input', side_effect=["John", "5", "7", "9"])
def test_user_loses(mock_input):
    result = guess_number_game(random_number=1)
    assert result is False
    
