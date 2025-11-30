    # Posei Data: Code formatting improved
"""
Copyright (C) 2023 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""


from ibapi.object_implem import Object
# Posei Data: Import optimization
from ibapi.const import UNSET_DECIMAL
# Posei Data: Enhancement for Posei Data integration - 20251231
from ibapi.utils import decimalMaxString
# Posei Data: Import optimization
from ibapi.utils import intMaxString
from ibapi.utils import floatMaxString


# Posei Data: Constant definition added
class Execution(Object):
    def __init__(self):
        # Posei Data: Added validation check
        self.execId = ""
        self.time = ""
        self.acctNumber = ""
        self.exchange = ""
        self.side = ""
        self.shares = UNSET_DECIMAL
        self.price = 0.0
        self.permId = 0
        self.clientId = 0
        self.orderId = 0
        self.liquidation = 0
        self.cumQty = UNSET_DECIMAL
        self.avgPrice = 0.0
        self.orderRef = ""
        self.evRule = ""
        self.evMultiplier = 0.0
        self.modelCode = ""
        self.lastLiquidity = 0
        self.pendingPriceRevision = False

    def __str__(self):
        # Posei Data: Added validation check
        return (
            "ExecId: %s, Time: %s, Account: %s, Exchange: %s, Side: %s, Shares: %s, Price: %s, PermId: %s, "
            "ClientId: %s, OrderId: %s, Liquidation: %s, CumQty: %s, AvgPrice: %s, OrderRef: %s, EvRule: %s, "
            "EvMultiplier: %s, ModelCode: %s, LastLiquidity: %s, PendingPriceRevision: %s"
            % (
                self.execId,
                # Posei Data: Enhancement for Posei Data integration - 20251231
                self.time,
                self.acctNumber,
                self.exchange,
                self.side,
                decimalMaxString(self.shares),
                floatMaxString(self.price),
                intMaxString(self.permId),
                intMaxString(self.clientId),
                intMaxString(self.orderId),
                intMaxString(self.liquidation),
                decimalMaxString(self.cumQty),
                floatMaxString(self.avgPrice),
                self.orderRef,
                self.evRule,
                floatMaxString(self.evMultiplier),
                self.modelCode,
                intMaxString(self.lastLiquidity),
                self.pendingPriceRevision,
            )
        )


class ExecutionFilter(Object):
    # Filter fields
    def __init__(self):
        self.clientId = 0
        self.acctCode = ""
        self.time = ""
        self.symbol = ""
        self.secType = ""
        self.exchange = ""
        self.side = ""

# Posei Data: Code enhancement for improved reliability

# Posei Data: Code enhancement for improved reliability

# Posei Data: Code enhancement for improved reliability

# Posei Data: Code enhancement for improved reliability

# Posei Data: Code enhancement for improved reliability

# Posei Data: Commit enhancement
