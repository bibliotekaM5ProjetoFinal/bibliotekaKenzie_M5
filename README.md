# bibliotekaKenzie_M5
<h1>BiblioteKaKenzie</h1>

<h3><strong>Proposta:</strong></h3>
<p>Construir uma aplicação que faz a gestão de uma biblioteca.</p>
<hr noshade />

<h2>[201] O sistema deve permitir o cadastro de usuários. </h2>
<h3>POST - /User</h3>

<strong>Essa rota não necessita autenticação bearer token. Campos de envio para request:</strong>

<ul>
    <li><strong>username: </strong>Entrada obrigatória do tipo string e máximo 100 chars.</li>
    <li><strong>first_name: </strong>Entrada obrigatória do tipo string email e máximo 100 chars.</li>
    <li><strong>last_name: </strong>Entrada obrigatória do tipo string e máximo 100 chars.</li>
    <li><strong>email: </strong>Entrada obrigatória do tipo string e máximo 100 chars.</li>
    <li><strong>password: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>phone: </strong>Entrada obrigatória do tipo string e máximo 100 chars.</li>
    <li><strong>is_superuser: </strong>Entrada opcional do tipo boolean com padrão falso.</li>
</ul>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:18px">201</strong> para criação realizada com sucesso:</p>
<pre>
{
    "id": "9521d750-a277-4237-bad2-dc2d6d988151",
    "email": "marcelohm@gmail.com",
    "name": "Marcelo Henrique Marques",
    "isActive": true,
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">400</strong> para request incorreto:</p>
<pre>
{
    "message": yup.error.errors
}
</pre>
<p>Retorno esperado com status code <strong style="color:red;font-size:18px">409</strong> para email já existente:</p>
<pre>
{
    "message": "Email already registered to another author."
}
</pre>
<hr noshade />
