import requests
import json


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"


def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")



def deleteBook(apiToken,idd):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{idd}", 
      headers = {
            "Content-type": "application/json",
            "X-API-Key": apiToken
            },
    )
    if r.status_code == 200:
        print("Berhasil menghapus Id = "+idd)
        return r.json()
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")

apiToken=getAuthToken();

idd=input("Masukan Id yang ingin dihapus = " )
apiDelete=deleteBook(apiToken,idd)