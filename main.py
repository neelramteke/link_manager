import sqlite3
import segno  

conn = sqlite3.connect('link_store.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS links (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               link TEXT NOT NULL
)''')


def list_links():
    cursor.execute("SELECT * FROM links")
    for row in cursor.fetchall():
      print(row)

def add_link(name, link):
    cursor.execute("INSERT INTO links (name, link) VALUES (?, ?)", (name, link))
    conn.commit()

def link_qr(link_id):
    # Fetch the link from the database
    cursor.execute("SELECT link FROM links WHERE id = (?)", (link_id))
    link = cursor.fetchone()[0]  # Get the first column of the result

    # Generate the QR code
    qr = segno.make_qr(link)
    
    qr.save("link_qr.png", scale=5)
    print(qr)

def delete_link(link_id):
    cursor.execute("DELETE FROM links WHERE id = (?)", (link_id))
    conn.commit()

def main():
    while True:
        print("\n WELCOME BUDDY! \n TO LINK STORE")
        

        print("1. List all links")
        print("2. Enter a link")
        print("3. Make a QR code of a link (Please enter the link first)")
        print("4. Delete a link")
        print("5. Exit the application")
        choice = input("Please enter a choice from below:")

        if choice == '1':
            list_links()

        elif choice == '2':
            name = input("Enter the link name: ")
            link = input("Enter the link: ")
            add_link(name, link)
        
        elif choice == '3':
            link_id = input("Enter the Id of the link which you want to make QR code: ")
            link_qr(link_id)

        elif choice == '4':
            link_id = input("Enter the ID of the link you want to delete: ")
            delete_link(link_id)
        
        elif choice == '5':
            break

        else:
            print("Invalid choice")


    conn.close

            
if __name__ == "__main__":
    main()