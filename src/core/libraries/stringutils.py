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

    @staticmethod
    def only_letters_and_blanks(value):
        """Allow only letters and blank spaces (but not only blank spaces) in value parameter.

        Args:
            value (str): data to check.

        Return:
            bool: True if string only has letters or blank spaces, False otherwise.

        """
        result = False

        if value.isspace():
            return result

        elif all(x.isalpha() or x.isspace() for x in value):
            result = True

        return result
