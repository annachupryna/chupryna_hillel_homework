from Homework_10.Chain_1.Children.smartphone import *
from Homework_10.Chain_1.Children.dial_phone import *
from Homework_10.Chain_1.Children.button_phone import *

smartphone = Smartphone('iPhone', 2019, '12 Pro', 6.06, '2556×1179 pixels', 3)
print(smartphone.brand)
smartphone.call()
smartphone.charge()
smartphone.take_photo()

button_phone = ButtonPhone('Nokia', 2005, 'X5', '2G', 2)
print(button_phone.brand)
button_phone.call()
button_phone.play_radio()

dial_phone = DialPhone('Sangyn', 1960, 'Black 1', 11, '6 cm')
print(dial_phone.brand)
dial_phone.call()
