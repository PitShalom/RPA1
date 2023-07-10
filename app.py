from flask import Flask


app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return '''
    <html>
<head>
  <title>Formulário de Informações Pessoais</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

</head>
<body>
  <h1>Formulário de Informações Pessoais</h1>
  <a class="button" onclick="iniciarRobo()">Iniciar ROBÔ</a>
  

  <form action="processar_formulario.php" method="POST">
    <h2>Informações de Contato</h2>
    <label for="nome">Nome completo:</label>
    <input type="text" id="nome" name="nome" required>
    <br>

    <label for="data_nascimento">Data de nascimento:</label>
    <input type="date" id="data_nascimento" name="data_nascimento" required>
    <br>

    <label for="genero">Gênero:</label>
    <select id="genero" name="genero">
      <option value="masculino">Masculino</option>
      <option value="feminino">Feminino</option>
      <option value="outro">Outrossssssss</option>
    </select>
    <br>

    <label for="endereco">Endereço completo:</label>
    <textarea id="endereco" name="endereco" required></textarea>
    <br>

    <label  for="telefone" class="line typing">Número de telefone:</label>
    <input type="tel" id="telefone" name="telefone" required>
    <br>

    <label for="email">Endereço de e-mail:</label>
    <input type="email" id="email" name="email" required>
    <br>

    <h2>Informações de Emprego</h2>
    <label for="empresa">Nome da empresa:</label>
    <input type="text" id="empresa" name="empresa" required>
    <br>

    <label for="cargo">Cargo:</label>
    <input type="text" id="cargo" name="cargo" required>
    <br>

    <label for="endereco_trabalho">Endereço do local de trabalho:</label>
    <textarea id="endereco_trabalho" name="endereco_trabalho" required></textarea>
    <br>

    <label for="telefone_trabalho">Número de telefone do trabalho:</label>
    <input type="tel" id="telefone_trabalho" name="telefone_trabalho" required>
    <br>

    <label for="email_trabalho">E-mail do trabalho:</label>
    <input type="email" id="email_trabalho" name="email_trabalho" required>
    <br>

    <h2>Informações de Educação</h2>
    <label for="nivel_educacao">Nível de educação alcançado:</label>
    <select id="nivel_educacao" name="nivel_educacao" required>
    <option value="">Selecione o nível de educação</option>
    <option value="ensino_medio">Ensino Médio</option>
    <option value="graduacao">Graduação</option>
    <option value="pos_graduacao">Pós-Graduação</option>
    <option value="mestrado">Mestrado</option>
    <option value="doutorado">Doutorado</option>
    <option value="outro">Outro</option>
    </select>
    <br>


    <label for="instituicao_educacional">Nome da instituição educacional:</label>
    <input type="text" id="instituicao_educacional" name="instituicao_educacional" required>
    <br>

    <label for="curso">Curso de formação/graduação:</label>
    <input type="text" id="curso" name="curso" required>
    <br>

    <label for="ano_conclusao">Ano de conclusão:</label>
    <input type="number" id="ano_conclusao" required>
    
     <script>
    function iniciarRobo() {
      fetch('/iniciar-robo', { method: 'POST' });  // Chama a rota '/iniciar-robo' via POST
    }
    </script>
   
</body>
</html>
    '''

@app.route('/iniciar-robo', methods=['POST'])
def iniciar_robo():
    # Coloque aqui o código para iniciar o seu robô
    # Por exemplo, chame uma função que inicie o robô
    print("Robô iniciado!")
    return 'Robô iniciado!'

if __name__ == '__main__':
    app.run()