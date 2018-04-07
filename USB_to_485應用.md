## USB to 485應用
### 以Modbus/RTU控制PLC為例

- 以下為程式範例, 主要由[這篇](https://github.com/maloyang/PLC-Python/blob/master/mb_demo1_mq.py)來的
- 使用的是ch340晶片的USB轉RS485的裝置，[請見連結](http://shop.cpu.com.tw/product/47556/info/)
- 插入USB設備後，會產生一個"/dev/ttyUSB0"的設備檔，因windows和linux下python程式都是相容的，因此我們只要把第19行改為"/dev/ttyUSB0"就可以了
    - 如果執行時有錯誤，應該是你沒安裝modbus-tk, serial這二個套件，可以安裝如下：
    - ```sudo pip install serial```
    - ```sudo pip install modbus-tk```
- 本來是在windows上的程式, 現在改為Linux環境執行, 感覺更穩定!

```
import paho.mqtt.client as mqtt  #import the client1
import time

import serial
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_rtu as modbus_rtu
import time

mbComPort = '/dev/ttyUSB0'   # ttyUSB0->RS-485
baudrate = 9600
databit = 8
parity = 'N'
stopbit = 1
mbTimeout = 100 # ms

def on_connect(client, userdata, flags, rc):
    m="Connected flags"+str(flags)+", result code "+str(rc)+", client_id  "+str(client)
    print(m)

    # first value OFF
    print('set light off!')
    control_light(0)
    client1.publish(topic,0)    

def on_message(client1, userdata, message):
    print("message received  "  ,str(message.payload.decode("utf-8")), message.topic, message.qos, message.retain)
    if message.topic == topic:
        print("set light: ", message.payload)
        if message.payload=='1' or message.payload==1:
            control_light(1)
        else:
            control_light(0)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def control_light(value):
    mb_port = serial.Serial(port=mbComPort, baudrate=baudrate, bytesize=databit, parity=parity, stopbits=stopbit)
    master = modbus_rtu.RtuMaster(mb_port)
    master.set_timeout(mbTimeout/1000.0)

    mbId = 1
    addr = 2 #base0

    try:
        #-- FC5: write multi-coils
        rr = master.execute(mbId, cst.WRITE_SINGLE_COIL, addr, output_value=value)
        print("Write(addr, value)=%s" %(str(rr)))

    except Exception, e:
        print("modbus test Error: " + str(e))

    master._do_close()


# some online free broker:
#   iot.eclipse.org
#   test.mosquitto.org
#   broker.hivemq.com
broker_address="iot.eclipse.org"
topic = "malo-iot/light"
client1 = mqtt.Client()    #create new instance
client1.on_connect = on_connect        #attach function to callback
client1.on_message = on_message        #attach function to callback
#client1.on_log=on_log

time.sleep(1)
client1.connect("iot.eclipse.org", 1883, 60)      #connect to broker
#client1.loop_start()    #start the loop
client1.subscribe(topic)

client1.loop_forever()
```
