#!/usr/bin/env python

# Shakespearean insult generator
# written by tony baldwin | https://tonybaldwin.info
# released according to GPLv3

import sys
from Tkinter import *

from random import randint

root = Tk()


def speak() :
	a = ("artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish", "dankish", "dissembling", "droning", "errant", "fawning", "foul", "fobbing", "froward", "frothy", "fusty", "gleeking", "goatish", "gorbellied", "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "mammering", "mangled", "mewling", "naughty", "paunchy", "pribbling", "puking", "deboshed", "puny", "qualling", "rank", "reeky", "roguish", "ruttish", "saucy", "spleeny", "spongy", "surly", "tottering", "unmuzzled", "vain", "venomed", "villainous", "warped", "wayward", "weedy", "yeasty", "cullionly", "fusty", "caluminous", "wimpled", "burly-boned", "misbegotten", "odiferous", "poisonous", "fishified", "wart-necked") # 64 items

	a1 = randint(0,63)
	a2 = a[a1]


	b = ("base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "deformed", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-griping", "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle", "headed", "ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered", "mocking", "motley-minded", "onion-eyed", "plume-plucked", "sodden-witted", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne", "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad", "spotted", "unchin-snouted", "weather-bitten", " whoreson", "malmsey-nosed", "rampallian", "lily", "livered", "scurvy-valiant", "brazen-faced", "unwash'd", "bunch-back'd", "leaden-footed", "muddy-mettled", "pigeon-liver'd", "scale-sided") # 65 items

	b1 = randint(0,64)
	b2 = b[b1]


	c = ("apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon", "drudge", "flax-wench", "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "joithead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow", "miscreant", "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane", "scut", "skainsmate", "strumpet", "varlot", "vassal", "whey-face", "wagtail", "knave", "blind-worm", "popinjay", "scullian", "jolt-head", " malcontent", "devil-monk", "toad", "rascal", "basket-cockle") # 61 items

	c1 = randint(0,60)
	c2 = c[c1]
	t1.insert(END, "Thou " + a2 + ", " + b2 + " " + c2 + "!\n")


t2 = Button(text="Speak, Fool!", fg="black", command=speak)

t3 = Button(text="Yield", fg="red", command=quit)
t2.pack(fill=X, side=TOP); 
t3.pack(fill=X, side=TOP)
t1 = Text(root, bg="white", width=60)
t1.pack(fill=BOTH, expand=1)	


mainloop()

# This program was written by anthony baldwin - tonytraductor@linguasos.org 
# This program is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation; either version 2 of the License, or 
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
