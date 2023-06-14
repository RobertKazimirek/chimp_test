import DataContainer
import stage


def run_session(session_number, window, is_training):
    session_data = DataContainer.Session(session_number+1, [], [], 0)
    n = 4
    strikes = 0

    stage_number = 1
    while strikes < 3 and n <= 20 and (not is_training or n <= 6):
        n, strikes_change, stage_data = stage.run_stage(stage_number, window, n)

        if strikes_change:
            session_data.errorStages.append(n)
            strikes += 1

        session_data.stages.append(stage_data)
        stage_number += 1

    session_data.lastStage = min(n, 20)
    return session_data
