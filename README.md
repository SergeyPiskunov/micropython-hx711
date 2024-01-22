# hx711-mpython
Micropython driver for the HX711 24-Bit Analog-to-Digital Converter

Latest version supports:
- retrieving data from the channel 'A' with gain 128 and 64, 
the channel 'B' with gain 32 in a raw form and a form 
converted from the two's complement.
- sending "power off" sequence to switch device to the power-saving mode.
- sending "power on" sequence with the gain saved before the "power off".
- checking if the device is ready for the data retrieval.

#### Example for the ESP8266:
Refer to the example folder. It can permorm tare and set a ratio to change the raw input.
D_OUT pin is connected to the GPIO 5<br/>
PD_SCK pin is connected to the GPIO 4<br/>
Using internal HX711 oscillator, so ESP8266's frequency is set to 160000000
 
```
from scales import Scales

scale = Scales(d_out=4, pd_sck=5)
scale.reset()
scale.tare()
while True:
    if scale.is_ready():
        val = scale.stable_value()
        print(val)
        sleep_us(500)

```
