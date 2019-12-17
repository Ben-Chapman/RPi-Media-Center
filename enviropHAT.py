import time
from envirophat import light, motion, weather, leds

try:
    while True:
        lux = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ', '')
        leds.off()
        accel = str(motion.accelerometer())[1:-1].replace(' ', '')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
        print(
            "Lux: {}
            RGB: {}
            Accelerometer: {}
            Heading: {}
            Temp C: {}
            Pressure hPa: {}".format(
                str(lux),
                rgb
                accel,
                str(heading),
                temp,
                press,
            ))

        time.sleep(0.5)

except KeyboardInterrupt:
    leds.off()
