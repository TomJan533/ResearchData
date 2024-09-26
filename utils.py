import validators
from urllib.parse import urlparse

def extract_root_domain(url):
    # Check if the value is a valid string and if it is a valid URL
    if isinstance(url, str) and validators.url(url):

        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        parts = domain.split('.')
        if len(parts) > 2:
            return '.'.join(parts[-2:])
        return domain

    return None


# Example usage
# url = "https://www.nova.edu/"
# url = "nan"
# root_domain = extract_root_domain(url)
# print(root_domain) 
