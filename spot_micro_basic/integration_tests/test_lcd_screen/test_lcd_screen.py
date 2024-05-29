#!/home/pi/spotmicroai/venv/bin/python3 -u

from spotmicroai.lcd_screen_controller import LCD_16x2_I2C_driver
from spotmicroai.utilities.log import Logger
from spotmicroai.utilities.config import Config
import time

log = Logger().setup_logger('Test LCD Screen')

log.info('Testing LCD screen...')

i2c_address = Config().get('lcd_screen_controller[0].lcd_screen[0].address')

log.info('Use the command "i2cdetect -y 1" to list your i2c devices connected and')
log.info('write your lcd screen i2c address in your configuration file ~/spotmicroai.json')
log.info('Current configuration value is: ' + str(i2c_address))
input("Press Enter to start the tests...")

lcd_screen = LCD_16x2_I2C_driver.lcd(address=int(i2c_address, 0))


def test_0():
    log.info('Test0')

    lcd_screen.lcd_clear()

    lcd_screen.backlight(0)
    time.sleep(1)
    lcd_screen.backlight(1)
    time.sleep(1)


def test_1():
    log.info('Test1')

    lcd_screen.lcd_clear()
    lcd_screen.lcd_display_string("1234567890123456", 1)
    lcd_screen.lcd_display_string("1234567890123456", 2)

    time.sleep(2)


def test_2():
    log.info('Test2')

    lcd_screen.lcd_clear()

    fontdata1 = [
        [0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10],
        [0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00],
        [0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01],
        [0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00],
        [0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00],
        [0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00],
        [0x1f, 0x0, 0x4, 0xe, 0x0, 0x1f, 0x1f, 0x1f],
    ]

    lcd_screen.lcd_load_custom_chars(fontdata1)

    # Write first three chars to row 1 directly
    lcd_screen.lcd_write(0x80)
    lcd_screen.lcd_write_char(0)
    lcd_screen.lcd_write_char(1)
    lcd_screen.lcd_write_char(2)

    # Write next three chars to row 2 directly
    lcd_screen.lcd_write(0xC0)
    lcd_screen.lcd_write_char(3)
    lcd_screen.lcd_write_char(4)
    lcd_screen.lcd_write_char(5)

    time.sleep(1)

    for x in range(0, 14):
        lcd_screen.lcd_clear()
        lcd_screen.lcd_display_string_pos(chr(0), 1, x)
        lcd_screen.lcd_display_string_pos(chr(1), 1, x + 1)
        lcd_screen.lcd_display_string_pos(chr(2), 1, x + 2)
        lcd_screen.lcd_display_string_pos(chr(3), 2, x)
        lcd_screen.lcd_display_string_pos(chr(4), 2, x + 1)
        lcd_screen.lcd_display_string_pos(chr(5), 2, x + 2)
        time.sleep(0.5)


def test_3():
    log.info('Test3')

    lcd_screen.lcd_clear()

    lcd_screen.lcd_display_string_pos("Testing", 1, 1)  # row 1, column 1
    time.sleep(1)
    lcd_screen.lcd_display_string_pos("Testing", 2, 3)  # row 2, column 3
    time.sleep(1)


def test_4():
    fontdata2 = [
        # Char 0 - left arrow
        [0x1, 0x3, 0x7, 0xf, 0xf, 0x7, 0x3, 0x1],
        # Char 1 - left one bar
        [0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10],
        # Char 2 - left two bars
        [0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18],
        # Char 3 - left 3 bars
        [0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c, 0x1c],
        # Char 4 - left 4 bars
        [0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e],
        # Char 5 - left start
        [0x0, 0x1, 0x3, 0x7, 0xf, 0x1f, 0x1f, 0x1f],
    ]

    lcd_screen.lcd_load_custom_chars(fontdata2)

    block = chr(255)  # block character, built-in

    # display two blocks in columns 5 and 6 (i.e. AFTER pos. 4) in row 1
    # first draw two blocks on 5th column (cols 5 and 6), starts from 0
    lcd_screen.lcd_display_string_pos(block, 1, 0)

    for pos in range(0, 16):
        lcd_screen.lcd_display_string_pos(chr(1), 1, pos)
        lcd_screen.lcd_display_string_pos(chr(1), 2, pos)
        time.sleep(0.1)

        lcd_screen.lcd_display_string_pos(chr(2), 1, pos)
        lcd_screen.lcd_display_string_pos(chr(2), 2, pos)
        time.sleep(0.1)

        lcd_screen.lcd_display_string_pos(chr(3), 1, pos)
        lcd_screen.lcd_display_string_pos(chr(3), 2, pos)
        time.sleep(0.1)

        lcd_screen.lcd_display_string_pos(chr(4), 1, pos)
        lcd_screen.lcd_display_string_pos(chr(4), 2, pos)
        time.sleep(0.1)

        lcd_screen.lcd_display_string_pos(block, 1, pos)
        lcd_screen.lcd_display_string_pos(block, 2, pos)
        time.sleep(0.1)


def test_5():
    block = chr(255)  # block character, built-in

    lcd_screen.lcd_display_string_pos(block * 16, 1, 0)
    lcd_screen.lcd_display_string_pos(block * 16, 2, 0)


test_0()
test_1()
test_2()
test_3()
test_4()
test_5()
