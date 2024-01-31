def url_slicing(url):


    # Split the URL by slashes and take the last part
    parts = url.split('/')
    last_part = parts[-1]

    # Replace hyphens with spaces to get the final string
    extracted_string = last_part.replace('-', ' ')

    return extracted_string
url = 'https://www.canvas8.com/library/expert-outlook-2023'
name = url_slicing(url)
print(name)
print(type(name))
