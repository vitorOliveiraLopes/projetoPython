import PySimpleGUI as sg
import pathlib

sg.ChangeLookAndFeel('Black') # change style

WIN_W = 50
WIN_H = 15
file = None

menu_layout = [
                ['Arquivo', ['Novo (Ctrl+N)', 'Abrir (Ctrl+O)', 'Salvar (Ctrl+S)', 'Salvar como', '---', 'Sair']],
                ['Ferramentas', ['Contar palavras']],
                ['Ajuda', ['Sobre']],
                ['Menu', ['Minimizar', 'Maximizar', 'Reduzir', 'Sair']]
            ]

layout = [[sg.Menu(menu_layout)],
          [sg.Text('> Novo arquivo <', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
          [sg.Multiline(font=('Roboto', 16), size=(WIN_W, WIN_H), key='_BODY_')]]

window = sg.Window('Notepad', layout=layout, 
                        margins=(0, 0), 
                        resizable=True, 
                        return_keyboard_events=True, 
                        keep_on_top = True,
                        element_padding = (0,0),
                        alpha_channel = .8,
                        no_titlebar=True,
                        finalize = True)

window['_BODY_'].expand(expand_x=True, expand_y=True)

def new_file():
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> Novo arquivo <')
    file = None
    return file

def open_file():
    filename = sg.popup_get_file('Abrir', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        window['_BODY_'].update(value=file.read_text())
        window['_INFO_'].update(value=file.absolute())
        return file

def save_file(file):
    if file:
        file.write_text(values.get('_BODY_'))
    else:
        save_file_as()

def save_file_as():
    filename = sg.popup_get_file('Salvar como', save_as=True, no_window=True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get('_BODY_'))
        
        window['_INFO_'].update(value=file.absolute())
        return file

def word_count():
    words = [w for w in values['_BODY_'].split(' ') if w!='\n']
    word_count = len(words)
    sg.popup_no_wait('Contar palavras: {:,d}'.format(word_count))

def about_me():
    sg.popup_no_wait('Use a barra preta (Menu) para reposicionar o aplicativo')

def fechar():
    sg.popup_auto_close()

def minimizar():
    window.minimize()

def maximizar():
    window.maximize()

def reduzir():
    window.normal()

while True:
    event, values = window.read()
    if event in('Sair', None):
        break
    if event in ('Novo (Ctrl+N)', 'n:78'):
        file = new_file()
    if event in ('Abrir (Ctrl+O)', 'o:79'):
        file = open_file()
    if event in ('Salvar (Ctrl+S)', 's:83'):
        save_file(file)
    if event in ('Salvar como',):
        file = save_file_as()   
    if event in ('Contar palavras',):
        word_count() 
    if event in ('Sobre',):
        about_me()
    if event in ('Minimizar',):
        minimizar()
    if event in ('Maximizar',):
        maximizar()
    if event in ('Reduzir',):
        reduzir()
    if event in ('Sair',):
        fechar()