import pickle

def save_token(filename, token):
    with open(filename, "wb") as file:
        pickle.dump(token, file)

def get_token(filename = 'token.dat'):
    with open(filename, "rb") as file:
        return pickle.load(file)

if __name__ == "__main__":
    print("API TOKEN MANAGER")
    path = "token.dat"
    token = input("Paste your token code here: ")
    save_token(path, token)

    print("Done")
