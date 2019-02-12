from collections.abc import Mapping
from abc import ABC, abstractproperty


class PrivacyModel(ABC, Mapping):
    """ ABC for ARX Privacy Models"""

    def __init__(self):
        self._internal_dict = {}

    def __getitem__(self, item):
        return self._internal_dict[item]

    def __len__(self) -> int:
        return len(self._internal_dict)

    def __iter__(self):
        return iter(self._internal_dict)

    @property
    def name(self) -> str:
        return self._anonymity_name

    def __str__(self):
        return self._print_messqge

class KAnonymity(PrivacyModel):
    """ Configuration class for KAnonymity"""

    def __init__(self, k):
        self._internal_dict = {"k": k}
        self._anonymity_name = "KANONYMITY"
        self._print_messqge = f"KAnonymity(k={k})"


class LDiversityShannonEntropy(PrivacyModel):
    """ Configuration class for LDiversity"""

    def __init__(self, l, column_name):
        self._internal_dict = {"l": l, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_SHANNONENTROPY"
        self._print_messqge = f"KAnonymity(l={l}, column_name={column_name})"

