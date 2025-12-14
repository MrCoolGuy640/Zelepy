import time
from zelepy.events import ZelesisClient


def on_detection(event):
    print(f"[DETECTION] {event}")


def on_triggerbot(event):
    print(f"[TRIGGERBOT] {event}")


def on_any_event(event):
    event_type = event.get("event", "unknown")
    print(f"[{event_type.upper()}] {event}")


def main():
    # make a instance of the client
    client = ZelesisClient()
    
    # subscribe to specific events like detection or triggerbot
    client.subscribe("detection", on_detection)
    client.subscribe("triggerbot", on_triggerbot)
    
    # add a general listener for all events (this will fire for ALL events regardless of the type)
    client.add_event_listener(on_any_event)
    
    try:
        # start the client or else it wont work
        client.start()
        
        # run forever
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # stop the client when finished using it
        client.stop()


if __name__ == "__main__":
    main()
