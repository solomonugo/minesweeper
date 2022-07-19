from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location, bgcolor, text):
        btn = Button(
            location,
            bg = bgcolor,
            text = text
        )
        self.cell_btn_object = btn

    def cell_place(self, column, row):
        self.cell_btn_object.grid(
            column = column,
            row = row
        )

    def add_cell(self, frame, color, text, column, row):
        self.create_btn_object(frame, color, text)
        self.cell_place(column, row)
