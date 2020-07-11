# from tkinter import * #imports tkinter package available in python


# def start_main_page(): #function definition of start_main_page
#     def start_game(args): #function definition of start game
#         main_window.destroy()
#         if args == 1:  #if arguement equals one
#             from Options import Animals
#             Animals.main() #calling of function
#         elif args == 3: #if arguement equals three
#              from Options import Colour
#              Colour.main()
#         elif args == 6: #if arguement equals six
#             from Options import Vegetable
#             Vegetable.main()
       

#     def option(): #styling the buttons

#         lab_img1 = Button(
#             main_window,
#             image=img1,
#             bg='#e6fff5',
#             border=0,
#             justify='center',

#         )
#         sel_btn1 = Button( #styling button animals
#             text="Animals",
#             width=18,
#             borderwidth=8,
#             font=("", 18),
#             fg="#000000",
#             bg="#99ffd6",
#             cursor="hand2",
#             command=lambda: start_game(1),
#         )



#         sel_btn3 = Button(  #styling button colour
#             text="Colour",
#             width=18,
#             borderwidth=8,
#             font=("", 18),
#             fg="#000000",
#             bg="#99ffd6",
#             cursor="hand2",
#             command=lambda: start_game(3),
#         )

        
 
#         sel_btn6 = Button(  #styling button Vegetable
#             text="Vegetable",
#             width=18,
#             borderwidth=8,
#             font=("", 18),
#             fg="#000000",
#             bg="#99ffd6",
#             cursor="hand2",
#             command=lambda: start_game(6),
#         )

       
#         lab_img1.grid(row=0, column=0, padx=20) #aligning the buttons in the gui window
#         sel_btn1.grid(row=4, column=4, pady=(10, 0), padx=50, )
        
#         sel_btn3.grid(row=5, column=4, pady=(10, 0), padx=50, )
       
#         sel_btn6.grid(row=6, column=4, pady=(10, 0), padx=50, )
       

#     def show_option(): #defining function called show_option
#         start_btn.destroy()

#         lab_img.destroy()
#         option()

#     main_window = Tk()
# #styling of main window
#     main_window.geometry("500x500+500+150")
#     main_window.resizable(0, 0)
#     main_window.title("Quizee --> Grow your kids with Quizee")
#     main_window.configure(background="#FAEBD7")
#     main_window.iconbitmap(r'quizee_logo_.ico')

#     img0 = PhotoImage(file="quizee_logo.png")
#     img1 = PhotoImage(file="back.png")

#     lab_img = Label(
#         main_window,
#         image=img0,
#         bg='#e6fff5',
#     )
#     lab_img.pack(pady=(50, 0))

#     start_btn = Button(
#         main_window,
#         text="Start",
#         width=20,
#         borderwidth=10,
#         fg="#111111",
#         bg="#99ffd6",
#         font=("", 18),
#         cursor="hand2",
#         command=show_option,
#     )
#     start_btn.pack(pady=(50, 20))

#     main_window.mainloop()


# start_main_page()



from tkinter import * #imports tkinter package available in python
def start_main_page(): #function definition of start_main_page
    def start_game(args): #function definition of start game
        main_window.destroy()
        if args == 1:  #if arguement equals one
            from Options import Animals
            Animals.main() #calling of function
        elif args == 3: #if arguement equals three
             from Options import Colour
             Colour.main()
        elif args == 6: #if arguement equals six
            from Options import Vegetable
            Vegetable.main()
       
    def option(): #styling the buttons

        lab_img1 = Button(
            main_window,
            image=img1,
            bg='#e6fff5',
            border=0,
            justify='center',)
        sel_btn1 = Button( #styling button animals
            text="Animals",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(1),
        )
        sel_btn3 = Button(  #styling button colour
            text="Colour",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        
 
        sel_btn6 = Button(  #styling button Vegetable
            text="Vegetable",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(6),
        )

       
        lab_img1.grid(row=0, column=0, padx=20) #aligning the buttons in the gui window
        sel_btn1.grid(row=4, column=4, pady=(10, 0), padx=50, )
        
        sel_btn3.grid(row=5, column=4, pady=(10, 0), padx=50, )
       
        sel_btn6.grid(row=6, column=4, pady=(10, 0), padx=50, )
       

    def show_option(): #defining function called show_option
        start_btn.destroy()
        lab_img.destroy()
        option()
    main_window = Tk()
#styling of main window
    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Quizee --> Grow your kids with Quizee")
    main_window.configure(background="#FAEBD7")
    main_window.iconbitmap(r'quizee_logo_.ico')
    img0 = PhotoImage(file="quizee_logo.png")
    img1 = PhotoImage(file="back.png")
    lab_img = Label(
        main_window,
        image=img0,
        bg='#e6fff5',
    )
    lab_img.pack(pady=(50, 0))
    start_btn = Button(
        main_window,
        text="Start",
        width=20,
        borderwidth=10,
        fg="#111111",
        bg="#99ffd6",
        font=("", 18),
        cursor="hand2",
        command=show_option,)
    start_btn.pack(pady=(50, 20))
    main_window.mainloop()
start_main_page()