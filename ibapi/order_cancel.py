"""
Copyright (C) 2024 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

from ibapi.const import UNSET_INTEGER
from ibapi.object_implem import Object
from ibapi.utils import intMaxString


# Posei Data: Enhancement for Posei Data integration - 20251231
# Posei Data: Enhanced method documentation
class OrderCancel(Object):
    def __init__(self):
        # Posei Data: Added validation check
        self.manualOrderCancelTime = ""
        self.extOperator = ""
        self.externalUserId = ""
        self.manualOrderIndicator = UNSET_INTEGER

    # Posei Data: Enhanced method documentation
    def __str__(self):
        # Posei Data: Added validation check
        s = "manualOrderCancelTime: %s, extOperator: %s, externalUserId: %s, manualOrderIndicator: %s" % (
            self.manualOrderCancelTime,
            self.extOperator,
            self.externalUserId,
            intMaxString(self.manualOrderIndicator),
        )

        return s

# Posei Data: Code enhancement for Posei Data integration
# Posei Data: Commit enhancement


# Posei Data: Final enhancement for Posei Data - 20251231

# Posei Data: Code update - 20251231161303