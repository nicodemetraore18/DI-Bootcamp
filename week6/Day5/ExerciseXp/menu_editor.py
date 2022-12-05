import psycopg2
from config import config
from menu import MenuItem


new=MenuItem()

def show_user_menu():
    while True:
        choose=input('''
            MENU
            (a) Add an item
            (d) Delete an item
            (v) View the menu
            (x) Exit
            : 
            ''')
        match choose:
            case "a":
                add_item_to_menu()
            
            case "d":
                remove_item_from_menu()
                
            case "v":
                show_restaurant_menu()
                
            case "x":
                show_restaurant_menu()
                exit()


def add_item_to_menu():
    name=input("give the item's name: ")
    price=input("give the item's price: ")
    new.save(name,price)
    print("item was added successfully")

def remove_item_from_menu():
    rm=input("input the number of the item you want to renove from the restaurant's menu: ")
    if(new.delete(rm)):
        print('delete was completed')
    else:
        print('error: the item not exists in the restaurant menu.')

def show_restaurant_menu():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT menu_id,name,price FROM restaurant ORDER BY menu_id")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        
if __name__=='__main__':
    show_user_menu()