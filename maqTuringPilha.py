import tkinter as tk

# Configurações iniciais
class TuringMachine:
    def __init__(self, input1, input2):
        self.tape = list('*' * input1 + ' ' + '*' * input2 + ' ')  # Fita inicial
        self.head_position = 0  # Posição inicial do apontador
        self.state = 0  # Estado inicial
        self.running = True
        self.stack = []  # Inicializa a pilha vazia

    def step(self):
        # Executa um único passo da máquina de Turing
        if not self.running:
            return

        current_cell = self.tape[self.head_position]

        # Estado 0
        if self.state == 0:
            if current_cell == '*':
                self.stack.append('*')  # Empilha o símbolo lido
                self.head_position += 1
            elif current_cell == ' ':
                self.tape[self.head_position] = '*'  # Escreve na fita
                self.stack.append('*')  # Empilha quando escreve
                self.head_position += 1
                self.state = 1

        # Estado 1
        elif self.state == 1:
            if current_cell == '*':
                self.stack.append('*')  # Empilha o símbolo lido
                self.head_position += 1
            elif current_cell == ' ':
                self.head_position -= 1
                self.state = 2

        # Estado 2
        elif self.state == 2:
            if current_cell == '*':
                self.tape[self.head_position] = ' '
                self.stack.pop()  # Desempilha ao apagar
                if not self.stack:  # Se a pilha estiver vazia, termina a execução
                    self.running = False

    def display_tape(self):
        # Retorna o estado atual da fita como string
        return ''.join(f'({c})' if i == self.head_position else c for i, c in enumerate(self.tape))

# Funções de controle da interface
def run_step():
    turing_machine.step()
    tape_display.config(text=turing_machine.display_tape())
    display_stack_visual()  # Atualizar a pilha visualmente
    if turing_machine.running:
        root.after(1000, run_step)  # Repetir o passo automaticamente após 1 segundo

# Função para exibir a pilha como quadrados verticais
def display_stack_visual():
    # Limpar o display da pilha
    for widget in stack_display.winfo_children():
        widget.destroy()

    # Adiciona a etiqueta "Topo"
    if turing_machine.stack:
        tk.Label(stack_display, text="Topo", font=("Courier", 14)).pack()

        # Exibir os elementos da pilha
        for item in reversed(turing_machine.stack):  # Mostrar de cima para baixo
            label = tk.Label(stack_display, text=f"  {item}  ", font=("Courier", 14), relief="solid", width=4, height=2)
            label.pack()

        # Adiciona a etiqueta "Base"
        tk.Label(stack_display, text="Base", font=("Courier", 14)).pack()
    else:
        tk.Label(stack_display, text="(Pilha vazia)", font=("Courier", 14)).pack()

# Função para desempilhar e contar
def desempilhar():
    total = 0
    while turing_machine.stack:  # Enquanto a pilha não estiver vazia
        # Remove o elemento do topo da pilha (último a entrar)
        item = turing_machine.stack.pop()  # Desempilha
        total += 1  # Incrementa o total
        display_stack_visual()  # Atualiza a visualização da pilha
        total_display.config(text=f"TOTAL: {total}")  # Atualiza o texto do total
        root.update()  # Atualiza a interface
        root.after(1000)  # Espera 1 segundo antes de continuar

# Interface com Tkinter
def create_gui():
    global tape_display, stack_display, total_display, root

    # Janela principal
    root = tk.Tk()
    root.title("Simulador de Máquina de Turing com Pilha")

    # Entrada para os números
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Número 1: ").pack(side=tk.LEFT)
    num1_entry = tk.Entry(input_frame, width=5)
    num1_entry.pack(side=tk.LEFT)

    tk.Label(input_frame, text="Número 2: ").pack(side=tk.LEFT)
    num2_entry = tk.Entry(input_frame, width=5)
    num2_entry.pack(side=tk.LEFT)

    # Botão para iniciar a simulação
    def start_simulation():
        global turing_machine
        num1 = int(num1_entry.get())
        num2 = int(num2_entry.get())
        turing_machine = TuringMachine(num1, num2)
        tape_display.config(text=turing_machine.display_tape())
        display_stack_visual()  # Atualizar a pilha visualmente
        run_step()  # Iniciar o processo automaticamente

    tk.Button(root, text="Iniciar", command=start_simulation).pack(pady=10)

    # Botão para desempilhar
    tk.Button(root, text="Desempilhar", command=desempilhar).pack(pady=10)

    # Visualização da fita
    tape_display = tk.Label(root, text="", font=("Courier", 18))
    tape_display.pack(pady=10)

    # Display do total
    total_display = tk.Label(root, text="TOTAL: 0", font=("Courier", 16))
    total_display.pack(pady=10)

    # Visualização da pilha
    stack_display = tk.Frame(root)  # Mudando de Label para Frame para conter os quadrados
    stack_display.pack(pady=10)

    root.mainloop()

# Iniciar a interface
if __name__ == "__main__":
    create_gui()
