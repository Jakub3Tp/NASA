import requests

if __name__ == '__main__':
    api_key = input("Podaj klucz API NASA: ")

    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        print("Informacje o zdjęciu kosmicznym:")
        print(f"Tytuł: {data['title']}")
        print(f"Data: {data['date']}")
        print(f"Opis: {data['explanation']}")
        print(f"URL zdjęcia: {data['url']}")
    except requests.exceptions.HTTPError as http_err:
        print(f"Błąd HTTP: {http_err}")
    except Exception as err:
        print(f"Nieoczekiwany błąd: {err}")

