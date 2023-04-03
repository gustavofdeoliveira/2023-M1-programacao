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