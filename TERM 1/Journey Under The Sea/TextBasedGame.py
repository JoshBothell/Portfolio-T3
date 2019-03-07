def choice(page1, page2):
    page1 = str(page1)
    page2 = str(page2)
    while True:
        choice = input("Enter either page " + page1 + " or page " + page2 + "\n")
        if choice == page1:
            return page1
        elif choice == page2:
            return page2
        else:
            print("Sorry that is not an option.")
            continue
            
    
def page1():
    print("""
       _                                     _    _           _            
      | |                                   | |  | |         | |           
      | | ___  _   _ _ __ _ __   ___ _   _  | |  | |_ __   __| | ___ _ __  
  _   | |/ _ \| | | | '__| '_ \ / _ \ | | | | |  | | '_ \ / _` |/ _ \ '__| 
 | |__| | (_) | |_| | |  | | | |  __/ |_| | | |__| | | | | (_| |  __/ |    
  \____/ \___/ \__,_|_|  |_| |_|\___|\__, |  \____/|_| |_|\__,_|\___|_|    
                                      __/ |                                
                                     |___/                                 
                 _______ _             _____                               
                |__   __| |           / ____|                              
                   | |  | |__   ___  | (___   ___  __ _                    
                   | |  | '_ \ / _ \  \___ \ / _ \/ _` |                   
                   | |  | | | |  __/  ____) |  __/ (_| |                   
                   |_|  |_| |_|\___| |_____/ \___|\__,_|                   
                                                                           
                                                                           
                 BY: R.A. MONTGOMERY
                 Adapted By: Hayden Whitney and Josh Bothell

                        Tip: To best view ascii art step back from the screen and look at it from a distance.
                """)
    input("...")
    page2()
def page2():
    print("""
                                                                                              `.`-/d
                                                                                             :/sNmdm
                                                                                            sNNmMyMm
                                                                                           +hmNMyomy
                                                                                          `o-- `   +
                                                                                          -        +
                                                                                                   +
                                                                                                `-oo
                                                                                                `+od
                                                                                                 ++y
                                                                                                -s+o
                                                                                              .yysod
....                        `+o+:.`.....-.`. `.`..`odm-`                                      -+.hdh
    ..`                     hs.so```..`-...-`...`./+/o `-.                                    .o`dNy
       ```                  o//:--:..-.-/yo-.-..`.---s`   `..                   `--       ./+.`+`yNy
          .`                hy: `      . .+o+/.``   -/--`    .``                +`.-      s:-:/..` +
            `.`             o:.:s-           `:o+::-`--./.     `.`             `s`.:      :`--`.   +
              .-            s .-:-               `.-/:hy- `.     /ho.           +-`-   `.`/:.:-:---o
                :`      .```y```                     ./ym/ -./ho+hhh-..`        s:./.-.:oyh++o:/-..+
         -`  `   -`    `/+s+/:o/.                        `/y: hMN`     .-.   ://y/:++:+s/omydNdo:::+
         ``ds`    -     :``/dd.-/`                         :: `+-        `-. `+mmMmymmmdyddmdho/-.-+
          dd/      :    .. -m/-:/.                         ss-sh+....       ./sss+soodhy+/+/:/yhhhdo
          o-.     `//``s+y++myhmhs+`..-/.                 -+. :dNdo+y      .-:+d.   .d- -/.   /yys++
           :/  ```.-.  `.o+os+//     `.`-.../:ds         `-.   `yNs/+o-  :yNdydhdNN+-o  +:y`  -+.s++
    `-----+:--.`           -s.              /+--        /d/      +do+oh:.NmmdmhsMMMNy+  +/.s+-/+o:o+
    +mmNNMMMMMNNNmdhyosoo++sssoooooooossshdhdds  .s:.-.:sh:-...``-+y:o/s.smdmmNsMMMm++:/oo/so+/o+so+
    -ooyhmNmddyho+-.```             ``....:ydNN:: +:       ``..`   `........--------...-.`.-.```   +
          `:hNNmNmNho-..-+/`  `-/+- `o+yoohNmm/:  /+`          `-                                  +
           `ydhhohNMMMNmNMNdohdNMMhoshMMNmMd:    `sNysshysyohhysyo+++//::-..---::-.-..--:o/---...--+
...``...`........--/+ymMNmmdddddmMNNNmho/:+--.    yMMMNmMNNmNMmmmNMMNmNNNmNmNmdmdddNNNNmmmNNmdddmmd+
                        ``.------..` `.....   -.`./MMMNNNdNmNmmNmNNNMmdmmmmmmNNNddmNNNmmmmNNNNmmmmh+
    .:o++oohoyshysoyyhhysyo:/+ooo+o++/o+/+:-  `//+sNMNNMMMNNNNdmmdmNmNmmdNNNNmNNmmNNNNMNmmMMNMMMNNy+
          `:/:-`.:////yy+ooyssohhhsyhso++:-..` ``     .-.::+oo+/:ooohhhmmmmNNmdmddhyoo:+ooos+//oy/-+
     ...-..`   `...-:-:/://+++/::--`...-.``` ```-.--.....-...::/::.----.```.:---/.`-/://--/oss+y///+
-`..``     `.-.:--....--.....:-..-.-//--/-:/::-.......-..```.. `.-::.  `--.-...:-::-:-.--::----`-:.+
                                            .....--..                                `..-...---..-.+
                                                                                                   +
                """)
    print("""
    You are an underwater explorer. You are leaving
to explore the deepest oceans. You must find
the lost city of Atlantis. This is your most challenging
assignment.
    It is morning and the sun pushes up on the
horizon. The sea is calm. You climb into the narrow
pilot's compartment of the underwater vessel
Seeker with your special gear. The crew of the
research vessel Maray screws down the hatch
clamps. Now begins the plunge into the depths of
the ocean. The Seeker crew begins lowering by a
strong, but thin cable. Within minutes, you are so
deep in the ocean that little light filters down to
you. The silence is eerie as the Seeker slips deeper
and deeper. You peer out the thick glass porthole
and see fish drifting past, sometimes stopping to
look at you—an intruder from another world.
                """)
    page3()
