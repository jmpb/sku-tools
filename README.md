# sku-tools

Useful tools for working with product names and model numbers.

---------
find_sku
An algorithm to return the model number from a string.

  The algorithm fetches the model number based on the criteria that the model number is all uppercase, and the string argument is all   lower case (beginning capital letters are allowed because - Grammar).
  The model number may include any characters in the regex pattern but must be in sequence within the string.

  Suggested improvements:

    1. Split the return value in to a list of possible Skus - I may write a separate function for this.
