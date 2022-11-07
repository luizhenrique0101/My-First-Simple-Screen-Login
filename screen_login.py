from tkinter import *
from tkinter.font import Font


window = Tk()


class Colors:
    white  = '#fefefe'
    black  = '#020202'
    cyan   = '#0af2e1'
    gray   = '#3b3b3b'
    light_gray = '#525252'
    yellow = '#fff900'


#TODO Organizar melhor está classe de estilo (criar função para cada tipo de atividade)
#TODO Renomear as variáveis 'text color'. 'label_color' das labels
#TODO Renomear a variável 'main title' para 'main_title_text'
class Style:
    main_title = Font(window,
    size=40,
    weight='bold',
    slant='roman')

    labels_text = Font(window,
    size=12,
    weight='bold',
    slant='roman')


    inbox_text = Font(window,         
    size=11,
    weight='bold',
    slant='roman')


    button_text = Font(window,
    size=20,
    weight='bold',
    slant='roman')

    frame_lines_thickness = 3

    padx_label_spacing = 20
    pady_label_spacing = 40

    inbox_text_color  = Colors.white
    label_color = Colors.white
    button_text_color = Colors.white
    main_title_bar_color = Colors.yellow
    input_bar_frames_color  = Colors.cyan
    background_color = Colors.gray



class ScreenLogin():
    def __init__(self) -> None:
        self.window = window
        self.centered_screen()
        self.configuration()
        self.screen_main_title()
        self.widgets()
        self.window.mainloop()


    def centered_screen(self):
        self.width = 416
        self.height = 624

        self.screenwidth = window.winfo_screenwidth()
        self.screenheight = window.winfo_screenheight()
        self.positionX = self.screenwidth/2 - self.width/2
        self.positionY = self.screenheight/2 - self.height/2

    
    def configuration(self):
        self.window.title('Tela de Login')
        self.window.iconbitmap('')
        self.window.geometry('%dx%d+%d+%d' %(self.width, self.height, self.positionX, self.positionY))
        self.window.configure(bg=Style.background_color)
        self.window.resizable(False,False)


    #TODO criar um único frame da barra do título principal
    def  screen_main_title(self):
        Label(self.window, 
        text='Login',
        font=Style.main_title,
        bg=Style.background_color, 
        fg=Style.label_color).pack(side='top', pady=15)

        Frame(self.window, bg= Style.main_title_bar_color).place(x=99, y=74, width=107, height=4)
        Frame(self.window, bg= Style.main_title_bar_color).place(x=225, y=74, width=94, height=4)


    def widgets(self):
        def labels(self):
            self.label_name = Label(self.window, 
            text='Nome',
            font=Style.labels_text,
            fg=Style.label_color,
            bg=Style.background_color).pack(side='top',padx=Style.padx_label_spacing, pady=Style.pady_label_spacing)


            self.label_age = Label(self.window, 
            text='Idade',
            font=Style.labels_text,
            fg=Style.label_color,
            bg=Style.background_color).pack(side='top',padx=Style.padx_label_spacing, pady=Style.pady_label_spacing)


            self.label_email = Label(self.window, 
            text='Email',
            font=Style.labels_text,
            fg=Style.label_color,
            bg=Style.background_color).pack(side='top',padx=Style.padx_label_spacing, pady=Style.pady_label_spacing)


            self.label_password = Label(self.window, 
            text='Senha',
            font=Style.labels_text,
            fg=Style.label_color,
            bg=Style.background_color).pack(side='top',padx=Style.padx_label_spacing, pady=Style.pady_label_spacing)

        
        def entrys(self):
            self.entry_name = Entry(self.window,
            font=Style.inbox_text,
            fg=Style.inbox_text_color,
            bd=0,
            bg=Style.background_color,
            width=25).place(x=107, y=160)


            self.entry_age = Entry(self.window, 
            font=Style.inbox_text,
            fg=Style.inbox_text_color,
            bd=0,
            bg=Style.background_color,
            width=6).place(x=199, y=265)

            
            self.entry_email = Entry(self.window, 
            font=Style.inbox_text,
            fg=Style.inbox_text_color,
            bd=0,
            bg=Style.background_color,
            width=25).place(x=107, y=370)


            self.entry_password = Entry(self.window, 
            font=Style.inbox_text,
            fg=Style.inbox_text_color,
            bd=0,
            bg=Style.background_color,
            width=25).place(x=107, y=475)


        def frames(self):
            self.frame_name = Frame(self.window,
            bg= Style.input_bar_frames_color ,
            height=Style.frame_lines_thickness).place(x=108, y=180, width=200)


            self.frame_age = Frame(self.window,
            bg= Style.input_bar_frames_color ,
            height=Style.frame_lines_thickness).place(x=177, y=285, width=60)


            self.frame_email = Frame(self.window,
            bg= Style.input_bar_frames_color ,
            height=Style.frame_lines_thickness).place(x=108, y=390, width=200)


            self.frame_password = Frame(self.window,
            bg= Style.input_bar_frames_color ,
            height=Style.frame_lines_thickness).place(x=108, y=495, width=200)


        def buttons(self):
            self.finish = Button(self.window, text='Finalizar',
            fg= Style.button_text_color,
            bd=0,
            bg=Colors.light_gray,
            command="").place(x=95, y=540, relwidth=0.55, relheight=0.090)
        return labels(self), frames(self), entrys(self), buttons(self)


ScreenLogin()