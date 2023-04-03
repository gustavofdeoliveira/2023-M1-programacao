# Para rodar o projeto

### Dentro da pasta Back-end rode o seguinte comando:

```
pip install flask prisma
```

### Ainda dentro da pasta Back-end

```
prisma migrate dev
```

### O terminal pedira para digitar algum nome para a migração:

#### ROCOMENDADO:

```
database
```
#### o último lib a ser instalada é Flask Cors para que a aplicação possa ser acessada de qualquer lugar:


```
python -m pip install flask-cors
``` 
### Após rodar os comandos com sucesso, basta inciar a aplicação, rode o comando no terminal:

```
python app.py
```

# Acesse o Front-end integrado ao Back-end no endereço:


```
http://127.0.0.1:5000
```

# Acessar o Godot com o projeto integrado ao Back-end:

1 - Instale o Godot versão 3.3.2 no site oficial deles: https://godotengine.org/download/
2 - Extrai o arquivo baixado
3 - Abra o Godot
4 - Clique em "Importar"
5 - Selecione a pasta "Semana-08\Robot"
6 - Aguarde o Godot importar o projeto
7 - Clique em "Executar" a cena Node2D.tscn
8 - Espere o Gofot carregar o projeto

<b>Nota: Após o Godot carregar o projeto, você pode manipular a posição do elemento por meio do Front-end</b>