"""
A module for extracting features from streaming data.
"""
from .agg import Agg
from .agg import TargetAgg
from .differ import Differ
from .target_encoding import TargetEncoder
from .vectorize import CountVectorizer
from .vectorize import TFIDFVectorizer


__all__ = [
    'Agg',
    'CountVectorizer',
    'Differ',
    'GroupBy',
    'TargetAgg',
    'TargetEncoder',
    'TFIDFVectorizer'
]
