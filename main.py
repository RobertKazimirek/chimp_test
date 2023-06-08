import dataclasses
import boards
import DataContainer
import session

from psychopy import visual, core, event, clock
import json
import datetime


def save_results(data_container):
    data = dataclasses.asdict(data_container)
    json_data = json.dumps(data)

    with open(f"Results\\chimp_test_{str(datetime.datetime.now()).replace(' ', '_').replace(':', '-')[:-7]}.json", "x") as file:
        file.write(json_data)


def main():
    window = visual.Window(units="height", fullscr=True, monitor=None, color=(10, 26, 26), colorSpace='rgb255')
    data_container = DataContainer.DataContainer([])

    boards.show_instruction(window)
    result = session.run_session(0, window, True).lastStage
    boards.show_training_end_board(window, result)
    for i in range(3):
        session_data = session.run_session(i, window, False)
        data_container.sessions.append(session_data)
        boards.show_score_board(window, i+1, session_data.lastStage)
    boards.show_final_board(window, data_container.sessions[-1].lastStage)

    save_results(data_container)

    window.close()
    core.quit()


if __name__ == '__main__':
    main()

