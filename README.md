# Sistema de Cadastro de Pessoas

Sistema em Python para cadastro e leitura de pessoas utilizando arquivos `.txt`.

## 🚀 Funcionalidades

* Cadastro de pessoas
* Leitura de dados
* Armazenamento em arquivo
* Interface via terminal

## 🛠️ Tecnologias

* Python 3

## ▶️ Como executar

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
python main.py
```

## 📂 Estrutura

```
projeto/
│── main.py
│── lib/
│   ├── interface.py
│   └── archive.py
│── people.txt
```

## ▶️ Como usar

Ao executar o programa, um menu será exibido no terminal com as seguintes opções:

1. **Listar pessoas cadastradas**
   
   * Exibe todas as pessoas salvas no arquivo
   * Mostra nome e idade formatados

2. **Cadastrar nova pessoa**
 
   * Permite inserir o nome e a idade do usuário
   * Os dados são armazenados no arquivo `people.txt`

3. **Sair do sistema**

   * Encerra a execução do programa

### 💡 Funcionamento interno

* Os dados são salvos no formato:

  ```
  nome;idade
  ```
* O sistema utiliza:

  * Manipulação de arquivos (`open`, `read`, `write`)
  * Tratamento de erros com `try/except`
  * Modularização com arquivos separados (`interface` e `archive`)


## 💡 Aprendizados

* Manipulação de arquivos
* Tratamento de erros
* Modularização do código

## 📌 Status

✔️ Projeto finalizado

## 👨‍💻 Autor

Arthur Teixeira

* GitHub: https://github.com/ArthurTeix
* LinkedIn: https://www.linkedin.com/in/arthur-teixeira-da-costa-lima-b47a83283/