def page3():
    print("""
    Now the cable attaching you to Maray is extended
almost to its limit. You have come to rest on
a ledge near the canyon in the ocean floor that
supposedly leads to the lost city of Atlantis.
You have a special sea suit that will protect you
from the intense pressure of the deep if you choose
to walk about on the sea bottom. You can cut
loose from the cable if you wish because the
Seeker is self-propelled. You are now in another
world.
________________________________________

    If you decide to explore the ledge
where the Seeker has come to rest,
turn to page 6.

    If you decide to cut loose from
the Maray and dive with the Seeker
into the canyon in the ocean floor,
turn to page 5.
                """)
    choicex = choice(6, 5)
    if choicex == "6":
        page6()
    if choicex == "5":
        page5()
def page4():
    print("""
       `o-                               :+   +-                                       :`           
         +:                              -+  `+`                                    `-oo/----.``    
          s`                             -s` -s:                                    :sdyyshhs/:.  `.
          .s                             /y. -:.                                    sMMhsso+:.   `-`
           s.                            :y` +o                                   /mMMmmdh.     .:  
           .o-                          `//  o/                                .+dMMMNhsso/`  `-:.` 
            -s                          `+:  -/`                             ../NMMMMNhhs/+/.``-`   
             h+                         .//   /.                             -odMMMMMMmyyyddsyho:`..
             ym-                        `//  `y-                             -mMMMMMMmhosyyyddsh/-. 
             yNd//:-                    `:-  `+`                             sMMMMMMNmy:/ooddydy:-  
             oMmyys+:`                  `/`  `::                            `NMMMMMMMdyssyhysshy:   
            ++MMNNdsoo.                 `/.  `-+                           `:MMMMMMMMmysyhsyss+-    
.`         `yyNMMMNhos-`                ./-   -/`                         :+mMMMMMMMNhdmmso+-`    `.
-/         .hymMMMMmh+.                 -+`   +/-                         -+MMMMMMMMd+yo+o:      .-`
:h.        `yymMMMMNmo/:-.``            .+-   `/                        `.+dMMMMMMMN+s:./.     `:.  
:ss         osdMMMMMMyoosss/`           -s.   `-.                       .sNMMMNMMMM/ :.:`     ./.   
-oh.     ```oshMMMMMMds+/+:-            /+`   `:/`                   `./sNMMMMMMMNy/+:/`     -:`    
-sy/     +ssdddMMMMMMMs:                +/     ::-`                  `+NMMMMMMMMNyoyy+: `  `:-  `   
/hyh:+osymNNmNNMMMMMMMs-```            `//     .::.                   :MMMMMMMMM/.//./`   ./` `.  ..
-+:ys/sdNNNmmNMMMMMMMMdso-`             o/     :+/                    :NNMMMMMMh `-`-. ` `-` --  --`
-++sh.:os/-ymdMMMMMMMMMd+              -o.     .o/                    /MNMMMMMN:``` :   ..  :-  --..
-///ssy+`  `oydNMMMMMMMd-              :y:     `oo.              `   -yNNMMMMMy`` `:.` -:`.:.  :-.+ 
-oooddd:     odNmmMMMMMMm+/-.```       :o:     .-:.             o-  +MMMMMMMMM/`.//:`.-- -/-  /-`/` 
:yhhdmd.     `hhydMMMMMMMmhhdhs/-`    `:o-     ++//            /+`.-NMMMMMMMMh.`+. ..//`//`  --`/.  
:syshm+     . `yhmMMMMMMMNso+o:.`     `/+`     -//-           `o./+mMMMMMMNyo.`:`  `oo`.`   :-./.   
+dhhhN:     :.`/hNMMMMMMMNm/:-.       `+::     .---          `osoymMMMMMMd:.--+  `.:s`.    -:.:     
/hhhmN+      o` `yMMMMMMMMm/   `       :o.     `+ss          -+/ssNMMMMMd`..-/. ```s/     ./::      
:ysyyydo     -:  -sMMMMMMMNy   `      -oo`     `--/.        `o-+ooMMMMMMh+hss` `/`+y.    `oo.       
/ysyyyym:    .o`  /NMMMMMMMN-  -:  `  ::/       -//.   .   `/. .sdMMNMNhhyyy/``o:++o     /:o        
:yyhyyysy-    -+.-/mNMMMMMMho` `+     -+-       `:-.  --   /-  /yNMMdhshdhyo-`++/+s:    +-o-        
+mhyyssmmm     y++yNNMMMMMMmm+  +` `-`:/-        -/+` +`  :+` -/mMMNs+hddhNs`+//os+    -oy/         
/mNhssdhym: `` o`sdNmMMMMMMMMd+.-y `+//:.`` ` ` `:+o/+-.`-s+--.+mMMo+ddddNs+++h/o+-   `/so`         
:sdmyosyss+  ` :-+hmMMMMMMMMMMNyhmy+syos:-.` `.-.:oo/-..-so..-+hMMMsyy+sdm:/hsooso    +/..       .+-
/hhdddhdyhd` ` --:smNMMMMMMMMMMdhdmhh+::+-`.``-::-o-oy++oy:.-/mNMMdshysyd/+yodhoy`   /s         -ss:
/ydddmmhssh-   `s`oyNMMMMMMMMNMNddmmd/:+s+oo++oo+so::+::hy/::omMMMmdhyhmooysyyys/    /:       `:+oy:
:ydddmmdysd-    +::hmMMMMMMMMMMNdhmNdo::dhsosyyhdNd/ .ydhs+oomNMMmdhydmmhdysyhho`   .+     ` `oshhs-
:hdhyyddhyd-    -+/sdMMMMMMMMMMMNdmMy: smmmhdhyysyds--yNmsyhdNMMNhhdmmmyyhosshs`    s.      `+oodys-
/dsshhhddddo    `h.sdMMMMMMMMMMMNmNNs.+dsssosssydNmy+/oNdmNNMMMMddmNNNddddhddo-``` -/   ` `.ohhmho+-
/ydmmdhdNNdd`   `+./dMMMMMMMMMMMMNMh--+hsoo+oo++ymy+/`/hdNMMMMMNddmmNNdymydmhy``.` s`  ```/hyyyyhss:
/hdsyhsoyddd` `.:so-ymNMMMMMMMMMMMN- :oddoos/++sydho-`-hNMMMMMMmmNmddmmmdhhyo.``  //   ` +yhhhhhs+- 
/hyo+o+ossdm:`..-ydoohmMMMMMMMMMMMy`  /odos+/::sdohyo..+NMNMMMMNNMmmdmdyhyoo:    .+-  ``-sdsyydo.   
`sysyysssdhsd/`--/sdhmNMMMMMMMMMMMd.`/hhdh//s/+ydodhy+.:NMMMMMNNNmmmNdo:+o+/     +/. ` -hddssys  .:-
 .hhhhdyyhsmyh+`:oymmyNMMMMMMMMMMN: `sNmNmyhho+yhmdmm/ `dMMMMMMMNmNdhy++o/+ `   `o/  ``oohyoos` :/.`
  -ddyhyhhhNhsm/syddmmyNNMMMMMMMMm:` sMNmMmdddmMydmNN/` -NMMMMMMMNmhdyhsoo-    `+-: `.o+sodss. :o:+:
   /NdmdhhhhNdddshhmmNmmMMMMMMMMMy```hMMNNdhmyNNmmNMMh-  sMMMMMMMMdNmNNdd/   ``-o`...oo+yysy. /ooy- 
   .dshsyshyhydhyyshmNNNMMMMMMMMm.  -NMMMMMNNdMmMNhyMN/` `mMMMMMMNNmNNmNm.`````++-`-oooyddh- .s+o-  
  ` shyooooyhdhoohhNNNNMMMMMMMMMy  `yMMMMMMMdNNMmNmoNMh.  yMMMMMMmMMMNNNy` ``.+/-..ohoso:s:``s++-   
``` .yhdhhhdhmdhssmdmNNMMMMMMMms+  /MMMMMMhyso+++hMMMMm+..yMMMMMMMNMMMMds`.``s-.:`+hs+sy+:  +s//    
`````ydyyyhhmddhoodNmMMMMMMMMm:-  .yMMMMMM:.----`+MMMMy/.-.mMMMMMMMMNNNho:``-y...+syyo+o.``+yho     
`   `.dyshhNmmdhhhdNmMMMMMMMNo`   hMMMMMMm/ymmmh.`MMMMNh`  syMMMMMMNNNhsy:-./++./sh+sso.  +-.:      
  ````oyoohNmyddmdddmNMMMMMMd   .:mMMMMMMh-omdhs  dMMMMd.  .hMMMMMMMMmhho+ooyy.:sss/+s.``/:         
    ```ddhhdMNmNNmNmNmMMMMMMm   :hMMMMMMMo`o+/-d  +MMMMM/  ./yMMMMMMMNdmysooo:.ssyooo: .o:          
..-    /hhmNNNNNNNNNNMNMMMmyh. ..osyNMMNmo/yh:oho+/dmNhoo-.`.+oyNMNMNNMdhos-o`+oh+o++` /y           
  `-` `-NhddmMmmNMNMNNNNMy`     ````-/+::yddhydmdso/.o-  --.    :mNNNNMddos:o+yhsoso```h-           
   .::/+dysyhNdhNNMMNNMMd`  .```      ` ``:::o/::-`  `     .  `` -NMNMNhhhdydho/oyy`  -s            
   `.so:sdsyhmmMmNMMNMNN.               //`` //` `-.              +MMMMhsdhhdhs+od`   o.            
   ` `+..hyyyhmNMMNMMMmm`                `:-:---:``               -yMMMNhysdho+oy/   .o  `          
.:---:/s.:dshyhmMmNMMMNy`                  /dyss.`                `hMMNhdysmssmdo    h` `           
-o++/++ss:yddssyNmMMMMMMo                .os.`.:s/                +MMMNNmsydyyys  ` .o.             
.-:+/---hyomdyhhddNMMMMmMd/             .:y-    +y-`           `+mMMMMdNh/yysyh/ `  s.`` `          
        -s+sMhddhMMNMMMNhyNNhs/:-.`````:++..--:. /+.       `:+hNMNyNMMMNhhhhyyds/::/s.-`.`          
.:       o+hmhhhmmNNNMMMhs/+yNMMNddhyydmms  `-`   dhhyyooymNNNmhsoydMMMNyyhs+yho+:-h` `             
 o-      `s.s/h/syhMMNMNms/o+o//yhmMNMMMN-` `` `  -NMMMMMmNyysso/+hNNNNmNdy+os:--:/o                
 `o`      :://ssyhNMMNNMMNss/yo+o/:/sdNMo          yNMhsyhy:oys/+omNdmmoshy:-+`.-:y-. `             
  .o       yo+/NdmmMMNNNNNoo+ssshy::/yhd.`         `hdyyyhddyyy+odmdmmydyhoyy/ ``s/.--.             
./:y/-..`.-o-:sMNmmdMMNNMNd+o+dhhs/-+yy/`  `   `    -dhyhhhNhyssdddhmm-//ms/y:``.h`--:.`            
+hyymo:/+/-`s+shmy/+hyhmmNNdhshhy+::+ys    ``        +shyhhMdddysssy++:-:hhh+./-:+` ``.`..          
-yoosd`.-``.syods`-:sshhhdmNNNmhdsssdm-     ````     `sdmNyhNNmso++my::::hoys `:h` `   `..``        
 `os+os```.-shsh` `.++o+/+hNmNhyhsodMh.`.` `.`-``..```-NNMhmmNNdyyhdhyo-oyy+-/.::+.      ``..       
   :+-/:``./`+/s+s`./:``./+dmy++ooyNN.     `.::`       +mNNmmmmddymy:/s+ssy/`.o/ `::`      ``.`     
  `.-/`y.`...`////s- /` ``.+dysysydmo        .`        `ymNmNmdddydd+/hds+/--`o-/.`./.`.     `.`    
 ..  o::o  `  .+--so.--  :+ydhdsoyNd`                   .mNMNNdmNmy++hhhdo:.-// :.: `:sy:`    ``..` 
``  ..o`h```.-`-+:+/o..:.+odyhd/ydm+               `     /sddmhhNmh//yhmdy..:y.  +-:`-yy:..:`   `..`
  ``  //s: -:...s+::++.s`/o+sysodmh.                      +sosyodNmsoyydy+/.o/-  :+/``/-hyso-     ` 
 `. `  y.o:::-/:-+o--+h:/ooosy/ddm:                       :+/o+-ymmdhdosy:/s-.:..++ys/s-ddds+       
`` ``  :/:h::/:--:o/+hd/hssshosNmy  .`                    --//+/ddNmdd+ss/+h`.:+/-.ydyN+:-+hh:`     
  ``    yodsss+++/:hdNyyysyhysdmN:  `.           -.`     .  :++ymdhyy+ :/+o/: :h//.-:ydydh+-:o/.    
 .` `  .sddNdyyssoyddmymsddhydmhy`   -  `+`    `:s+-        `:ommdyod+.`:/s:/: +/y/`   ``    `s/-   
`     .:-dmNyoyhhhddmddmmmdyhmmm-`.  .`        `:::          .oyhosyhs+`.o+/-o`.ho:.           ::.  
  `  ::.:++:m+o-+oy+myNNMNNmmNNs  :   .        `  .    `      /o::.yoo/:`o://:: :o.:.           .-.`
`` `++./o/.-:d-::o-:/hydNMMMNmm.  .`  `               `    `` .//-o//++/::::/:--.+/`:. `      `  `-`
  `+/-:+/...+/yoo:..:hymmNNNmh+    `  `.              -  `.. ` .:o/.`++o+-:::/:/.:y/.o.`-   ` ```  `
 `o/./++:.-/-.:hs`..+NhddNNydy`    .   `---           .  :      :/:-``++o/:::/-:/`oy:-/..:. ``:---` 
`o+-/+/:`-//`.:-y+/sosdsddNyd/     -`  omdNs         -  ``     .----- -+oo.::-::---oo.:/:-/-``-::--.
:/-/++:`/-o`-`.+/m+:-++yydhmy      `- `odyhy+        ` ``     .- .:.-- /+o:---./:` /y/:/+:-::.`.---.
.-/+//`:-s`:`:-/-:y.-:.dhhyN/       - ./s:/+s`      `--`      -   ---`.`+oo.--..-` `/s:-/:--+:.`:::.
./++:.--s.-  `///-do:`:oy:yo/.      .` --:.`-:     ..`       `-   `.--  -+oo`-` ./- /o/:://:-+---::.
-/+:-/:o--`   `   -d.`-:.ss-...     `- .  -  `    ``       `.-`    .-..  :+o/``  //:-/:-:-+:/:+/-/:.
.+/:++//`-        -/+`. `/:  `-      :           `-      .`         --`   oos.    /:/:/.//:/:/://:--
                """)
