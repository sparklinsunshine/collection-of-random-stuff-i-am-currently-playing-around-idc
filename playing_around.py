# import pyfirmata2
# import time
# import sys

# def setup_arduino(port='COM4'):
#     """
#     Initialize the Arduino board and set up the LED pin
#     Returns the board and LED pin objects
#     """
#     try:
#         # Connect to Arduino board
#         board = pyfirmata2.Arduino(port)
#         print(f"Successfully connected to Arduino on {port}")
        
#         # Start iterator thread to prevent buffer overflow
#         it = pyfirmata2.util.Iterator(board)
#         it.start()
        
#         # Configure pin 13 (built-in LED) as output
#         led_pin = board.digital[13]
#         led_pin.mode = pyfirmata2.OUTPUT
        
#         return board, led_pin
    
#     except Exception as e:
#         print(f"Error setting up Arduino: {str(e)}")
#         sys.exit(1)

# def blink_led(board, led_pin, on_time=5, off_time=5):
#     """
#     Main loop to blink the LED with specified on and off times
#     """
#     try:
#         while True:
#             # Turn LED on
#             led_pin.write(1)
#             print("LED ON")
#             time.sleep(on_time)
            
#             # Turn LED off
#             led_pin.write(0)
#             print("LED OFF")
#             time.sleep(off_time)
            
#     except KeyboardInterrupt:
#         print("\nProgram terminated by user")
#     except Exception as e:
#         print(f"Error during operation: {str(e)}")
#     finally:
#         # Clean up and exit
#         board.exit()
#         print("Arduino connection closed")

# if __name__ == "__main__":
#     # Set up the Arduino and start blinking
#     board, led_pin = setup_arduino()
#     blink_led(board, led_pin)

import pyfirmata2
import time
import sys

def setup_arduino(port='COM4'):
    """
    Initialize the Arduino with both LED and button functionality.
    We'll use digital pin 2 for the button instead of pin 10, as pin 2
    has more reliable interrupt capabilities on most Arduino boards.
    """
    try:
        # First establish the connection we know works
        print("Connecting to Arduino...")
        board = pyfirmata2.Arduino(port)
        print("Connected successfully!")
        
        # Set up the LED - we know this part works
        print("Setting up LED on pin 13...")
        led = board.get_pin('d:13:o')
        
        # Set up our button on pin 2
        print("Setting up button on pin 2...")
        button = board.get_pin('d:2:i')
        
        # Start the iterator - this is crucial for reading inputs
        print("Starting Arduino communication handler...")
        it = pyfirmata2.util.Iterator(board)
        it.start()
        
        # Give the board a moment to initialize
        print("Waiting for initialization...")
        time.sleep(2)
        
        return board, led, button
        
    except Exception as e:
        print(f"Setup error: {str(e)}")
        sys.exit(1)

def run_led_button_test(board, led, button):
    """
    Run a continuous test of the LED and button functionality.
    """
    try:
        print("\nStarting button test...")
        print("Press the button to turn on the LED")
        print("Press Ctrl+C to exit")
        
        while True:
            # Read the button state
            button_state = button.read()
            
            # Update LED based on button state
            if button_state is True:  # Button is pressed
                led.write(1)  # Turn LED on
                print("Button pressed - LED ON")
            else:
                led.write(0)  # Turn LED off
            
            # Small delay to prevent overwhelming the serial connection
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nTest ended by user")
    finally:
        # Clean up
        led.write(0)  # Make sure LED is off
        board.exit()
        print("Arduino connection closed")

if __name__ == "__main__":
    # Start the program
    print("=== Arduino Button and LED Test Program ===")
    print("This program will turn on the LED when you press the button")
    print("\nFirst, check your circuit:")
    print("1. LED: Built-in LED on pin 13 will be used")
    print("2. Button: Connect between pin 2 and GND")
    print("   - One leg of button to pin 2")
    print("   - Other leg to GND (ground)")
    
    input("\nPress Enter when your circuit is ready...")
    
    # Set up the Arduino
    board, led, button = setup_arduino()
    
    # Run the test
    run_led_button_test(board, led, button)