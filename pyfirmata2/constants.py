
# Message command bytes (0x80(128) to 0xFF(255)) - straight from Firmata.h
ANALOG_MESSAGE = 0xE0       # send data for an analog pin (or PWM)
DIGITAL_MESSAGE = 0x90      # send data for a digital pin
REPORT_ANALOG = 0xC0        # enable analog input by pin #
REPORT_DIGITAL = 0xD0       # enable digital input by port pair

START_SYSEX = 0xF0          # start a MIDI SysEx msg
SET_PIN_MODE = 0xF4         # set a pin to INPUT/OUTPUT/PWM/etc
SET_PIN_VALUE = 0xF5        # set digital pin value to 0/1
END_SYSEX = 0xF7            # end a MIDI SysEx msg
REPORT_VERSION = 0xF9       # report firmware version
SYSTEM_RESET = 0xFF         # reset from MIDI

# SysEx core features
EXTENDED_ID =0X00           # next two bytes are used to define the extended ID
                            # 0x01-0x0F reserved
ANALOG_MAPPING_QUERY = 0x69     # ask for mapping of analog to pin numbers
ANALOG_MAPPING_RESPONSE = 0x6A  # reply with mapping info
CAPABILITY_QUERY = 0x6B         # ask for supported modes and resolution of all pins
CAPABILITY_RESPONSE = 0x6C      # reply with supported modes and resolution
PIN_STATE_QUERY = 0x6D          # ask for a pin's current mode and value
PIN_STATE_RESPONSE = 0x6E       # reply with pin's current mode and value
EXTENDED_ANALOG = 0x6F          # analog write (PWM, Servo, etc) to any pin
STRING_DATA = 0x71          # a string message with 14-bits per char
REPORT_FIRMWARE = 0x79      # report name and version of the firmware
SAMPLING_INTERVAL = 0x7A    # set the poll rate of the main loop
SYSEX_NON_REALTIME = 0x7E   # MIDI Reserved for non-realtime messages
SYSEX_REALTIME = 0x7F       # MIDI Reserved for realtime messages

# SysEx optional features
SERIAL_DATA = 0X60
ENCODER_DATA = 0X61
ACCELSTEPPER_DATA = 0X62
SPI_DATA = 0X68
SERVO_CONFIG = 0X70
ONEWIRE_DATA = 0X73
DHTSENSOR_DATA = 0x74
SHIFT_DATA = 0x75           # a bitstream to/from a shift register
I2C_REQUEST = 0x76          # send an I2C read/write request
I2C_REPLY = 0x77            # a reply to an I2C read request
I2C_CONFIG = 0x78           # config I2C settings such as delay times and power pins

# Pin modes.
# except from UNAVAILABLE taken from Firmata.h
UNAVAILABLE = -1
INPUT = 0          # as defined in wiring.h
OUTPUT = 1         # as defined in wiring.h
ANALOG = 2         # analog pin in analogInput mode
PWM = 3            # digital pin in PWM output mode
SERVO = 4          # digital pin in SERVO mode
SERIAL = 10        # serial pin (Rx | Tx)
INPUT_PULLUP = 11  # Same as INPUT, but with the pin's internal pull-up resistor enabled

# Pin types
DIGITAL = OUTPUT   # same as OUTPUT below
# ANALOG is already defined above

# Time to wait after initializing serial, used in Board.__init__
BOARD_SETUP_WAIT_TIME = 2

##################
#     SERIAL     #
##################

# See https://github.com/firmata/protocol/blob/master/serial-1.0.md for more info
# SysEx command byte
SERIAL_DATA = 0X60

# Command bytes (add port descriptor f.e. Config HW_serial1 -> 0x11)
SERIAL_CONFIG   = 0x10
SERIAL_WRITE    = 0x20
SERIAL_READ     = 0x30
SERIAL_REPLY    = 0x40
SERIAL_CLOSE    = 0x50
SERIAL_FLUSH    = 0x60
SERIAL_LISTEN   = 0x70

# Serial port descriptor
HW_SERIAL0 = 0x00
HW_SERIAL1 = 0x01
HW_SERIAL2 = 0x02
HW_SERIAL3 = 0x03

SW_SERIAL0 = 0x08
SW_SERIAL1 = 0x09
SW_SERIAL2 = 0x0A
SW_SERIAL3 = 0x0B

# serial capable pin
PIN_MODE_SERIAL = 0x0A

# Capability response
# Where the pin mode = "Serial" and the pin resolution = one of the following:
RES_RX0 = 0x00
RES_TX0 = 0x01
RES_RX1 = 0x02
RES_TX1 = 0x03
RES_RX2 = 0x04
RES_TX2 = 0x05
RES_RX3 = 0x06
RES_TX3 = 0x07
# extensible up to 8 HW ports