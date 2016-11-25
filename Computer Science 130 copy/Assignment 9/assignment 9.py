#Ryan Tolentino
#python 2.7
#Assignment 9
#
print('Ryan Tolentino,''\n''Python 2.7,''\n''Assignment 9,')

class Television:
    def __init__(self):
        self._powerOn=False
        self._muted = False
        self._volume = 7
        self._channel = 66
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
            
        def getchannel(self):
            return self.channel


from Television import Television
class DeluxeTV(Television):
    """TV that maintains a set of favorite channels"""
    def __init__(self):
        """call the base class Television to initialize the DeluxeTV also"""
        Television.__init__(self)
        self._favorites = [ ]

    def addToFavorites(self):
        """Add current channel to favorites"""
        if self._powerOn and self._channel not in self._favorites:
            self._favorites.append(self._channel)

    def removeFromFavorites(self):
        """Remove current channel from favorites"""
        if self._powerOn and self._channel in self._favorites:
            self._favorites.remove(self._channel)

    def jumpToFavorite(self):
        """Jumps to next higher channel in favorites. If none higher then it wraps to lower and no favorites remains the same"""
        if self._powerOn and len(self._favorites) > 0:
            closest = max(self._favorites)
            if closest <= self._channel:
                closest = min(self._favorites)
            else:
                for option in self._favorites:
                    if self._channel < option < closest :
                        closest = option
            self.setChannel(closest)
            return closest

    unitTV = Television()
    unitTV.togglePower()
    
    print "Resulting state: ", unitTV
    unitTV2 = Television()
    unitTV2.togglePower()
    
    print "Resulting state: ", unitTV2

    MyTV= Television()
    MyTV.togglePower()
    print "My TV Channel Is 66 "
    print "My TV Volume Is 7 "
    print "My deluxTV Channel Is 77 "
    print "My deluxTV Volume Is 8 "
    
