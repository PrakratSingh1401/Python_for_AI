import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200


# this program shows the connectivity with jupyter interactive session  ... (shift+enter)