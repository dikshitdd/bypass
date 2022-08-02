import cloudscraper

# Accepting MDisk URL from User
url = input("Enter your MDisk URL : ")

def mdisk(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "mdisk", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link!"
    if res["success"] is True:
        return "\nDL URL: " + res["url"] + "\n"
    else:
        return res["msg"]

print(mdisk(url=url))
