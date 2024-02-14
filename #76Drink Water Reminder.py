from plyer import notification
import time

title = 'Drink water my friend'
message = 'Trying to be cactus?(drink water)'
for i in range(4):
    notification.notify(
        title = title,
        message=message,
    )
    time.sleep(5)

# import pywhatkit as kit
# import time

# number = "+91"
# msg = "Heelllloooooo"
# for i in range(5):
#     kit.sendwhatmsg(number, msg, 12, 5)
#     time.sleep(12)