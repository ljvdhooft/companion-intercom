from CompanionIntercom import CompanionIntercom

c = CompanionIntercom()

c.createButton("PGM", 1, [0, 1], False, [], [], ["/aux/7/send/mx5/on"], ["/aux/7/send/mx5/lvl"])
c.createButton("CREW", 1, [0, 2], True, ["/ch/36/send/mx6/on 1"],["/ch/36/send/mx6/on 0"],["/ch/35/send/mx5/on"],["/ch/35/send/mx5/lvl"])
c.createButton("STAGE",1,[0, 3],False,["/ch/36/send/12/on 1"],["/ch/36/send/12/on 0"])
c.createButton("VLOER",1,[0, 4],False,["/ch/36/main/1/on 1",],["/ch/36/main/1/on 0",])
c.createButton("BAND",1,[2, 1],False,[
        "/ch/36/send/1/on 1",
        "/ch/36/send/2/on 1",
        "/ch/36/send/3/on 1",
        "/ch/36/send/4/on 1",
        "/ch/36/send/5/on 1",
        "/ch/36/send/6/on 1",
        "/ch/36/send/7/on 1",
        "/ch/36/send/8/on 1",
        "/ch/36/send/9/on 1",
        "/ch/36/send/10/on 1",
		],
		[
        "/ch/36/send/1/on 0",
        "/ch/36/send/2/on 0",
        "/ch/36/send/3/on 0",
        "/ch/36/send/4/on 0",
        "/ch/36/send/5/on 0",
        "/ch/36/send/6/on 0",
        "/ch/36/send/7/on 0",
        "/ch/36/send/8/on 0",
        "/ch/36/send/9/on 0",
        "/ch/36/send/10/on 0",
		]
)
c.createButton("STGMGR",1,[2, 2],False,["/ch/36/send/mx4/on 1",],["/ch/36/send/mx4/on 0",])
c.createButton("DIED",1,[2, 3],False,["/ch/36/send/4/on 1",],["/ch/36/send/4/on 0",],["/ch/22/send/mx5/on"],["/ch/22/send/mx5/lvl"])
c.createButton("ILSE",1,[2, 4],False,["/ch/36/send/6/on 1",],["/ch/36/send/6/on 0",])

c.createListenButton(1, [0, 0])
c.createVolUpButton(1, [1, 0])
c.createVolDownButton(1, [2, 0])

c.createInstance("192.168.84.10", 2223)

print(c.toJSON())
