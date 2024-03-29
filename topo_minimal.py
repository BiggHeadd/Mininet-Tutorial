#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def Minimal():

    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/8')

    info( '*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=Controller,
                           protocol='tcp',
                           port=6633)

    info( '*** Add one switche\n')
    s1 = net.addSwitch(name='s1',
                       cls=OVSKernelSwitch)

    info( '*** Add hosts')
    h1 = net.addHost(name='h1',
                     cls=Host,
                     ip='10.0.0.1',
                     defaultRoute=None)
    h2 = net.addHost(name='h2',
                     cls=Host,
                     ip='10.0.0.2',
                     defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    Minimal()