
**************
Django inicial
**************

Primeiros Passos
================


Verifique se o Python está instalado e sua versão
-------------------------------------------------

Para ter certeza que tenho Python executo o python pedindo a versão.

.. code-block:: bash

    # no seu shell execute ... o comando abaixo

    $>python -V

... o resultado esperado é  a versão do Python instalada, algo como "Python 3.X.X", onde X é uma variação da versão 3.

O meu computador o resultado é...

    Python 3.7.4


Instalando o Django
-------------------

Instale o Django ...   depois de ter seu Python3 instalado.

.. code-block:: bash

    # no seu shell execute ... o comando abaixo

    $>pip install django


Valide se Django OK

Validando que o Django está instalado e verificamos sua versao ..

.. code-block:: bash

    # no seu shell execute ... o comando abaixo

    $>django-admin --version

A saída esperada é algo como **2.x.x** onde x é uma variação da versão 2.

na minha máquina a saída do comando foi ...

    2.2.6


Inicie um projeto Django
========================

A sintaxe do comando é `django-admin startproject <nome do projeto>`

.. code-block:: bash

    # no seu shell execute ... o comando abaixo

    $>django-admin startproject prjdj

O Django criar um diretório com o nome do projeto (ex.: "prjdj")
vou acessar o diretório do meu projeto Django que acabei de criar com o nome de "prjdj"

.. code-block:: bash

    $>cd /Volumes/p10G/prj/prjdj


Rode o seu projeto django
-------------------------

comando `python manage.py runserver`


.. code-block:: bash

    # no seu shell execute ... o comando abaixo

    $>python manage.py  runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.

    October 09, 2019 - 19:20:09
    Django version 2.2.6, using settings 'prjdj.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    [09/Oct/2019 19:20:18] "GET / HTTP/1.1" 200 16348
    [09/Oct/2019 19:20:18] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
    [09/Oct/2019 19:20:19] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
    [09/Oct/2019 19:20:19] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
    [09/Oct/2019 19:20:19] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692

Com o seu navegador Web acesse o endereço  *127.0.0.1:8000*

ex.: http://127.0.0.1:8000  (o mesmo que http://localhost:8000)

No seu navegador você deverá ver uma página como a abaixo.

.. image:: docs/imgs/django_tela_inicial.png
    :align: center


Entenda a saída do comando `runserver` ...
------------------------------------------

O servidor de desenvolvimento do Django está rodando e você pode editar seu código sem desligá-lo.

Desde que não tenha erros, ele não deve parar ( ... boa sorte!)

    >Watching for file changes with StatReloader


Ao executar seu projeto, o Django identificou que existem migrações para serem executadas no banco de dados ...

    You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.

Essa migrações são referentes as aplicações Django "enbutidas" no Django. Uma delas é o **sistema de gestão de usuários**


Seguindo a sugestão do Django, vamos rodar essas migrações para que nosso banco seja criado...


Criando o Banco de dados
------------------------

comando *`python manage.py migrate`*

    Atenção: se o banco de dados for o POSTGRESQL você deve ANTES criar o banco de dados e depois rodar as migrations - neste caso o Django somente criar as tabelas.


.. code-block:: bash

    # no seu shell execute ... o comando abaixo

    >$python manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying sessions.0001_initial... OK

Com o banco criado podemos adicionar nosso prieiro usuário, o SUPERUSER do sistema...


Criando o SUPERUSER
-------------------

comando `python manage.py  createsuperuser`

.. code-block:: bash

    # no seu shell ...

    $>python manage.py  createsueruser

    #... a saída esperada está abaixo.
    Unknown command: 'createsueruser'. Did you mean createsuperuser?
    Type 'manage.py help' for usage.
    (prjdj) 20191009.Wed16:39:55cadu>/Volumes/p10G/prj/prjdj>
    cadu.[489] (master *=)$python manage.py createsuperuser
    Username (leave blank to use 'menunome'):mybeautifulusername
    Email address: c@mail.com
    Password:
    Password (again):
    # as linhas abaixo são mostradas caso o Django entende que o password fornecido seja fraco...
    # basta dar um "y" (yes) para confirmar a criação do nosso user.
    This password is too short. It must contain at least 8 characters.
    This password is too common.
    This password is entirely numeric.
    Bypass password validation and create user anyway? [y/N]: y




