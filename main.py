import tkinter as tk

class Page():
    def __init__(self, name):
        self.name_cur = name
        self.body = []
    def add(self, body):
        self.body += [body]

def run(*objs):

    initVars = ""
    view = ""
    Btn1 = ""
    Btn2 = ""
    Btn3 = ""
    KeyB = ""

    pages = "pages = {\n"

    for obj in objs:
        view += f"def {obj.name_cur}_page():\n"
        view += f"\tglobal canvas"
        pages += f"\t\t'{obj.name_cur}': {obj.name_cur}_page,\n"
        for elem in obj.body:
            initVars += elem['vars']
            view += "\n\t" + elem['global'] + "\n\n"
            view += elem['view']
            Btn1 += "\n\t" + elem['global'] + "\n\n"
            Btn1 += elem['Btn1']
            Btn2 += elem['Btn2']
            Btn3 += elem['Btn3']
            KeyB += elem['KeyB']
        view += "\n\tcanvas.update()\n\n"

    finalCode = "# Tkinter Design Kruglov Leonid 2020\n\n"
    finalCode += "def push_screen(url): None\n\n"
    finalCode += "import tkinter\n"
    finalCode += "import time\n\n"
    finalCode += "root = tkinter.Tk()\n"
    finalCode += "root.geometry('1020x800')\n"
    finalCode += "canvas = tkinter.Canvas(root, width=1020, height=800)\n"
    finalCode += f"\nurl = '{objs[0].name_cur}'\n"
    finalCode += f"\nscreen_action = 'PUSH'\n\n"
    finalCode += f"{initVars}\n"
    finalCode += f"{view}"

    finalCode += f"def present():\n"
    finalCode += "\tglobal url, canvas, screen_action\n"
    finalCode += "\tif screen_action != 'MOVE':\n"
    finalCode += "\t\tcanvas.delete('all')\n"
    finalCode += f"\t{pages}\t{'}'}\n"
    finalCode += f"\tpages[url]()\n\n"

    finalCode += f"def button1_click(event):\n"
    finalCode += f"\tglobal screen_action\n\n"
    finalCode += f"\tclick_x = event.x\n"
    finalCode += f"\tclick_y = event.y\n"
    finalCode += f"{Btn1}"

    finalCode += f"def push_screen(url_next):\n"
    finalCode += f"\tglobal url, screen_action\n\n"
    finalCode += f"\tscreen_action = 'PUSH'\n"
    finalCode += f"\turl = url_next\n"
    finalCode += f"\tpresent()\n"

    finalCode += f"def tab_next_active():\n"
    finalCode += f"\tglobal url, screen_action\n\n"
    finalCode += f"\tscreen_action = 'PUSH'\n"
    finalCode += f"\turl = url_next\n"
    finalCode += f"\tpresent()\n"

    finalCode += "present()\n\n"
    finalCode += "root.bind('<Button-1>', button1_click)\n\n"
    finalCode += "canvas.pack()\n"
    finalCode += "canvas.update()\n"
    finalCode += "root.mainloop()\n"

    return finalCode

class export:
  Page = Page
  run = run

def main():
  return export()
