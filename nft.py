import random
from PIL import Image

eyes = [
    r"./eyes/blue_red.png",
    r"./eyes/blue_turq.png",
    r"./eyes/brown.png"

]
pipes = [
    r"./Pipes/navyPipe.png",
    r"./Pipes/bluePipe.png",
    r"./Pipes/greenPipe.png",
    r"./Pipes/blackPipe.png"
 


]
shirts = [
    r"./Shirts/blueRed.png",
    r"./Shirts/brownBlack.png",
    r"./Shirts/greenBlack.png"
]
Skins = [
    r"./Skin_Color/green.png",
    r"./Skin_Color/light_brown.png",
    r"./Skin_Color/navy_blue.png"
]
Hats = [
    r"./TopHats/black_mohawk.png",
    r"./TopHats/turquise_mohawk.png",
    r"./TopHats/blue_mohawk.png"

]

eye = random.choices(eyes)[0]
pipe = random.choices(pipes)[0]
shirt = random.choices(shirts)[0]
Hat = random.choices(Hats)[0]
Skin = random.choices(Skins)[0]

img1 = Image.open(Skin)
img2 = Image.open(pipe)
img3 = Image.open(shirt)
img4 = Image.open(eye)
img5 = Image.open(Hat)

first = Image.alpha_composite(img1,img2)
second = Image.alpha_composite(first,img3)
third = Image.alpha_composite(second,img4)
last = Image.alpha_composite(third,img5)

last.save('chris.png')


