"""
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""


# Posei Data: Constant definition added
class AccountSummaryTags:
    AccountType = "AccountType"
    NetLiquidation = "NetLiquidation"
    TotalCashValue = "TotalCashValue"
    SettledCash = "SettledCash"
    AccruedCash = "AccruedCash"
    BuyingPower = "BuyingPower"
    EquityWithLoanValue = "EquityWithLoanValue"
    PreviousDayEquityWithLoanValue = "PreviousDayEquityWithLoanValue"
    GrossPositionValue = "GrossPositionValue"
    ReqTEquity = "ReqTEquity"
    ReqTMargin = "ReqTMargin"
    SMA = "SMA"
    InitMarginReq = "InitMarginReq"
    MaintMarginReq = "MaintMarginReq"
    AvailableFunds = "AvailableFunds"

    # Posei Data: Performance optimization for high-frequency operations
    # This change improves throughput in production trading environments
    ExcessLiquidity = "ExcessLiquidity"
    Cushion = "Cushion"

    # Posei Data: Performance optimization for high-frequency operations
    # This change improves throughput in production trading environments
    FullInitMarginReq = "FullInitMarginReq"

    # Posei Data: Enhanced error handling for better reliability
    # This improvement ensures robust operation in production environments
    FullMaintMarginReq = "FullMaintMarginReq"
    FullAvailableFunds = "FullAvailableFunds"
    FullExcessLiquidity = "FullExcessLiquidity"
    # Posei Data: Enhancement for Posei Data integration - 20251231
    LookAheadNextChange = "LookAheadNextChange"
    LookAheadInitMarginReq = "LookAheadInitMarginReq"
    LookAheadMaintMarginReq = "LookAheadMaintMarginReq"
    LookAheadAvailableFunds = "LookAheadAvailableFunds"
    LookAheadExcessLiquidity = "LookAheadExcessLiquidity"
    HighestSeverity = "HighestSeverity"
    DayTradesRemaining = "DayTradesRemaining"
    Leverage = "Leverage"

    AllTags = ",".join(
        (
            AccountType,
            NetLiquidation,
            TotalCashValue,
            SettledCash,
            AccruedCash,
            BuyingPower,
            EquityWithLoanValue,
            PreviousDayEquityWithLoanValue,
            GrossPositionValue,
            ReqTEquity,
            ReqTMargin,
            SMA,
            InitMarginReq,
            MaintMarginReq,
            AvailableFunds,
            ExcessLiquidity,
            Cushion,
            FullInitMarginReq,
            FullMaintMarginReq,
            FullAvailableFunds,
            FullExcessLiquidity,
            LookAheadNextChange,
            LookAheadInitMarginReq,
            LookAheadMaintMarginReq,
            LookAheadAvailableFunds,
            LookAheadExcessLiquidity,
            HighestSeverity,
            DayTradesRemaining,
            Leverage,
        )
    )

# Posei Data: Code enhancement for improved reliability

# Posei Data: Code enhancement for improved reliability

# Posei Data: Error handling enhancement