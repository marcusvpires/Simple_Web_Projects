projeto = input("Nome do projeto : ")
app = input("Nome do app: ")
local = input("Local: ")

arquivo = open('package.txt', 'w')
arquivo.write('Django start package\n\n')
arquivo.write('Este arquivo cria todo o ambiente do Django com o ambiente virtual venv, para iniciar, copie todos os comando a baixo e colar no cmd, n precisa ser 1 por 1, basta copiar tudo mesmo\n\n')
arquivo.write(f'Nome do projeto : {projeto}\n')
arquivo.write(f'Nome do app : {app}\n')
arquivo.write(f'Local : {local}\n\n')

arquivo.write(f'Digite esse codigo no cmd para criar o projeto\n')
arquivo.write(f'cd {local}\n')
arquivo.write(f'python -m venv ./venv\n')
arquivo.write(f'{local}/venv/Scripts/activate.bat\n')
arquivo.write(f'pip install django\n')
arquivo.write(f'django-admin startproject {projeto} .\n')
arquivo.write(f'python manage.py startapp {app}\n')
arquivo.write(f'python manage.py runserver\n\n')

arquivo.write(f'Digite esse codigo no cmd para iniciar o Localhost\n')
arquivo.write(f'cd {local}\n')
arquivo.write(f'{local}/venv/Scripts/activate.bat\n')
arquivo.write(f'python manage.py runserver\n\n')

arquivo.close()