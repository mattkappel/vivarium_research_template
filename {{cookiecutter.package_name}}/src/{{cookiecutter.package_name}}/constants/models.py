from {{cookiecutter.package_name}}.constants import data_keys

###########################
# Disease Model variables #
###########################

class TransitionString(str):

    def __new__(cls, value):
        # noinspection PyArgumentList
        obj = str.__new__(cls, value.lower())
        obj.from_state, obj.to_state = value.split('_TO_')
        return obj


# TODO input details of model states and transitions
SOME_MODEL_NAME = data_keys.SOME_DISEASE.name
SUSCEPTIBLE_STATE_NAME = f'susceptible_to_{SOME_MODEL_NAME}'
FIRST_STATE_NAME = 'first_state'
SECOND_STATE_NAME = 'second_state'
SOME_DISEASE_MODEL_STATES = (SUSCEPTIBLE_STATE_NAME, FIRST_STATE_NAME, SECOND_STATE_NAME)
SOME_DISEASE_MODEL_TRANSITIONS = (
    TransitionString(f'{SUSCEPTIBLE_STATE_NAME}_TO_{FIRST_STATE_NAME}'),
    TransitionString(f'{FIRST_STATE_NAME}_TO_{SECOND_STATE_NAME}'),
    TransitionString(f'{SECOND_STATE_NAME}_TO_{FIRST_STATE_NAME}')
)


STATES = tuple(state for model in STATE_MACHINE_MAP.values() for state in model['states'])
TRANSITIONS = tuple(state for model in STATE_MACHINE_MAP.values() for state in model['transitions'])