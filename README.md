# Desafio Polícia Civil CE 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)


O desafio é baseado em uma diagrama EER, onde deveriamos fazer um relacionamento da classe 'objeto' após instanciar um armamento ou uma munição.
- Obs: Eu fiz utilização do arquivo .env, mas você pode ficar a vontade para fazer a sua configuração no settings. 

<br>

1. Clone o projeto em sua máquina.
```bash
   git clone <url do repositorio>
```
2. Crie a virtualenv com o comando.
```bash
   python3 -m venv venv
   source/bin/activate
```

3.Instale os pacotes requeridos.
```bash
   pip install -r requirements.txt
```
4. Criar banco de dados (Eu fiz a utilizando do postgresql, mas você pode ficar a vontade para usar o banco que desejar).

```bash
  python manage.py migrate
```
5. Start o servidor

```bash
  python manage.py runserver
```
