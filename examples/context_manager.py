import time
from zelepy.events import ZelesisClient


def main():
    try:
        # You can use the client like a context manager
        # when doing so, it will automatically start when entering and stop when exiting
        with ZelesisClient() as client:
            print(f"Client is running: {client.is_running}")
            
            # example for sending a mouse move command
            print("Sending mouse move command...")
            client.move_mouse(10, 10)
            
            time.sleep(0.5)
            
            # example for subscribing to events while in context
            def on_detection(event):
                print(f"[DETECTION] {event}")
            
            client.subscribe("detection", on_detection)
            
            time.sleep(5)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
