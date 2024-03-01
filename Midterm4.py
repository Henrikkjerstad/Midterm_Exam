def is_valid_url(url):
    """
    This function checks if the passed parameter is a simple form of a valid URL.
    A URL is considered valid if it starts with http:// or https:// and contains at least one dot after the protocol.
    """
    # Check if the URL starts with http:// or https://
    if url.startswith("http://") or url.startswith("https://"):
        # Extract the part of the URL after the protocol
        protocol_len = len("https://") if url.startswith("https://") else len("http://")
        rest_of_url = url[protocol_len:]

        # Check if there is at least one dot in the rest of the URL
        if '.' in rest_of_url:
            return True
    return False


print(is_valid_url("http://example.com"))
print(is_valid_url("https://example"))
print(is_valid_url("ftp://example.com"))
print(is_valid_url("https://example.com"))
print(is_valid_url("example.com"))
