# Para rodar o projeto

### Dentro da pasta ENV rode o seguinte comando:
    pip install flask prisma

### Ainda dentro da pasta ENV
    prisma migrate dev

### O terminal pedira para digitar algum nome para a migração:
<br>

#### ROCOMENDADO:
    database

### Após rodar os comandos com sucesso, basta inciar a aplicação, rode o comando  no terminal:
    python app.py

# Acessar rotas e formato:

### Para acessar a rota de GET, apenas de uma coordenada:

    http://127.0.0.1:5000/coordinate/listOne

#### Deve se passar o JSON da seguinte maneira:
    {
		"id": 2
	}

<br>

### Para acessar a rota de GET, pegando todas as coordenadas:

    http://127.0.0.1:5000/coordinate/listAll

<br>

### Para acessar a rota de POST, pegando todas as coordenadas:

    http://127.0.0.1:5000/coordinate/create

#### Deve se passar o JSON da seguinte maneira:
    {	
		"coordinateX": 1.0,
		"coordinateY": 1.0,
		"coordinateZ": 1.0,
        "coordinateR": 1.0
	}

<br>

### Para acessar a rota de PUT, pegando todas as coordenadas:

    http://127.0.0.1:5000/coordinate/update

#### Deve se passar o JSON da seguinte maneira:
    {	
        "id": 2,
		"coordinateX": 2.0,
		"coordinateY": 2.0,
		"coordinateZ": 2.0,
        "coordinateR": 2.0
	}

### Para acessar a rota de DELETE, apenas de uma coordenada:

    http://127.0.0.1:5000/coordinate/delete

#### Deve se passar o JSON da seguinte maneira:
    {
		"id": 2
	}

<br>