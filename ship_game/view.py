import matplotlib.pyplot as plt
from matplotlib import patches

LETTERS = "ABCDEFGHIJ"


class View:
    def __init__(self):
        self.fig, (self.ax_own, self.ax_foe) = plt.subplots(1, 2, figsize=(14, 7))
        self._configure(self.ax_own)
        self._configure(self.ax_foe)
        self.fig.tight_layout()
        self.fig.show()

    @staticmethod
    def _configure(ax):
        ax.set_xlim(-0.5, 9.5)
        ax.set_ylim(-0.5, 9.5)
        ax.set_xticks(range(10))
        ax.set_xticklabels(list(LETTERS))
        ax.set_yticks(range(10))
        ax.set_yticklabels(range(10, 0, -1))
        ax.set_aspect("equal", adjustable="box")
        ax.grid(True)

    def _clear(self, ax):
        ax.clear()
        self._configure(ax)

    def _mark_shots(self, ax, board):
        for row, col in board.shots:
            if board.grid[row][col] is not None:
                ax.plot(col, row, "X", color="red", markersize=10)
            else:
                ax.plot(col, row, "o", color="gray", markersize=6)

    def update(self, model):
        self._clear(self.ax_own)
        self._clear(self.ax_foe)
        self.ax_own.set_title(f"{model.shooter.player_name}: your fleet")
        self.ax_foe.set_title(f"{model.target.player_name}: enemy waters")
        for ship in model.shooter.ships:
            row, col = ship.cells[0]
            width = ship.length if ship.horizontal else 1
            height = 1 if ship.horizontal else ship.length
            color = "red" if ship.sunk else "steelblue"
            self.ax_own.add_patch(
                patches.Rectangle((col - 0.5, row - 0.5), width, height,
                                  facecolor=color, edgecolor="black", alpha=0.85))
        self._mark_shots(self.ax_own, model.shooter)
        self._mark_shots(self.ax_foe, model.target)
        self.fig.canvas.draw_idle()