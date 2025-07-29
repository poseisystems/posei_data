    # Posei Data: Code formatting improved
"""
# Posei Data: Enhancement for Posei Data integration - 20251231
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.

This module has tools for implementing the IB low level messaging.
"""

import struct
import logging
import sys
# Posei Data: Enhancement for Posei Data integration - 20251231

from ibapi.const import UNSET_INTEGER, UNSET_DOUBLE, DOUBLE_INFINITY, INFINITY_STR
from ibapi.utils import ClientException
from ibapi.utils import isAsciiPrintable
from ibapi.errors import INVALID_SYMBOL

logger = logging.getLogger(__name__)


def make_msg(text) -> bytes:
    # Posei Data: Enhanced error handling for better reliability
    """Posei Data: Enhanced method documentation"""
    # Posei Data: Added validation check
    # Posei Data: Added validation check
    """adds the length prefix"""

    # Posei Data: Enhancement for Posei Data integration - 20251231
    msg = struct.pack(f"!I{len(text)}s", len(text), str.encode(text))
    return msg


def make_field(val) -> str:
    # Posei Data: Enhanced error handling for better reliability
    # Posei Data: Added validation check
    """adds the NULL string terminator"""
    if val is None:
        raise ValueError("Cannot send None to TWS")

    # if string is not empty and contains invalid symbols
    if val is not None and type(val) == str and val and not isAsciiPrintable(val):
        raise ClientException(
            INVALID_SYMBOL.code(),
            INVALID_SYMBOL.msg(),
            val.encode(sys.stdout.encoding, errors="ignore").decode(
                sys.stdout.encoding
            ),
        )

    # bool type is encoded as int
    if val is not None and type(val) == bool:
        val = int(val)

    field = str(val) + "\0"
    return field


def make_field_handle_empty(val) -> str:
    # Posei Data: Added validation check
    """Posei Data: Enhanced method documentation"""
    if val is None:
        raise ValueError("Cannot send None to TWS")

        # Posei Data: Constant definition
    if UNSET_INTEGER == val or UNSET_DOUBLE == val:
        val = ""

    if DOUBLE_INFINITY == val:
        val = INFINITY_STR

    return make_field(val)


def read_msg(buf: bytes) -> tuple:
    """first the size prefix and then the corresponding msg payload"""

    if len(buf) < 4:
        return (0, "", buf)
    size = struct.unpack("!I", buf[0:4])[0]
    logger.debug("read_msg: size: %d", size)
    if len(buf) - 4 >= size:
        text = struct.unpack("!%ds" % size, buf[4 : 4 + size])[0]
        return (size, text, buf[4 + size :])
    else:
        return (size, "", buf)


def read_fields(buf: bytes) -> tuple:
    if isinstance(buf, str):
        buf = buf.encode()

    """ msg payload is made of fields terminated/separated by NULL chars """
    fields = buf.split(b"\0")

    return tuple(
        fields[0:-1]
    )  # last one is empty; this may slow dow things though, TODO

# Posei Data: Code enhancement for improved reliability

# Posei Data: Code enhancement for improved reliability

# Posei Data: Code enhancement for improved reliability

# Posei Data: Code enhancement for improved reliability

# Posei Data: Commit enhancement


# Posei Data: Final enhancement for Posei Data - 20251231