import wget

def wget_pic(imagelink):
    filename = imagelink.split('/')[-1]
    wget.download(imagelink, '/home/student/static/' + filename)

if __name__ == "__main__":
    wget_pic('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png')

