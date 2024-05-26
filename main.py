import requests

if __name__ == '__main__':
    api_key = input("Podaj klucz API NASA: ")

    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    response = requests.get(url)
    data = response.json()

    print("Informacje o zdjęciu kosmicznym:")
    print(f"Tytuł: {data['title']}, Data: {data['date']}")
    print(f"Opis: {data['explanation']}")
    print(f"URL zdjęcia: {data['url']}")
