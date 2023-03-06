# BiblioteKaKenzie M5

<h1>BiblioteKaKenzie</h1>

<h3><strong>Proposta:</strong></h3>
<p>Construir uma aplicação que faz a gestão de uma biblioteca.</p>
<hr noshade />

<h2>[201] O sistema deve permitir o cadastro de usuários. </h2>
<h3>POST - /User</h3>

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
