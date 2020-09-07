from enum import Enum


class QuerySizeEnum(str, Enum):
    """
    Where `length` is the larger of image `size.height` or image `size.width`,
    \n `small`: length range = 0px - 499px
    \n `medium`: length range = 500px - 999px
    \n `large`: length range = 1000px -
    """

    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
