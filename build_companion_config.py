from CompanionIntercom import CompanionIntercom

c = CompanionIntercom()

c.createButton("button1", 1, [0, 1], ["/a/b 1", "/b/c 10"], ["/a/b 0"], ["x/y", "/q/t"], ["/x/y/vol"])
c.createButton("button2", 1, [1, 1], ["/a/b 1"], ["/a/b 0"])

c.createListenButton(1, [0, 0])
c.createVolUpButton(1, [1, 0])
c.createVolDownButton(1, [2, 0])

print(c.toJSON())
