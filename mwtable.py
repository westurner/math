#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'mwtable.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart mwtable.py")

#!/bin/sh
"""
mw table to lists
"""
t="""
{| class="wikitable" style="width: 500px"
|-
_ip.system(" 0 !! 1 !! 2 !! 3 !! 4 !! 5 !! 6 !! 7 !! 8 !! 9 !! 10 !! 11 !! 12")
|-
_ip.system(" E")
| F || F{{music|sharp}} || G || A{{music|flat}} || A || B{{music|flat}} || B || C || C{{music|sharp}} || D || E{{music|flat}} || E
|-
_ip.system(" B")
| C || C{{music|sharp}} || D || E{{music|flat}} || E || F || F{{music|sharp}} || G || A{{music|flat}} || A || B{{music|flat}} || B
|-
_ip.system(" G")
| A{{music|flat}} || A || B{{music|flat}} || B || C || C{{music|sharp}} || D || E{{music|flat}} || E || F || F{{music|sharp}} || G
|-
_ip.system(" D")
| E{{music|flat}} || E || F || F{{music|sharp}} || G || A{{music|flat}} || A || B{{music|flat}} || B || C || C{{music|sharp}} || D
|-
_ip.system(" A")
| B{{music|flat}} || B || C || C{{music|sharp}} || D || E{{music|flat}} || E || F || F{{music|sharp}} || G || A{{music|flat}} || A
|-
_ip.system(" E")
| F || F{{music|sharp}} || G || A{{music|flat}} || A || B{{music|flat}} || B || C || C{{music|sharp}} || D || E{{music|flat}} || E
|}"""
tl=t.split('\n')
tl
t[2::2]
t[2:]
print t[2:]
print t[2::1]
print t[2::0]
print t[2::2]
t
len(t)
tl
print tl[2::2]
print '\n'.join(tl[2::2])
print '\n'.join(tl[2::1])
print '\n'.join(tl[1::2])
tl
tl[4]
print '\n'.join(tl[5::2])
print '\n'.join(tl[5::1])
print '\n'.join(tl[5::])
print '\n'.join(tl[5:])
l=tl[6]
l
fl=l.split('||')
fl
fl=l.lstrip('|').split('||')
fl
fl=(x.strip() for x in l.lstrip('|').split('||'))
fl
list(fl)
list(fl)
_34
l=_34
l
l[::2]
l
fl=l
parse_f = lambda f: len(f)>1 and (f[1].startswith('{{music|') and f.endswith('}}') and f.split('{{')[1].split('}})[0].split('|')) or f
parse_f = lambda f: len(f)>1 and (f[1].startswith('{{music|') and f.endswith('}}') and f.split('{{')[1].split('}}')[0].split('|')) or f
map(parse_f, fl)
parse_f = lambda f: len(f)>1 and (f[1].startswith('{{music|') and f.endswith('}}') and f[1:].split('{{')[1].split('}}')[0].split('|')) or f
map(parse_f, fl)
parse_f('asd')
parse_f('A{{music|flat}}')
parse_f = lambda f: (len(f)>1 and f[1].startswith('{{music|') and f.endswith('}}') and f[1:].split('{{')[1].split('}}')[0].split('|')) or f
parse_f('A{{music|flat}}')
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and f[1:].split('{{')[1].split('}}')[0].split('|')) or f
parse_f('A{{music|flat}}')
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and (f[1], f[1:].split('{{')[1].split('}}')[0].split('|'))) or f
parse_f('A{{music|flat}}')
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and (f[0], f[1:].split('{{')[1].split('}}')[0].split('|'))) or f
parse_f('A{{music|flat}}')
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and (f[0], (f[1:].split('{{')[1].split('}}')[0].split('|'),))) or f
parse_f('A{{music|flat}}')
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and (f[0], tuple(f[1:].split('{{')[1].split('}}')[0].split('|'),))) or f
parse_f('A{{music|flat}}')
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and tuple(f[0], f[1:].split('{{')[1].split('}}')[0].split('|'),))) or f
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and tuple(f[0], f[1:].split('{{')[1].split('}}')[0].split('|')))) or f
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and tuple(f[0], f[1:].split('{{')[1].split('}}')[0].split('|'))) or f
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and tuple(f[0], f[1:].split('{{')[1].split('}}')[0].split('|')))) or f
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and tuple(f[0], f[1:].split('{{')[1].split('}}')[0].split('|'))) or f
parse_f('A{{music|flat}}')
parse_f = lambda f: (len(f)>1 and f[1:].startswith('{{music|') and f.endswith('}}') and (f[0], f[1:].split('{{')[1].split('}}')[0].split('|'))) or f
parse_f('A{{music|flat}}')
map(parse_f, fl)
l=_34
l
tl
map(str,tl)
tl
t
t="""{{Other uses}}
{{pp-semi-indef}}
{{Pp-move-indef}}
{{Infobox instrument
|name=Guitar
|names=
|image=guitar_1.jpg
|image_capt=A [[classical guitar|classical guitar (nylon string)]]
|background=string
|classification=[[String instrument]] (plucked, nylon-stringed guitars usually played with fingerpicking, and steel-, etc. usually with a [[Guitar pick|pick]].)
|hornbostel_sachs=321.322
|hornbostel_sachs_desc=Composite [[chordophone]]
|range= [[Image:Range guitar.svg|130px|center]]<div class="center">(a standard tuned guitar)</div>
|related=*[[Bowed string instrument|Bowed]] and [[plucked string instrument|plucked]] string instruments
|articles=
}}
The '''guitar''' is a [[plucked string instrument]], usually played with fingers or a [[guitar pick|pick]]. The guitar consists of a body with a rigid neck to which the strings, generally six in number, are attached. Guitars are traditionally constructed of various woods and strung with animal gut or, more recently, with either nylon or steel strings. Some modern guitars are made of [[polycarbonate]] materials. Guitars are made and repaired by [[luthier]]s. There are two primary families of guitars: acoustic and electric.
[[Acoustic guitar]]s (and similar instruments) with hollow bodies have been in use for over a thousand years. There are three main types of modern acoustic guitar: the [[classical guitar]] (nylon-string guitar), the [[steel-string acoustic guitar]], and the [[archtop guitar]]. The tone of an acoustic guitar is produced by the vibration of the strings, which is amplified by the body of the guitar, which acts as a resonating chamber. The classical guitar is often played as a [[solo (music)|solo]] instrument using a comprehensive [[fingerpicking]] technique.
[[Electric guitar]]s, introduced in the 1930s, rely on an [[amplifier]] that can electronically manipulate tone. Early amplified guitars employed a hollow body, but a solid body was found more suitable. Electric guitars have had a continuing profound influence on [[popular culture]]. Guitars are recognized as a primary instrument in genres such as [[blues]], [[Bluegrass music|bluegrass]], [[country music|country]], [[flamenco]], [[jazz]], [[jota (music)|jota]], [[mariachi]], [[heavy metal music|metal]], [[reggae]], [[rock music|rock]], [[Soul music|soul]], and many forms of [[pop music|pop]].
==History==
{{Main|History of the classical guitar}}
[[Image:Guitar-like plucked instrument, Carolingian Psalter, 9th century manuscript.jpg|thumb|right|Illustration from a [[Carolingian]] [[Psalter]] from the 9th century, showing a guitar-like plucked instrument.]]
Before the development of the electric guitar and the use of synthetic materials, a guitar was defined as being an instrument having "a long, fretted neck, flat wooden soundboard, ribs, and a flat back, most often with incurved sides".<ref>Kasha, Dr. Michael (August 1968). "A New Look at The History of the Classic Guitar". ''Guitar Review'' 30,3-12</ref> The term is used to refer to a number of related instruments that were developed and used across Europe beginning in the 12th century and, later, in the Americas.<ref>Wade, Graham ''A Concise History of the Classic Guitar'' Mel Publications, 2001</ref> These instruments are descended from ones that existed in ancient [[ancient India and Central Asia|central Asia and India]]. For this reason guitars are distantly related to modern instruments from these regions, including the [[tanbur]], the [[setar]], and the [[sitar]]. The oldest known iconographic representation of an instrument displaying the essential features of a guitar is a 3,300&nbsp;year old stone carving of a [[Hittites|Hittite]] bard.<ref>Dr. Michael Kasha, "A New Look at The History of the Classic Guitar", Guitar Review 30, August 1968, pp.3-12.</ref>
The modern word ''guitar'', and its antecedents, have been applied to a wide variety of cordophones since ancient times and as such is the cause of confusion. The English word ''guitar'', the German ''{{lang|de|gitarre}}'', and the French ''{{lang|fr|guitare}}'' were adopted from the Spanish ''{{lang|es|guitarra}
Although the wor
Two medieval ins
The Spanish [[vihuela]] or (in I
==Type
[[Image:Jan Vermeer
Guitars can be divided into two broad categories, acoustic and ele
===Acoustic guitars===
{{main|Acoustic guitar}}
There are several notable subcategories within the acoustic guitar group: classical and [[flamenco guitar]]s; steel-string guitars, which include the flat-t
====Renaissance and Baroque guitars====
{{main|
:These are the gracile ancestors of the modern [[classical guitar]]. They are substantially smaller and more delicate than the classical guitar, and generate a much quieter sound. The strings are paired in courses 
====Classical guitars====
{{main|Classical guitar}}
[[File:Agustin Barrios.gif|thumb|Eminent South American guitarist, [[Agustin Barrios]]]]
:These are typically strung with nylon strings, plucked with the fingers, played in a seated position and are used to play a diversity of musical styles including [[European classical music|classical music]]. The classical guitar's wide, flat neck allows the musician to play scales, arpeggios, and certain chord forms more easily and with less adjacent string interference than on other 
====Extended-range classical guitars====
{{main|Extended-range classical guitar}}
:An Extended-range classical guitar is a classical guitar with more than 6 strings, usually up to 13.
====Flamenco guitars====
{{main|Flamenco guitar}}
:The flamenco guitar is similar to the classical guitar, but of lighter construction, with a cypress body and spruce top. Tuning pegs like those of a violin are traditional, although many modern [[flamenco]] guitars have machine heads. A distinguishing feature of all flamenco guitars is the tapping plates (''golpeadores'') g
====Flat-top (steel-string) guitars====
[[File:Bernd Voss - Copito Blues guitar.ogv|thumb|A guitarist playing a blues tune on a semi-acoustic guitar]]
{{main|Steel-string acoustic guitar}}
:Similar to the [[classical guitar]], however, within the varied sizes of the steel-stringed guitar the body size is usually significantly larger than a classical guitar, and has a narrower, reinf
====Archtop guitars====
{{main|Archtop guitar}}
:These are steel-string instruments in which the top (and often the back) of the instrument are carved from a solid billet in a curved rather than a flat shape; this violin-like construction is usually credited to the American [[Orville Gibson]] (1856-1918). [[Lloyd Loar]] of the [[Gibson Guitar Corporation|Gibson Mandolin-Guitar Mfg. Co]] introduced the violin-inspired f-hole design now usually associated with archtop guitars, after designing a style of [[mandolin]] of the same type. The typical archtop guitar has a large, deep, hollow body whose form is much like that of a mandolin or violin family instrument. Nowadays, most archtops are equipped with magnetic pickups and are therefore both acoustic and electric. F-hole archtop guitars were immediately adopted upon their release by both [[jazz]] and [[country music|country]] musicians and have remained particularly popular in jazz music, usually with flatwound strings.
====Selmer-Maccaferri guitars====
:These are usually played by those who follow the style of [[Django Reinhardt]]. It is an unusual-looking instrument, distinguished by a fairly large body with squarish bouts, and either a "D"-shaped or longitudinal oval soundhole. The strings are gathered at the tail like an archtop guitar, but the top is formed from thin spruce (like a flat-top or classical) forced into a shallow dome. It also has a wide fingerb
[[Image:JMT8stringguitar.jpg|right|thumb|thumb|An 8-string [[baritone guitar|baritone]] tricone [[resonator guitar]].]]
====Resonator, resophonic or Dobro guitars====
{{main|Resonator guitar|Dobro}}
:All three principal types of resonator guitars were invented by the Slovak-American [[John Dopyera]] (1893-1988) for the National a
====Twelve-strin
{{main|Twelve-string guitar}}
:Th
====Ru
{{main|Russian guitar}}
:These seven-string acoustic guitars were the norm for Russian guitarists throughout t
====Acoustic bass guita
[[File:Bass-und-primgitarre.jpg|thumb|Prime and bass acoustic guitars]]
{{main|Acoustic bass guitar}}
:These have steel strings or gut strings and often the
c
d
a
.
bread
_ip.system("/bin/ls --color=auto ")
_ip.system("vim -g ./table.txt")
_ip.system("bash")
import mwlib
