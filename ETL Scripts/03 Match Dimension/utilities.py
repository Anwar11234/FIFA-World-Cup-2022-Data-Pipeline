def map_pens(pens):
    if pens == 'N':
        return 'No'
    elif pens == 'Y':
        return 'Yes'
    else:
        return 'N/A - Group Stage'

def map_rounds(round):
    rounds = {
        32: 'Group Stage',
        16: 'Round of 16',
        8: 'Quarter Fianl',
        4: 'Semi Final',
        12: 'Final',
        34: 'Match for third place'
    }
    return rounds[round]