from .constants import *

class MissingPinDefinitionError(Exception):
    pass

class Serial(object):
    """ Object for serial port handling. """
    def __init__(self, board, port) -> None:
        self._board = board
        self._port = port
        self._buff = []

    def start(self, baudRate=115200, rx=None, tx=None) -> None:
        """ Sends config and starts continous read """
        self.config(baudRate, rx, tx)
        self.read(True) # start continous reading

    def config(self, baudRate=115200, rx=None, tx=None) -> None:
        """ Send Config message """
        self._baudRate = baudRate
        command = SERIAL_CONFIG + self._port
        mask = 0b1111111
        msg = [command]
        baud = [baudRate & mask, (baudRate >> 7) & mask, (baudRate >> 14) & mask]
        msg.extend(baud)
        if rx==None and tx==None:
            pass    # Nothing more to be done
        elif rx!=None & tx!=None:
            msg.append(rx)
            msg.append(tx)
        else:   # Just one pin defined
            raise MissingPinDefinitionError("Both Rx and Tx pins must be specified")
        msg = bytearray(msg)
        self._board.send_sysex(SERIAL_DATA, msg)

    def write(self, data:bytearray):
        """ Send data thru serial port """
        command = SERIAL_WRITE + self._port
        mask = 0b1111111
        msg = [command]
        for d in data:
            d_l = d & mask
            d_h = (d >> 7)
            msg.append(d_l)
            msg.append(d_h)
        msg = bytearray(msg)
        self._board.send_sysex(SERIAL_DATA, msg)

    def read(self, continous:bool, maxBytesToRead = None):
        """ Read bytes of data from serial port """
        command = SERIAL_READ + self._port
        mask = 0b1111111
        msg = [command]
        msg.append(0x00 if continous is True else 0x01)
        if maxBytesToRead is not None:
            d_l = maxBytesToRead & mask
            d_h = (maxBytesToRead >> 7)
            msg.append(d_l)
            msg.append(d_h)
        msg = bytearray(msg)
        self._board.send_sysex(SERIAL_DATA, msg)

    def close(self) -> None:
        """ Closes port. Should not be called directly (pins would still be marked as taken) """
        command = SERIAL_CLOSE + self._port
        msg = [command]
        msg = bytearray(msg)
        self._board.send_sysex(SERIAL_DATA, msg)

    def readByte(self):
        """ Used to proccess incomming data """
        return self._buff.pop(0)
    
    def readBytes(self, bytesToRead:int) -> bytes:
        buff = []
        for i in range(bytesToRead):
            buff.append(self.readByte())
        return buff
    
    def available(self) -> int:
        return len(self._buff)
