
import random
import tkinter as tk

root = tk.Tk()
root.title("AI Drawing Game")
root.configure(bg="#2b1d14")

GRID = 20
color = "#000000"
time_left = 30
running = False

canvas = tk.Canvas(
    root, width=400, height=400, bg="#f3e1b5", highlightthickness=0
)
canvas.pack(pady=10)


def draw_grid():
    for x in range(0, 400, GRID):
        canvas.create_line(x, 0, x, 400, fill="#b8b0a3")
    for y in range(0, 400, GRID):
        canvas.create_line(0, y, 400, y, fill="#b8b0a3")


def draw(event):
    if 0 <= event.x < 400 and 0 <= event.y < 400:
        x = (event.x // GRID) * GRID
        y = (event.y // GRID) * GRID
        canvas.create_rectangle(
            x, y, x + GRID, y + GRID, fill=color, outline="#b8b0a3"
        )


canvas.bind("<B1-Motion>", draw)
canvas.bind("<Button-1>", draw)


def update_color(val=None):
    global color
    r = red.get()
    g = green.get()
    b = blue.get()
    color = f"#{r:02x}{g:02x}{b:02x}"
    preview.configure(bg=color)


def send_to_ai():
    # Base dictionary of common things across multiple categories
    guesses = [
        # --- ANIMALS & CREATURES ---
        "a happy cat 🐱", "a playful dog 🐶", "a tiny mouse 🐭", "a fluffy hamster 🐹", "a cute rabbit 🐰",
        "a wild fox 🦊", "a big brown bear 🐻", "a giant panda 🐼", "a sleepy koala 🐨", "a fierce tiger 🐯",
        "a powerful lion 🦁", "a fast leopard 🐆", "a heavy horse 🐴", "a striped zebra 🦓", "a sturdy deer 🦌",
        "a massive ox 🐂", "a milk cow 🐄", "a pink pig 🐷", "a woolly sheep 🐑", "a curious goat 🐐",
        "a tall camel 🐫", "a long llama 🦙", "a giant giraffe 🦒", "a huge elephant 🐘", "a thick rhino 🦏",
        "a large hippo 🦛", "a slow monkey 🐵", "a swinging gorilla 🦍", "a smart chimpanzee 🦧", "a green frog 🐸",
        "a scaly crocodile 🐊", "a green turtle 🐢", "a slithering snake 🐍", "a flying dragon 🐉", "a swimming lizard 🦎",
        "a fierce dinosaur 🦖", "a friendly whale 🐳", "a jumping dolphin 🐬", "a scary shark 🦈", "a colorful fish 🐟",
        "a blue tropical fish 🐠", "a spikey blowfish 🐡", "a red lobster 🦞", "a small crab 🦀", "a giant squid 🦑",
        "a red octopus 🐙", "a slow snail 🐌", "a busy honeybee 🐝", "a crawling ant 🐜", "a jumping cricket 🦗",
        "a colorful butterfly 🦋", "a tiny ladybug 🐞", "a glowing firefly 🪰", "a creepy spider 🕷", "a stinging scorpion 🦂",
        "a buzzing mosquito 🦟", "a white dove 🕊", "a black crow 🐦", "a wise owl 🦉", "a colorful parrot 🦜",
        "a pink flamingo 🦩", "a waddling penguin 🐧", "a proud eagle 🦅", "a swimming duck 🦆", "a graceful swan 🦢",
        "a scratching chicken 🐔", "a loud rooster 🐓", "a small chick 🐥", "a wild turkey 🦃", "a colorful peacock 🦚",

        # --- FOOD & DRINK ---
        "a crisp green apple 🍏", "a ripe red apple 🍎", "a yellow pear 🍐", "a juicy orange 🍊", "a sour lemon 🍋",
        "a sweet banana 🍌", "a red watermelon 🍉", "a bunch of grapes 🍇", "a sweet strawberry 🍓", "a small blueberry 🫐",
        "a fuzzy melon 🍈", "a sweet cherry 🍒", "a fuzzy peach 🍑", "a tropical mango 🥭", "a spiky pineapple 🍍",
        "a brown coconut 🥥", "a green kiwi 🥝", "a ripe tomato 🍅", "a purple eggplant 🍆", "a green avocado 🥑",
        "a green broccoli 🥦", "a leafy lettuce 🥬", "a crunchy cucumber 🥒", "a spicy chili pepper 🌶", "a sweet corn 🌽",
        "a orange carrot 🥕", "a pungent garlic 🧄", "a round onion 🧅", "a brown potato 🥔", "a sweet potato 🍠",
        "a French croissant 🥐", "a loaf of bread 🍞", "a baked pretzel 🥨", "a round bagel 🥯", "a breakfast pancake 🥞",
        "a waffle 🧇", "a slice of cheese 🧀", "a bone-in steak 🥩", "a strip of bacon 🥓", "a chicken drumstick 🍗",
        "a burger 🍔", "a box of fries 🍟", "a slice of pizza 🍕", "a hot dog 🌭", "a pressed sandwich 🥪",
        "a Mexican taco 🌮", "a wrapped burrito 🌯", "a fried egg 🍳", "a bowl of hot stew 🍲", "a steaming fondue 🫕",
        "a bowl of ramen 🍜", "a plate of sushi 🍣", "a fried shrimp 🍤", "a fish cake 🍥", "a sweet dango 🍡",
        "a dumpling 🥟", "a fortune cookie 🥠", "a takeout box 🥡", "a soft-serve ice cream 🍦", "a shaved ice 🍧",
        "a scoop of ice cream 🍨", "a frosted doughnut 🍩", "a chocolate cookie 🍪", "a birthday cake 🎂", "a cupcake 🧁",
        "a slice of pie 🥧", "a chocolate bar 🍫", "a sweet candy 🍬", "a lollipop 🍭", "a custard pudding 🍮",
        "a jar of honey 🍯", "a glass of milk 🥛", "a hot coffee mug ☕", "a cup of green tea 🍵", "a teapot 🫖",
        "a soda can 🥤", "a box of juice 🧃", "a glass of water 🧊", "a salt shaker 🧂", "a popcorn bucket 🍿",

        # --- HOUSEHOLD OBJECTS ---
        "a wooden chair 🪑", "a comfortable couch 🛋", "a soft bed 🛏", "a wooden door 🚪", "a glass window 🪟",
        "a work desk 🖥", "a bright desk lamp 💡", "a flashlight 🔦", "a wax candle 🕯", "a trash can 🗑", 
        "a shopping cart 🛒", "a cardboard box 📦", "a heavy safe 🔐", "a key 🔑", "a padlock 🔒", 
        "a metal hammer 🔨", "a sharp axe 🪓", "a metal wrench 🔧", "a screwdriver 🪛", "a sharp pair of scissors ✂", 
        "a razor blade 🪒", "a sewing needle 🪡", "a paint brush 🖌", "a pencil ✏", "a fountain pen 🖋", 
        "a binder clip 📎", "a roll of tape 🎞", "a magnifying glass 🔍", "a wall mirror 🪞", "a bar of soap 🧼", 
        "a soft towel 🧻", "a white toilet 🚽", "a water shower 🚿", "a bathtub 🛁", "a toothbrush 🪥", 
        "a hair sponge 🧽", "a sweeping broom 🧹", "a water bucket 🪣", "a porcelain bowl 🥣", "a flat plate 🍽", 
        "a metal fork 🍴", "a soup spoon 🥄", "a kitchen knife 🔪", "a wine glass 🍷", "a beer mug 🍺", 

        # --- NATURE & WEATHER ---
        "a blazing sun ☀️", "a glowing crescent moon 🌙", "a sparkling star ⭐", "a fluffy white cloud ☁", "a dark storm cloud ⛈",
        "a pouring rain cloud 🌧", "a cold snowflake ❄", "a blast of wind 💨", "a bright flash of lightning ⚡", "a colorful rainbow 🌈",
        "a fiery flame 🔥", "a drop of water 💧", "a rolling ocean wave 🌊", "a tall mountain ⛰", "a smoking volcano 🌋",
        "a patch of green grass 🌱", "a green herb 🌿", "a lucky four-leaf clover 🍀", "a tall pine tree 🌲", "a leafy deciduous tree 🌳",
        "a tropical palm tree 🌴", "a prickly desert cactus 🌵", "a red rose flower 🌹", "a yellow sunflower 🌻", "a purple blossom 🌸",

        # --- CLOTHING & TRAVEL ---
        "a warm winter coat 🧥", "a bright t-shirt 👕", "a pair of blue jeans 👖", "a formal necktie 👔", "a summer dress 👗",
        "a baseball cap 🧢", "a royal crown 👑", "a straw sun hat 👒", "a pair of running shoes 👟", "a leather backpack 🎒",
        "a fast sports car 🚗", "an urban taxi cab 🚕", "a blue delivery truck 🚙", "a heavy city bus 🚌", "a mountain bicycle 🚲",
        "a fast motorcycle 🏍", "a flying airplane ✈", "a military helicopter 🚁", "a cruise ship 🚢", "a futuristic rocket ship 🚀",

        # --- HOBBY & FANTASY ---
        "a white soccer ball ⚽", "a orange basketball 🏀", "a video game controller 🎮", "a musical guitar 🎸", "a grand piano 🎹",
        "a shiny gold medal 🥇", "a championship trophy 🏆", "a wooden skateboard 🛹", "a small residential house 🏠", "a tall castle tower 🏰",
        "a magic wizard wand 🪄", "a sharp knight sword ⚔", "a spooky ghost 👻", "a green space alien 👽", "a futuristic robot 🤖"
    ]

    # Expand dataset to over 1,000 distinct visual descriptors dynamically
    adjectives = [
        "a giant", "a tiny", "a neon", "a shiny", "a broken", "a mysterious", "a golden", 
        "a futuristic", "a classic", "an old", "a pixelated", "a weird", "a beautiful", 
        "a massive", "a strange", "a dark", "a cosmic", "a flying", "a radioactive", "a vintage"
    ]
    static_guesses = list(guesses)
    
    while len(guesses) < 1005:
        base_item = random.choice(static_guesses)
        clean_item = base_item.replace("a ", "").replace("an ", "")
        guesses.append(f"{random.choice(adjectives)} {clean_item}")

    # Set selection onto display label
    timer_display.config(text=f"AI Guess: {random.choice(guesses)}")


def countdown():
    global time_left, running
    if not running:
        return
    if time_left > 0:
        timer_display.config(text=f"Time Left: {time_left}")
        time_left -= 1
        root.after(1000, countdown)
    elif time_left == 0:
        running = False
        timer_display.config(text="AI thinking...")
        root.after(1500, send_to_ai)


def start():
    global time_left, running
    try:
        time_left = int(timer_entry.get())
    except ValueError:
        time_left = 30
    running = True
    countdown()


def clear():
    canvas.delete("all")
    draw_grid()


timer_display = tk.Label(
    root, text="30", font=("Arial", 20), bg="#2b1d14", fg="#f3e1b5"
)
timer_display.pack(pady=5)

timer_entry = tk.Entry(root, font=("Arial", 12), width=5, justify="center")
timer_entry.insert(0, "30")
timer_entry.pack(pady=2)

tk.Button(
    root,
    text="Start Timer",
    command=start,
    bg="#d9a441",
    fg="black",
    font=("Arial", 11, "bold"),
).pack(pady=5)

slider_frame = tk.Frame(root, bg="#2b1d14")
slider_frame.pack(pady=5)

red = tk.Scale(
    slider_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="R",
    command=update_color,
    bg="#2b1d14",
    fg="white",
    highlightthickness=0,
)
green = tk.Scale(
    slider_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="G",
    command=update_color,
    bg="#2b1d14",
    fg="white",
    highlightthickness=0,
)
blue = tk.Scale(
    slider_frame,
    from_=0,
    to=255,
    orient="horizontal",
    label="B",
    command=update_color,
    bg="#2b1d14",
    fg="white",
    highlightthickness=0,
)

red.pack(side="left", padx=5)
green.pack(side="left", padx=5)
blue.pack(side="left", padx=5)

preview = tk.Frame(root, width=40, height=40, bg=color)
preview.pack(pady=5)
preview.pack_propagate(False)

tk.Button(
    root, text="Clear Canvas", command=clear, bg="#444444", fg="white", font=("Arial", 11)
).pack(pady=5)

draw_grid()
root.mainloop()