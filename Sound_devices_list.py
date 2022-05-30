import sounddevice as sd 
for r in list(sd.query_devices()):
      print(r.get('name'))

