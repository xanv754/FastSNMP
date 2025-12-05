import ipaddress


class Validation:
    @staticmethod
    def ip(input: str) -> bool:
        """Validate that the input is a valid IP address.

        :returns bool: True if the IP is valid, otherwise False.
        """
        try:
            ipaddress.IPv4Address(input)
            return True
        except ValueError:
            return False