def page5():
    page4()
    print("""
    You radio a status report to the Moray and tell
them that you are going to cast off from the line
and descend under your own power. Your plan is
approved and you cast off your line. Now you are
on your own. The Seeker slips noiselessly into the
undersea canyon.
    As you drop into the canyon, you turn on the
Seeker's powerful searchlight. Straight ahead is a
dark wall covered with a strange type of barnacle
growth. To the left (port) side you see what appears
to be a grotto. The entrance is perfectly
round, as if it had been cut by human hands.
Lantern fish give off a pale, greenish light. To the
right (starboard) side of the Seeker you see bubbles
rising steadily from the floor of the canyon.
_______________________________________

    If you decide to investigate
the bubbles, turn to page 8.

    If you decide to investigate the grotto
with the round entrance, turn to page 9.

                    """)
    choicex = choice(8, 9)
    if choicex == "8":
        page8()
    if choicex == "9":
        page9()
def page6():
    print("""
    Your sea suit will protect you from the intense
pressures of the deep. It is a tight fit and takes you
some time to put it on. Finally you slip from the
airlock of the Seeker and stand on the ocean floor.
It is a strange and marvelous world where your
every move isslowed down. You begin to explore
with your special hand-held searchlight. You
examine the ledge by the canyon.
    Suddenly, a school of bright yellow angel fish
dart by, almost brushing you. What made them
move so fast? Are they being chased?
    Then you see it. The Seeker is in the grips of a
huge sea monster. It is similar to a squid, but it is
enormous. The Seeker is just a toy in its long,
powerful tentacles. You seek shelter behind a rock
formation. You know the spear gun you carry will
be useless against this monster. It looks asthough it
will destroy the Seeker. Fish of allsizes huddle with
you in an attempt to escape the monster.
______________________________________

    If you stay hidden close to
the Seeker, turn to page 10.

    If you try to escape in the
hope that rescuers will see
you, turn to page 12.
                """)
    choicex = choice(10, 12)
    if choicex == "10":
        page10()
    if choicex == "12":
        page12()
def page7():
    print("""

                """)
def page8():
    print(""" 
    Carefully, you maneuver the Seeker between
the walls of the canyon.
    On the floor of the canyon, you discover a large
round hole out of which flow the large bubbles.
The Seeker is equipped with scientific equipment
to analyze the bubbles. It also has sonar equipment
that can measure the depth of any hole.
______________________________________

    If you decide to analyze the bubbles,
turn to page 11.

    If you decide to take sonar readings,
turn to page 15.
                """)
    choicex = choice(11, 15)
    if choicex == "11":
        page11()
    if choicex == "15":
        page15()

page1()
