# BiblioteKaKenzie M5

<h3><strong>Proposta:</strong></h3>
<p>Construir uma aplicação que faz a gestão de uma biblioteca.</p>

<hr noshade />
<h2>Rotas de Usuários:</h2>
<hr noshade />

<h2>[201] O sistema deve permitir o cadastro de usuários. </h2>
<h3>POST - /api/users/</h3>

<strong>Essa rota não necessita autenticação bearer token. Campos de envio para request:</strong>

<ul>
    <li><strong>username: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>first_name: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>last_name: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>email: </strong>Entrada obrigatória do tipo string email e máximo 127 chars.</li>
    <li><strong>password: </strong>Entrada obrigatória do tipo string e máximo 20 chars.</li>
    <li><strong>phone: </strong>Entrada obrigatória do tipo string e máximo 100 chars.</li>
    <li><strong>can_loan: </strong>Entrada opcional do tipo boolean com padrão falso.</li>
    <li><strong>is_superuser: </strong>Entrada obrigatória do tipo boolean com padrão falso.</li>
</ul>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">201</strong> para criação realizada com sucesso:</p>
<pre>
{
    "id": 1,
    "username": "daniel_buster_comum",
    "email": "daniel_common@mail.com",
    "first_name": "daniel",
    "last_name": "Comum",
    "phone": "1999-09-09",
    "can_loan": false,
    "is_superuser": false
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">400</strong> para request incorreto:</p>
<pre>
{
	"username": [
		"This field may not be blank."
	],
	"password": [
		"This field may not be blank."
	],
	"email": [
		"This field may not be blank."
	],
	"first_name": [
		"This field may not be blank."
	],
	"last_name": [
		"This field may not be blank."
	],
	"is_superuser": [
		"Must be a valid boolean."
	],
	"can_loan": [
		"Must be a valid boolean."
	],
	"phone": [
		"This field may not be blank."
	]
}

</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">409</strong> para email já existente:</p>
<pre>
{
	"username": [
		"user with this username already exists."
	],
	"email": [
		"Email Alredy Registered"
	]
}
</pre>
<hr noshade />
<!-- =========================================================================================================================================================================: -->

<h2>[200] O sistema deve permitir o login de usuários. </h2>
<h3>POST - /api/users/login/</h3>

<strong>Essa rota não necessita autenticação bearer token. Campos de envio para request:</strong>

<ul>
    <li><strong>username: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>password: </strong>Entrada obrigatória do tipo string e máximo 20 chars.</li>
</ul>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para login realizado com sucesso:</p>
<pre>
{
	"refresh":
     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3ODczMTI5MSwiaWF0IjoxN
    jc4MTI2NDkxLCJqdGkiOiIyOWY5OWQ1ZTAxNWY0ZjMyOTVhYjZkN2FhYTI4YzM1OSIsInVzZXJfaWQiOjF9.apwWAwGCQr-yWTWeldPubdLEW13DKNFUjPdJcRevXrU",
	"access": 
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4NzMxMjkxLCJpYXQiOjE2NzgxMjY0OTEsImp
    0aSI6ImQyZjRmNzUyNTJjZjQzODE4YjViMjRiMjRlZTAwYTZlIiwidXNlcl9pZCI6MX0.tQV9c1OiuFGfTk7Tg1WNracmUSfKhY2Rw70CwfoOwYc"
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">400</strong> para campos em branco para essa rota:</p>
<pre>
{
	"username": [
		"This field may not be blank."
	],
	"password": [
		"This field may not be blank."
	]
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">401</strong> para usuário sem permissão de uso dessa rota:</p>
<pre>
{
	"detail": "No active account found with the given credentials"
}
</pre>

<hr noshade />
<!-- =========================================================================================================================================================================: -->

<h2>[200] O sistema deve permitir a listagem de usuários. </h2>
<h3>GET - /api/users/</h3>

<strong>Essa rota necessita autenticação bearer token. Apenas usários Admim podem acessar essa rota. Não há Campos de envio para request:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">201</strong> para listagem realizada com sucesso:</p>
<pre>
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"username": "daniel_comum",
			"email": "daniel_common@mail.com",
			"first_name": "daniel",
			"last_name": "Comum",
			"is_superuser": false,
			"can_loan": false,
			"phone": "1999"
		},
		{
			"id": 2,
			"username": "daniel_admin",
			"email": "daniel_admin@mail.com",
			"first_name": "daniel",
			"last_name": "admin",
			"is_superuser": true,
			"can_loan": true,
			"phone": "1999"
		}
	]
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">403</strong> para usuário sem permissão de uso dessa rota:</p>
<pre>
{
	"detail": "You do not have permission to perform this action."
}
</pre>
<hr noshade />

<!-- =========================================================================================================================================================================: -->

<h2>[200] O sistema deve permitir a listagem do Profile do usuário. </h2>
<h3>GET - /api/users/user_id</h3>

<strong>Essa rota necessita autenticação bearer token. Usuários não Admim podem acessar apenas o seu próprio Profile. Não há Campos de envio para request:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para listagem realizada com sucesso:</p>
<pre>
{
	"id": 6,
	"username": "Lucas_Book",
	"email": "lucas@biblioteka.com",
	"first_name": "Lu",
	"last_name": "Cas",
	"is_superuser": true,
	"can_loan": true,
	"phone": "(19)1111-1111",
	"following": [
		{
			"title": "Uma senhora enrrascada",
			"since": "2023-03-08"
		}
	]
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">403</strong> para usuário sem permissão de uso dessa rota:</p>
<pre>
{
	"detail": "You do not have permission to perform this action."
}
</pre>
<hr noshade />
<!-- =========================================================================================================================================================================: -->

<h2>Rotas de Books:</h2>
<hr noshade />

<h2>[201] O sistema deve permitir Cadastro de novos livros.</h2>
<h3>POST - /api/books/</h3>

<strong>Essa rota necessita autenticação bearer token. Usuários não Admim podem acessar apenas o seu próprio Profile. Não há Campos de envio para request:</strong>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">200</strong> para listagem realizada com sucesso:</p>
<pre>
{
	"id": 6,
	"username": "Lucas_Book",
	"email": "lucas@biblioteka.com",
	"first_name": "Lu",
	"last_name": "Cas",
	"is_superuser": true,
	"can_loan": true,
	"phone": "(19)1111-1111",
	"following": [
		{
			"title": "Uma senhora enrrascada",
			"since": "2023-03-08"
		}
	]
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">403</strong> para usuário sem permissão de uso dessa rota:</p>
<pre>
{
	"detail": "You do not have permission to perform this action."
}
</pre>
<hr noshade />
<!-- =========================================================================================================================================================================: -->