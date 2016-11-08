# ApiRestPythonTest
ApiRestPythonTest


<h2>
API
</h2>
<b>FeiraLivreResource (api/api.py)</b>
<i>GET (ALL / FILTERED)</i>
<br>
api/feiraslivre
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

<i>GET (REGISTRO)</i>
api/feiraslivre/123

<i>POST</i>
api/feiraslivre/ (POST , Content-Type : Application/Json)
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

<i>PUT</i>
api/feiraslivre/ (POST , Content-Type : Application/Json)
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

<i>DELETE</i>
api/feiraslivre/123  (HTTP : DELETE )

<h2> Para rodar os testcases </h2> 
python -m unittest -v

<h2> Para Verificicar a cobertura de testes , rodar o coverage report </h2>
coverage run -m
coverage report

<h2>Documentação da API REST</h2>
/swagger


***********************************************
superuser
*************************************************
api@api.com.br
usuario : api
password : api12345
