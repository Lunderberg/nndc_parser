class Level(object):
    def __init__(self):
        self.energy = None
        self.energy_uncertainty = None
        self.transitions_from = []
        self.transitions_to = []
        self.spin_parity = None

    @staticmethod
    def IsValidRecord(line):
        can_be_level_record = line[7]=='L'
        is_not_comment = line[6]==' '
        is_not_continuation = line[5]==' '
        return can_be_level_record and is_not_comment and is_not_continuation

    @staticmethod
    def FromRecord(line):
        output = Level()
        output.energy = float(line[9:19].strip())

        energy_uncertainty = line[19:21].strip()
        if energy_uncertainty:
            output.energy_uncertainty = float(energy_uncertainty)

        spin_parity = line[21:39].strip()
        if spin_parity:
            output.spin_parity = spin_parity

        return output


class Transition(object):
    def __init__(self):
        self.energy = None
        self.initial_state = None
        self.final_state = None

    @staticmethod
    def IsValidRecord(line):
        can_be_gamma_record = line[7]=='G'
        is_not_comment = line[6]==' '
        is_not_continuation = line[5]==' '
        return can_be_gamma_record and is_not_comment and is_not_continuation

    @staticmethod
    def FromRecord(line):
        output = Transition()
        output.energy = float(line[9:19].strip())

        energy_uncertainty = line[19:21].strip()
        if energy_uncertainty:
            output.energy_uncertainty = energy_uncertainty

        return output


def parse_table(table):
    all_levels = []
    current_level = None
    for line in table.split('\n'):
        # Pad to 80 characters, makes parsing fixed-width formats easier
        line = line + ' '*(80-len(line))

        if Level.IsValidRecord(line):
            level = Level.FromRecord(line)
            if current_level is not None:
                all_levels.append(current_level)
            current_level = level

        if Transition.IsValidRecord(line):
            transition = Transition.FromRecord(line)
            initial_state = current_level
            final_state = min(all_levels,
                  key=lambda state:abs(state.energy - (current_level.energy - transition.energy)))

            transition.initial_state = initial_state
            transition.final_state = final_state
            initial_state.transitions_from.append(transition)
            final_state.transitions_to.append(transition)


    if current_level is not None:
        all_levels.append(current_level)

    return all_levels
