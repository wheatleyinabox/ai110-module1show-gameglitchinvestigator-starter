from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the Higher/Lower hint bug ---

def test_too_high_guess_says_go_lower():
    # Guess above the secret: the player needs to go LOWER
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_guess_says_go_higher():
    # Guess below the secret: the player needs to go HIGHER
    outcome, message = check_guess(1, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_edges_of_range():
    # Guessing 1 should never say "go lower", guessing 100 never "go higher"
    assert "HIGHER" in check_guess(1, 2)[1]
    assert "LOWER" in check_guess(100, 99)[1]


# --- Regression tests for the New Game reset bug ---

from pathlib import Path
from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")


def _finished_game(status):
    at = AppTest.from_file(APP_PATH).run()
    at.session_state["status"] = status
    at.session_state["history"] = [10, 20, 30]
    at.session_state["score"] = 42
    return at

def _click(at, label):
    next(b for b in at.button if label in b.label).click()
    return at.run()

def test_new_game_resets_state_after_loss():
    at = _click(_finished_game("lost"), "New Game")
    assert at.session_state["status"] == "playing"
    assert at.session_state["history"] == []
    assert at.session_state["score"] == 0

def test_new_game_resets_state_after_win():
    at = _click(_finished_game("won"), "New Game")
    assert at.session_state["status"] == "playing"

def test_can_guess_after_new_game():
    at = _click(_finished_game("lost"), "New Game")
    at.text_input[0].set_value("5")
    at = _click(at, "Submit Guess")
    assert at.session_state["history"] == [5]
    assert not at.error  # no "Game over" message blocking the guess

def test_new_game_secret_respects_difficulty():
    at = AppTest.from_file(APP_PATH).run()
    at.sidebar.selectbox[0].select("Easy").run()
    for _ in range(20):
        at = _click(at, "New Game")
        assert 1 <= at.session_state["secret"] <= 20
