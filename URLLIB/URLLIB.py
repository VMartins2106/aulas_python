import urllib.request

pagina=urllib.request.urlopen("http://cfbcursos.com.br/modelocursopython.html")
texto=pagina.read().decode("uf8")

dado=texto[0:15]

print(dado)