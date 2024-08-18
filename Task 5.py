import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        self.contacts = []
        self.filename = "contacts.json"
        
        # Create GUI elements
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.phone_label = tk.Label(root, text="Phone")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.email_label = tk.Label(root, text="Email")
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.address_label = tk.Label(root, text="Address")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        
        self.address_entry = tk.Entry(root, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)
        
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=6, column=0, padx=10, pady=10)
        
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=1, padx=10, pady=10)
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, padx=10, pady=10)
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=7, column=1, padx=10, pady=10)
        
        # Load existing contacts from file
        self.load_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contacts.append(contact)
            self.save_contacts()
            self.clear_entries()
            self.view_contacts()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required!")
    
    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    
    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number:")
        if query:
            self.listbox.delete(0, tk.END)
            found = False
            for contact in self.contacts:
                if query.lower() in contact['name'].lower() or query in contact['phone']:
                    self.listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
                    found = True
            if not found:
                messagebox.showinfo("Search Result", "No contact found")
    
    def update_contact(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            contact = self.contacts[index]
            new_name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact['name'])
            new_phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact['phone'])
            new_email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact['email'])
            new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact['address'])
            
            contact['name'] = new_name or contact['name']
            contact['phone'] = new_phone or contact['phone']
            contact['email'] = new_email or contact['email']
            contact['address'] = new_address or contact['address']
            
            self.save_contacts()
            self.view_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update")
    
    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.contacts[index]
            self.save_contacts()
            self.view_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
    
    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file)
    
    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                self.contacts = json.load(file)
                self.view_contacts()
        except FileNotFoundError:
            self.contacts = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
