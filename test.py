"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."
        d={}
        for i in range(250,301):
            s='s'+str(i)
            d[s]=self.addSwitch(s)
        with open(r'test_file.txt') as f:
          line = f.readline()
          print(line[0:3])
          while line:
            line = f.readline()
#             s='s'+str(line[0:3])
#             d[s]=self.addSwitch(s)
#             s='s'+str(line[0:3])
            x='s'+str(line[4::])
            d[x.split('\n')[0]]=self.addSwitch(x.split('\n')[0])
        with open(r'test_file.txt') as f:
          line = f.readline()
          print(line[0:3])
          while line:
            line = f.readline()
            x='s'+str(line[4::])
            self.addLink(d['s'+str(line[0:3])],d[x.split('\n')[0]])
#          # Add hosts and switches
#         leftHost = self.addHost( 'h1' )
#         rightHost = self.addHost( 'h2' )
#         leftSwitch = self.addSwitch( 's251' )
#         rightSwitch = self.addSwitch( 's256' )

#         # Add links
#         self.addLink( leftHost, leftSwitch )
#         self.addLink( leftSwitch, rightSwitch )
#         self.addLink( rightSwitch, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }
