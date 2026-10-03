import random

from model import FLEET, SIZE, GameModel


def test_fleet_complete_and_inside_grid():
    model = GameModel()
    for board in model.boards:
        assert len(board.ships) == len(FLEET)
        assert sum(s.length for s in board.ships) == sum(FLEET)
        for ship in board.ships:
            assert all(0 <= r < SIZE and 0 <= c < SIZE for r, c in ship.cells)
        assert len(board.shots) == 0


def test_miss_switches_turn_and_double_fire_ignored():
    model = GameModel()
    empties = [(r, c) for r in range(SIZE) for c in range(SIZE)
               if model.target.grid[r][c] is None]
    assert empties
    row, col = empties[0]
    before = model.current
    assert model.fire(row, col) == "miss"
    assert model.current == 1 - before
    assert model.fire(row, col) == "already"
    assert model.current == 1 - before


def test_out_of_bounds_and_already_reported():
    model = GameModel()
    assert model.fire(-1, 0) == "invalid"
    assert model.fire(SIZE, SIZE) == "invalid"


def test_full_game_terminates():
    random.seed(1)
    model = GameModel()
    for _ in range(1000):
        if model.game_over:
            break
        model.fire(random.randrange(SIZE), random.randrange(SIZE))
    assert model.game_over
    assert model.winner() in ("Player 1", "Player 2")
    loser = model.boards[1 - model.boards.index(
        next(b for b in model.boards if b.player_name == model.winner))]
    assert loser.all_sunk()
