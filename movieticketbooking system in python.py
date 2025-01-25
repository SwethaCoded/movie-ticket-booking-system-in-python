import tkinter as tk

class MovieTicketBookingSystem:
    def __init__(self, master):
        self.master = master
        master.title("Movie Ticket Booking System")

        # Create widgets
        self.movie_label = tk.Label(master, text="Select a movie:")
        self.movie_label.grid(row=0, column=0, padx=10, pady=10)
        self.movie_listbox = tk.Listbox(master, height=5)
        self.movie_listbox.grid(row=0, column=1, padx=10, pady=10)
        self.movies = {"Toy story-Rs412": 412, "The lion king-Rs410": 410, "Enchanto-Rs308": 308,"Soul-Rs.300":300} # Movie ticket prices
        for movie in self.movies:
            self.movie_listbox.insert(tk.END, movie)

        self.time_label = tk.Label(master, text="Select a show time:")
        self.time_label.grid(row=1, column=0, padx=10, pady=10)
        self.time_listbox = tk.Listbox(master, height=5)
        self.time_listbox.grid(row=1, column=1, padx=10, pady=10)
        self.time_listbox.insert(tk.END, "10:00 AM")
        self.time_listbox.insert(tk.END, "1:00 PM")
        self.time_listbox.insert(tk.END, "4:00 PM")
        self.time_listbox.insert(tk.END, "7:00 PM")
        self.time_listbox.insert(tk.END, "10:00 PM")

        self.quantity_label = tk.Label(master, text="Select number of tickets:")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=10)
        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)

        self.name_label = tk.Label(master, text="Enter your name:")
        self.name_label.grid(row=3, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=3, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(master, text="Enter your phone number:")
        self.phone_label.grid(row=4, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=4, column=1, padx=10, pady=10)

        self.book_button = tk.Button(master, text="Book Now", command=self.book_ticket)
        self.book_button.grid(row=5, column=1, padx=10, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def book_ticket(self):
        movie = self.movie_listbox.get(tk.ACTIVE)
        time = self.time_listbox.get(tk.ACTIVE)
        quantity = int(self.quantity_entry.get())
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        # Perform booking operation
        ticket_price = self.movies[movie]
        total_price = quantity * ticket_price

        # Display result
        result_text = f"Booked {quantity} tickets for {movie} at {time} by {name} ({phone}). Total price: Rs.{total_price}"
        self.result_label.config(text=result_text)

root = tk.Tk()
app = MovieTicketBookingSystem(root)
root.mainloop()
