import requests
import json


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"



def getBookList(idd):
    r = requests.get(
        f"{APIHOST}/api/v1/books/{idd}", 

    )
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")


def getBook():
    r = requests.get(
        f"{APIHOST}/api/v1/books", 
    

    )
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")



print("ini list buku")
books=getBook()
print(books)
idd=input("Masukan Id yang ingin dilihat= " )

books=getBookList(idd)
print(books)