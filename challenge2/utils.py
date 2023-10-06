def convert_hex_string_to_address(hex_str: str) -> str:
    """
    Converts a hexadecimal string to an Ethereum address.

    Args:
      hex_str: A hexadecimal string.

    Returns:
      A string representing the Ethereum address.
    """
    return f'0x{hex_str[-40:].rjust(40, "0")}'
