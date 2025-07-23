# 🖱️ Automação com PyAutoGUI + Interface Tkinter

Este repositório contém uma série de scripts em Python desenvolvidos para automações com **PyAutoGUI** e uma interface gráfica de cadastro com **Tkinter**. Ideal para quem deseja automatizar tarefas no desktop e entender melhor como controlar mouse, teclado, janelas e formulários via código.

---

## 📂 Conteúdo

### 📌 `abrir_calculadora.py`
Abre automaticamente o menu iniciar, digita "calculadora" e executa o aplicativo.  
Ideal para demonstrar automações simples e rápidas de teclado.

### 📌 `interacoes_mouse_teclado.py`
Demonstra diversos comandos do PyAutoGUI para:
- Mover e clicar o mouse 🖱️
- Digitar e usar atalhos de teclado ⌨️
- Interagir com caixas de mensagem 🪟
- Tirar screenshots da tela 📸

### 📌 `cadastro_alunos.py`
Lê um arquivo `alunos.txt` com nome e email, e preenche um formulário automaticamente:
- Simula o preenchimento dos campos
- Realiza clique no botão "Add"
- Tira screenshot de cada cadastro para auditoria

### 📌 `interface_tkinter.py`
Interface gráfica simples com **Tkinter** para cadastrar alunos manualmente:
- Campos de entrada para Nome e Email
- Lista de alunos cadastrados com `Treeview`
- Botão para salvar e limpar campos

### 📌 `screenshot_loop.py`
Tira um print da tela a cada 3 segundos e salva com timestamp.  
Útil para monitoramento ou auditoria automática de ações na tela.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pypi.org/project/pyautogui/)
- [Tkinter (GUI padrão do Python)](https://docs.python.org/pt-br/3/library/tkinter.html)

---

## ⚠️ Avisos Importantes

- **FailSafe:** Todos os scripts possuem mecanismo de segurança. Mova o mouse para o canto superior esquerdo para interromper a execução.
- **Cuidado com cliques automáticos:** Execute em ambiente controlado para evitar ações indesejadas.
- **Requisitos:** `alunos.txt` deve estar no formato `nome,email` em cada linha.

---

## 📷 Exemplo de uso

```bash
# Para rodar o script de cadastro automático:
python cadastro_alunos.py
