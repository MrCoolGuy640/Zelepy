import time
from zelepy.events import ZelesisClient

def main():
    # make a instance of the client
    client = ZelesisClient()
    
    try:
        # start the client or else it wont work
        client.start()
        
        
        # Example for moving the mouse in a square
        movements = [
            (100, 0),
            (0, 100),
            (-100, 0),
            (0, -100),
        ]
        
        for x, y in movements:
            print(f"Moving mouse to ({x}, {y})")
            client.move_mouse(x, y)
            time.sleep(0.5)

            
        # Example for clicking with the mouse
        for i in range(3):
            client.click_mouse()
            time.sleep(1)
        
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # stop the client when finished using it
        client.stop()
        print("Client stopped.")


if __name__ == "__main__":
    main()