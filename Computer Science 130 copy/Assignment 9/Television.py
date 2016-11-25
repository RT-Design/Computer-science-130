#Ryan Toletino

class Television:
    def __init__(self):
        self._powerOn=False
        self._muted = False
        self._volume = 5
        self._channel = 2
        self._prevChan = 2

    def togglePower(self):
        self._powerOn = not self._powerOn

#Clicking flips between muted and unmuted.
    def toggleMute(self):
            if self._powerOn:
                self._muted = not self._muted

#volume can range from 1 upto including 10
    def volumeUp(self):
        if self._powerOn:
            if self._volume < 10:
                self._volume += 1
            self._muted = False
            return self._volume

#channel increases by one and wraps back to 2
        def channelUp(self):
            if self._powerOn:
                self._prevChan = self._channel
                if self._channel == 99:
                    self._channel = 2
                else:
                    self._channel += 1
                return self._channel

    
        
        
