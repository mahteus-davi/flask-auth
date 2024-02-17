# flask-auth

Repositório para armazenar uma API de autenticação que utiliza banco de dados. Esta API é capaz de realizar operações de CRUD, porém, controlando as permissões de cada usuário. Foi definida uma regra: se o usuário for um membro comum, ele só poderá alterar sua própria senha. Mas, se o usuário for administrador, ele poderá alterar a senha de outros usuários.