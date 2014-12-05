#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Geekman2
#
# Created:     22/11/2014
# Copyright:   (c) Geekman2 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from dragonfly.all import CompoundRule, Grammar, Key
import natlink
import time
import vlc
import os
import random

musdir = "C:/Users/Geekman2/Dropbox/Tessa and Devon/__Devon/"
ins = vlc.Instance()
player = ins.media_player_new()
playlist = os.listdir(musdir)
def addSong(file):
    media = ins.media_new(unicode(file))
    player.set_media(media)
    player.play()


class ExampleRule(CompoundRule):
    spec = "car"
    def _process_recognition(self,node,extras):
        print "Voice command spoken"

class PlayMusicRule(CompoundRule):
    spec = "Music Time"
    def _process_recognition(self,node,extras):
        song = random.choice(playlist)
        print song
        addSong(musdir+song)
class SkipRule(CompoundRule):
    spec = "Skip"
    def _process_recognition(self,node,extras):
        song = random.choice(playlist)
        print song
        addSong(musdir+song)
class StopRule(CompoundRule):
    spec = "Pause"
    def _process_recognition(self,node,extras):
        player.pause()
class ResumeRule(CompoundRule):
    spec = "Resume"
    def _process_recognition(self,node,extras):
        player.play()

class VolumeUp(CompoundRule):
    spec = "Volume Up"
    def _process_recognition(self,node,extras):
        a1 = Key("w-b,right,right,right,right,enter,up:20")
        a1.execute()

grammar = Grammar("Basic Grammar")
grammar.add_rule(PlayMusicRule())
grammar.add_rule(SkipRule())
grammar.add_rule(StopRule())
grammar.add_rule(ResumeRule())
grammar.add_rule(VolumeUp())

natlink.natConnect()
grammar.load()
print natlink.getMicState()
grammar.enable()
natlink.waitForSpeech()
natlink.natDisconnect()