Adicionando uma "aplicação Django" ao projeto.
==============================================

comando `python manage.py startapp <nome da minha app>`

    Não utilize espaços, e é uma boa prática usar nomes em caixa baixa (letras minússculas)

.. code-block:: bash

    # no seu bash ... minha aplicação se chama "app1"
    $>python manage.py startapp app1

Além de criar a aplicação, para que o django reconheça como parte do projeto eu preciso adicionar minha aplicação no `settings.py` dentro da variávels `INSTALLED_APPS`.


.. code-block:: python

    # arquivo settings.py

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app1',  # <<<<  MINHA NOVA APP.
    ]


Após a criação da minha APP a árvode de diretórios deve estar deste modo::


    prjdj
        ├── README.rst
        ├── app1
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── migrations
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── tests.py
        │   └── views.py
        ├── db.sqlite3
        ├── docs
        │   └── imgs
        │       └── django_tela_inicial.png
        ├── manage.py
        └── prjdj
            ├── __init__.py
            ├── __pycache__
            │   ├── __init__.cpython-37.pyc
            │   ├── settings.cpython-37.pyc
            │   ├── urls.cpython-37.pyc
            │   └── wsgi.cpython-37.pyc
            ├── settings.py
            ├── urls.py
            └── wsgi.py


Adicionando conteúdo ao projeto
-------------------------------

.. code-block:: Python3

    # Conteúdo do arquivo app1/models.py

    from django.db import models

    TIPO = (
        (1, 'despesa'),
        (2, 'receita')
    )


    class Emissor(models.Model):
        '''
        Modelo representa o Emissor da Nota Fiscal
        O Emissor é uma empresa que emite a nota fiscal para que eu a pague, ou, minha empresa emite uma nota fiscal.
        '''
        cpnj = models.CharField('CNPJ', max_length=50, primary_key=True)
        nome = models.CharField('nome', max_length=50)

        def __str__(self):

            return str(self.cpnj) 


    class Lancamento(models.Model):

        num_nota_fiscal = models.CharField('numero da nota fiscal', max_length=50, blank=True, null=True)
        receita_despesa = models.PositiveSmallIntegerField('receita ou despesa', choices=TIPO)  # True = Receita

        emissor = models.ForeignKey(Emissor, blank=True, null=True, on_delete=models.CASCADE)

        valor_nota = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
        desconto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
        valor_total = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)

        class Meta:
            verbose_name = 'Lançamento'
            verbose_name_plural = 'Lançamentos'

        def __str__(self):

            return str(self.pk)

O model, é a representação Python do nosso tipo de conteúdo

Para criar as tabelas no banco de dados, referentes aos modelos que acabamos de criar.

#. Executar o `makemigrations` para criar o código Python que irá gerar as tabelas
#. Executar o `miagrate` para que de fato as alterações sejam aplicadas ao banco de dados . 

... então `makemigrations`

.. code-block:: bash

    # no seu shell ...

    $>python manage.py  makemigrations

    # ... saida esperada.
    Migrations for 'app1':
      app1/migrations/0001_initial.py
        - Create model Emissor
        - Create model Lancamento

... e após o makemigrations, executamos o `migrate`

.. code-block:: bash

    # no seu shell ...

    $>python manage.py  migrate

    # ... saida esperada.
    Operations to perform:
      Apply all migrations: admin, app1, auth, contenttypes, sessions
    Running migrations:
      Applying app1.0001_initial... OK


Colocando seu modelo no Admin do Django
---------------------------------------

Precisamos "registrar" nossos modelos no admin do Django 


.. code-block:: Python3

    # conteúdo do app1/admin.py

    from django.contrib import admin
    from app1.models import Emissor, Lancamento


    class EmissorAdmin(admin.ModelAdmin):
        pass
    admin.site.register(Emissor, EmissorAdmin)


    class LancamentoAdmin(admin.ModelAdmin):
        pass
    admin.site.register(Lancamento, LancamentoAdmin)


ver em https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#modeladmin-objects



---------------


Gerar modelo do banco (ERD) como Django-Extensions
    $>python manage.py  graph_models -a -g -o app1

git
--------


git init
git remote add origin git@github.com:cadu-leite/prjdj.git
git remote add origin git@github.com:cadu-leite/prjdj.git
git add .
git commit -m "first commit"
git push -u origin master