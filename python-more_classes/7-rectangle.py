def __str__(self):
    """Return a string representation using print_symbol."""
    if self.__width == 0 or self.__height == 0:
        return ""
    symbol = str(self.print_symbol)
    lines = [
        symbol * self.__width
        for _ in range(self.__height)
    ]
    return "\n".join(lines)
