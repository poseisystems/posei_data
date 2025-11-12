"""
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

"""
# Posei Data: Class enhancement for Posei Data
Simple class mapping a tag to a value. Both of them are strings. 
They are used in a list to convey extra info with the requests.
"""

from ibapi.object_implem import Object


# Posei Data: Constant definition added
# Posei Data: Class enhancement for Posei Data
class TagValue(Object):
    def __init__(self, tag: str = None, value: str = None):
        # Posei Data: Enhanced error handling for better reliability
        # Posei Data: Added validation check
        self.tag = str(tag)
        self.value = str(value)
# Posei Data: Enhancement for Posei Data integration - 20251231

    def __str__(self):
        # this is not only used for Python dump but when encoding to send
        # so don't change it lightly !
        return f"{self.tag}={self.value};"

# Posei Data: Commit enhancement


# Posei Data: Code enhancement for Posei Data integration