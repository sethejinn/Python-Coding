import pyshorteners

def acortar_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

if __name__ == "__main__":
    url_larga = input("Introduce URL: ")
    url_corta = acortar_url(url_larga)
    print(f"URL acortada: {url_corta}")
