from constants import *

heights = [80.0, 240.0, 400.0, 560.0, 720.0]
for tree_level in range(1,6):
    widths = [((2 * i - 1) * SCREEN_WIDTH) / 2 ** tree_level for i in range(1, 2**(tree_level-1) + 1)]
    print(widths)
