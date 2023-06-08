import boards
import DataContainer

from psychopy import visual, event, clock

import random


def create_random_squares(window, n):
    positions = list(range(20))
    random.shuffle(positions)
    positions = positions[:n]

    squares = []
    for number, position in enumerate(positions):
        y = (position // 5 - 1.5) * 0.24
        x = (position % 5 - 2) * 0.24

        new_square = visual.rect.Rect(window, pos=(x, y), width=0.2, height=0.2, color=(240, 250, 250), colorSpace= 'rgb255')
        new_square.draw()
        squares.append(new_square)

        visual.TextBox2(window, text=f'{number+1}', font="Open Sans", pos=(x, y), alignment='centre', letterHeight=0.16, bold=True, color=(10, 26, 26), colorSpace='rgb255').draw()
    window.flip()

    return list(zip(positions, squares))


def draw_new_squares(window, pos_squares):
    for _, square in pos_squares:
        square.draw()

    window.flip()


def handle_selection(stage_data, pos_squares, idx, m_clock):
    event.Mouse()

    stage_data.selectedSquares.append((pos_squares[idx][0] % 5, pos_squares[idx][0] // 5))
    stage_data.actionTimes.append(m_clock.getTime())
    m_clock.reset()


def run_stage(stage_number, window, n):
    pos_squares = create_random_squares(window, n)

    squares_locations = [(pos_square[0] % 5, pos_square[0] // 5) for pos_square in pos_squares]  # (x, y) format
    stage_data = DataContainer.Stage(stage_number, squares_locations, [], [])
    m_clock = clock.Clock()

    mouse = event.Mouse(visible=True)

    while len(pos_squares) > 0:
        if mouse.isPressedIn(pos_squares[0][1]):
            handle_selection(stage_data, pos_squares, 0, m_clock)

            pos_squares.pop(0)
            draw_new_squares(window, pos_squares)

        else:
            for i in range(1, len(pos_squares)):
                if mouse.isPressedIn(pos_squares[i][1]):
                    handle_selection(stage_data, pos_squares, i, m_clock)

                    boards.show_error_board(window)
                    return n, True, stage_data

    return n + 1, False, stage_data
