print('Ryan Tolentino')
print('Assignment 6')
class Television:
    def __init__(self):
        self._powerOn = False
        self._muted = False
        self._volume = 5
        self._channel = 7
        self._prevChan = 2
    def __str__(self):
        return 'Power is On: '+str(self._powerOn)+'  Muted is :   '+str(self._muted)
        
    def togglePower(self):
        self._powerOn=not self._powerOn
    def toggleMute(self):
        if self._powerOn:
            self._muted=not self._muted

    def volumeUp(self):
        if self._powerOn:
            if self._volume<10:
                self._volume+=1
            self._muted=False
            return self._volume
    def channelUp(self):
        if self._powerOn:
            self._prevChan = self._channel
            if self._channel == 99:
                self._channel = 2
            else:
                self._channel += 1
            return self._channel
    #Channel is set to number.
    def setChannel(self, number):
        if self._powerOn:
            if 2 <= number <= 99: 
                self._prevChan = self._channel
                self._channel = number
            return self._channel
#Flip to previous channel.
    def jumpPrevChannel(self):
        if self._powerOn:
            incoming = self._channel
            self._channel = self._prevChan
            self._prevChan = incoming
            return self._channel
    
