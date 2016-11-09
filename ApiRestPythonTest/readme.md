# ApiRestPythonTest
ApiRestPythonTest


<h2>
API
</h2>
<b>FeiraLivreResource (api/api.py)</b>


<b> autenticação BasicAuthentication </b>
<br>
usuario : api
<br>
password : api12345
<br>

<i><b>GET (ALL / FILTERED)</b></i>
<br>
api/feiraslivre/
<br>
api/feiraslivre/?BAIRRO=[bairro]
<br>
api/feiraslivre/?DISTRITO=[distrito]
<br>
api/feiraslivre/?REGIAO5=[regiao5]
<br>
api/feiraslivre/?NOME_FEIRA=[nomefeira]
<br>
api/feiraslivre/?BAIRRO=[bairro]?DISTRITO=[distrito]?REGIAO5=[regiao5]?NOME_FEIRA=[nomefeira]

<i><b>GET (REGISTRO)</b></i>
<br>
api/feiraslivre/[registro]/

<i><b>POST</b></i>
<br>
api/feiraslivre/ (POST , Content-Type : Application/Json)
<br>
{
            "BAIRRO": "POMPEIA",
            "DISTRITO": "",
            "LOGRADOURO": "RUA XPTO",
            "NOME_FEIRA": "FEIRA XPTO",
            "NUMERO": "",
            "REFERENCIA": "IGREJA POMPEIA",
            "REGIAO5": "",
            "REGIAO8": "",
            "REGISTRO": "reg12345",
            "SUBPREFE": "",
}

<i><b>PUT</b></i>
<br>
api/feiraslivre/[registro]/ (PUT , Content-Type : Application/Json)
<br>
{ 
            "ID" : "123"
            "BAIRRO": "POMPEIA",
            "DISTRITO": "",
            "LOGRADOURO": "RUA XPTO",
            "NOME_FEIRA": "FEIRA XPTO",
            "NUMERO": "",
            "REFERENCIA": "IGREJA POMPEIA",
            "REGIAO5": "",
            "REGIAO8": "",
            "REGISTRO": "reg12345",
            "SUBPREFE": "",
}

<i><b>DELETE</b></i>
<br>
api/feiraslivre/[registro]/  (HTTP : DELETE )

<h2> Para rodar os testcases </h2> 
python manage.py test

<h2> Para Verificicar a cobertura de testes , rodar o coverage report </h2>
coverage run manage.py test
coverage report

<h2>Documentação da API REST</h2>
/swagger

<h2>LOGGING</h2>
api.debug.log


***********************************************
superuser
*************************************************
api@api.com.br
usuario : api
password : api12345
