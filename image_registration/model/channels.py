"""
a short description for channels ...

"""


class Channels(object):

    # python 2.7 does not provide enum out-of-box, and
    # it turns out that the following is the simplest
    # method to achieve enum-like functionality.
    GRAY = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class MarkerChannelAssociation(object):
    """
    some description about this association.
    """
    associations = {
        # Gray channel:
        'CD20': Channels.GRAY, 'CD56': Channels.GRAY, 'RORGT': Channels.GRAY, 'P16': Channels.GRAY,
        'CD3': Channels.GRAY,

        # Red channel:
        'FOXP3': Channels.RED, 'CK5': Channels.RED, 'CK14': Channels.RED, 'PDL1': Channels.RED,
        'PD-L1': Channels.RED, 'PD1': Channels.RED, 'MHC II': Channels.RED, 'MHCII': Channels.RED,
        'DC-SIGN': Channels.RED, 'CK19': Channels.RED, 'F480': Channels.RED,

        # Green channel:
        'DC LAMP': Channels.GREEN, 'DC-LAMP': Channels.GREEN, 'CD83': Channels.GREEN, 'CD11C': Channels.GREEN,
        'TIM3': Channels.GREEN,

        # Channels.BLUE channel:
        'CD45': Channels.BLUE, 'CD4': Channels.BLUE, 'CD8': Channels.BLUE, 'EOEMS': Channels.BLUE,
        'TBR2': Channels.BLUE, 'TBET': Channels.BLUE, 'T-BET': Channels.BLUE, 'GRZB': Channels.BLUE,
        'GRANZYME B': Channels.BLUE, 'GRANZYMEB': Channels.BLUE, 'ICOS': Channels.BLUE, 'IDO': Channels.BLUE,
        'IL10': Channels.BLUE,'KI67': Channels.BLUE, 'PD1': Channels.BLUE, 'EOMES': Channels.BLUE,
        'CK': Channels.BLUE, 'BTK': Channels.BLUE, 'NKP46': Channels.BLUE, 'CD56': Channels.BLUE,
        'CSF1R': Channels.BLUE, 'CD66B-': Channels.BLUE, 'CD66B': Channels.BLUE,'CD163': Channels.BLUE,
        'CD3CD20NK': Channels.BLUE,'PANCK': Channels.BLUE,'SMA': Channels.BLUE, 'CD32056': Channels.BLUE,
        'CD320NKP46': Channels.BLUE, 'CD3-20-56': Channels.BLUE, 'TRYPTASE': Channels.BLUE,
        'CD68': Channels.BLUE,'ASCF1R': Channels.BLUE, 'CD207': Channels.BLUE, 'CD206': Channels.BLUE,
        'B220': Channels.BLUE, 'LY6G': Channels.BLUE, 'GATA3': Channels.BLUE, 'CD11B': Channels.BLUE,
        'TCF1TCF7': Channels.BLUE
    }
