import random

def sorteio(categoria):
    lista = ["Alabama","Montgomery","Alaska","Juneau","Arizona","Phoenix","Arkansas","Little Rock","California","Sacramento","Colorado","Denver","Connecticut","Hartford","Delaware","Dover","Florida","Tallahassee","Georgia","Atlanta","Hawaii","Honolulu","Idaho","Boise","Illinois","Springfield","Indiana","Indianapolis","Iowa","Des Moines","Kansas","Topeka","Kentucky","Frankfort","Louisiana","Baton Rouge","Maine","Augusta","Maryland","Annapolis","Massachusetts","Boston","Michigan","Lansing","Minnesota","Saint Paul","Mississippi","Jackson","Missouri","Jefferson City","Montana","Helena","Nebraska","Lincoln","Nevada","Carson City","New Hampshire","Concord","New Jersey","Trenton","New Mexico","Santa Fe","New York","Albany","North Carolina","Raleigh","North Dakota","Bismarck","Ohio","Columbus","Oklahoma","Oklahoma City","Oregon","Salem","Pennsylvania","Harrisburg","Rhode Island","Providence","South Carolina","Columbia","South Dakota","Pierre","Tennessee","Nashville","Texas","Austin","Utah","Salt Lake City","Vermont","Montpelier","Virginia","Richmond","Washington","Olympia","West Virginia","Charleston","Wisconsin","Madison","Wyoming","Cheyenne"
    ]

    lista_fruta = [
        'Avocado','Pineapple','Acai','Barbados cherry','Plum','Prunes','Blackberry','Araza','Atemoya','Banana','Yellow Cavendish Banana','Plantain','Manzano Banana','Dried Banana','Chunkey Banana','Jelly palm','Cocoa','Hog plum','Cashew','Cambuci','Persimmon','Star Fruit','Cherry','Black Cherry','Coconut','Cupuacu','Apricot','Fig','Raspberry','Sweetsop','Guava','Soursop','Gooseberry','Brazilian Grape','Jackfruit','Jambolan','Jenipapo','Kiwi','Orange','Lychee','Rangpur','Lemon','Persian lime','Apple','Green Papaya','Papaya','Mango','Mangosteen','Passion Fruit','Quince','Watermelon','Tangerine','Murcott','Ugli Fruit','Blueberry','Strawberry','Nectarine','Loquat','Cranberry','Pear','Peach','Dragon Fruit','Surinam cherry','Pomegranate','Clementine','Grapefruit','Grape','Raisins'
    ]

    if categoria == 'geografia':
        pos = random.randint(0, len(lista))
        return lista[pos]
    elif categoria == 'frutas':
        pos = random.randint(0, len(lista_fruta))
        return lista_fruta[pos]

