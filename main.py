import requests

print("welcome to the status code checker thingy 2000")
print("here is how googles status currently is.")
print("------------------------------------------------------------------------")

got = requests.get("https://google.com")
print(got.status_code)
if got.status_code == 200:
    print("Request was successful!")
elif got.status_code == 404:
    print("Page not found!")
elif got.status_code == 500:
    print("Server error!")
else:
    print("An unexpected error occurred!")

print("------------------------------------------------------------------------")
url = input("If you want to check another url enter in the url you want to check: ")
while True:
    try:
        got = requests.get(url)
        print(got.status_code)
        if got.status_code == 200:
            print("Request was successful!")
        elif got.status_code == 404:
            print("Page not found!")
        elif got.status_code == 500:
            print("Server error!")
        else:
            print("An unexpected error occurred!")
        break
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except requests.exceptions.InvalidURL:
        print("Invalid URL format. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
