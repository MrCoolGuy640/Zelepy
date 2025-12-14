# Zelepy
![PyPI](https://img.shields.io/pypi/v/zelepy)
![License](https://img.shields.io/github/license/mrcoolguy640/zelepy)

Zelepy is a Python wrapper for the [Zelesis Neo API](https://zelesis.com/), allowing you to communicate with the Zelesis Neo software from python

# Installation
```bash
pip install zelepy
```

# Features
- Configuration File API
- Listen for Neo Events over UDP
- Broadcast Neo Events over UDP

# Examples
## Zelesis Client
The Zelesis Client is used to broadcast or listen for events via UDP. It can be initialized via:
```py
from zelepy.events import ZelesisClient
client = ZelesisClient()
client.start()
```
Remember when you are finished with the client to run
```py
client.stop()
```