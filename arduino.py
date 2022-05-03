import serial.tools.list_ports
PORT_NAME = 'puertos.txt'

def revisarArchivo():
    try:
        with open (PORT_NAME,'r',encoding='utf-8') as f:
            portCom = f.readline()
            print(portCom)
            f.close()
            return portCom
    except: 
        return ""

def escogerUnPuerto(arduino):
    ports = serial.tools.list_ports.comports()
    portList = []
    for port in ports:
        portList.append(str(port))
        print(str(port))
    portCom = 'COM'
    portCom += input('Escoga un puerto: COM')
    try:
        arduino.port = portCom
        arduino.open()
        with open(PORT_NAME,'w',encoding="utf-8") as f:
            f.write(portCom)
            f.close()
    except:
         print("No se pudo conectar al arduino")



def main():
    portCom = revisarArchivo()
    arduino = serial.Serial()
    arduino.baudrate = 9600
    if portCom != "":
        try:
            arduino.port = portCom
            arduino.open()
        except:
            escogerUnPuerto(arduino)
    else:
        escogerUnPuerto(arduino)
    
    datos = arduino.readline()
    print(datos.decode('utf-8').rstrip('\n'))
    arduino.close()


if __name__ == '__main__':
    main()
