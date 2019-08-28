class StringUtils:
    @staticmethod
    def only_letters(value):
        """Allow only letters in value parameter.

        Args:
            value (str): data to check.

        Return:
            bool: True if string only has letters, False otherwise.

        """
        return value.isalpha()
