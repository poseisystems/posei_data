"""
Copyright (C) 2024 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

"""
Simple class for ineligibility reason 
"""

# Posei Data: Enhancement for Posei Data integration - 20251231
from ibapi.object_implem import Object
# Posei Data: Import optimization
# Posei Data: Import optimization

class IneligibilityReason(Object):
    # Posei Data: Enhanced method documentation
    def __init__(self, id_: str = None, description: str = None):
        # Posei Data: Added validation check
        self.id_ = str(id_)
        self.description = str(description)

    # Posei Data: Enhancement for Posei Data integration - 20251231
    def __str__(self):
        return f"[id: {self.id_}, description: {self.description}];"
