from tkinter import Frame,Label,CENTER
import logics
import constants as c

class game_2048(Frame):
    def __init__(self):
        Frame.__init__(self)                     # creating frame of 0 width and 0 height

        self.grid()                              # frame is represented in the form of grid
        self.master.title("2048")                # setting title of the window
        self.master.bind("<Key>",self.key_pressed)  # if any key is pressed inside the frame then key_pressed func is called 

        self.commands = {c.key_up:logics.up_move , c.key_down:logics.down_move , c.key_left:logics.left_move ,
                          c.key_right:logics.right_move }  # mapping keys with the functions

        self.grid_cells = []                     
        self.init_grid()                         # initialize the grid cells inside the frame with background color
        self.init_matrix()                       # random two 2 will be added in the matrix and rest with 0
        self.update_grid_cells()                 # changing the bg_color and text color of the matrix such as for 2
        self.mainloop()                          # to run the execution , waits for any event to occur

    def init_grid(self):

        # creating a new frame inside original frame represnted as self 
        inside_frame = Frame(self,bg = c.background_color , width = c.game_size , height = c.game_size)   

        inside_frame.grid()                      # creating inside frame also a grid

        # adding cells inside the frame 
        for i in range(c.game_size):
            grid_row = []
            for j in range(c.game_size):
                # creating a new frame(cell) in inside_frame
                cell = Frame(inside_frame,bg = c.background_color_cell_empty,height = c.window_size/c.game_size,
                       width = c.window_size/c.game_size)

                # adding a cell inside the grid
                cell.grid(row = i,column = j,padx = c.grid_padding,pady = c.grid_padding)

                t = Label(master = cell , text = "" , bg = c.background_color_cell_empty , justify = CENTER , 
                    font = c.font , width = 5 , height = 2)
                t.grid()

                grid_row.append(t)
            self.grid_cells.append(grid_row)

    # create a matrix for internal operations which will be reflected in the UI
    def init_matrix(self):
        self.game_matrix = logics.start_game()
        logics.add_random_2(self.game_matrix)
        logics.add_random_2(self.game_matrix)
 
    #UI is changed according to the internal matrix
    def update_grid_cells(self):
        for i in range(c.game_size):
            for j in range(c.game_size):
                new_number = self.game_matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text = "",bg = c.background_color_cell_empty)
                else:
                    self.grid_cells[i][j].configure(text = str(self.game_matrix[i][j]),
                    bg = c.background_color_dict[new_number],fg = c.cell_color_dict[new_number])
        self.update_idletasks()

    def key_pressed(self,event):
        key = repr(event.char)             #repr return the printable part of the object i.e "'w'"
        if key in self.commands:
            #calling keys functions
            self.game_matrix,ischanged = self.commands[repr(event.char)](self.game_matrix)
            if ischanged:
                logics.add_random_2(self.game_matrix)
                self.update_grid_cells()                       #update the UI because a new 2 has been added

                ischanged = False
                if logics.check_current_state(self.game_matrix) == "WON":
                    self.grid_cells[c.game_size//2][(c.game_size//2)-1].configure(text = "YOU", bg = c.background_color_cell_empty)
                    self.grid_cells[c.game_size//2][c.game_size//2].configure(text = "WIN", bg = c.background_color_cell_empty)
                if logics.check_current_state(self.game_matrix) == "LOST":
                    self.grid_cells[c.game_size//2][(c.game_size//2)-1].configure(text = "YOU", bg = c.background_color_cell_empty)
                    self.grid_cells[c.game_size//2][c.game_size//2].configure(text = "LOSE", bg = c.background_color_cell_empty)
                
game = game_2048()     

    
        




