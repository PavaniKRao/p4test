
# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab
# Import Geni URN
import geni.urn as urn
# Import Cloudlab
import geni.aggregate.cloudlab as cloudlab


# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node1 = request.RawPC("node1")
node2 = request.RawPC("node2")

node1.hardware_type = 'xl170'
node2.hardware_type = 'xl170'
node1.component_id = urn.Node(cloudlab.Utah, "hp197")
node2.component_id = urn.Node(cloudlab.Utah, "hp199")

iface1 = node1.addInterface()
#iface2 = node1.addInterface()
iface3 = node2.addInterface()
#iface4 = node2.addInterface()


#link = request.Link(members = [node1, node2])

#link_0 = request.Link(ltype = "L2", members = [node1, node2])
#link_1 = request.Link(ltype = "L1", members = [node1, node2])




link_0 = request.L1Link("L1")
link_0.addInterface(iface1)
link_0.addInterface(iface3)
#link_0.setNoInterSwitchLinks()
#link_0.bandwidth = 1000000000

link_1 = request.Link(ltype = "L2", members = [node1, node2])
#link_1.bandwidth = 10000000
#link_1.setProperties(bandwidth=10000000)

#link_1 = request.Link(ltype = "L1")
#link_1.addInterface(iface2)
#link_1.addInterface(iface4)
#link_1.setNoInterSwitchLinks()


# Install and execute a script that is contained in the repository.
node1.addService(pg.Execute(shell="sh", command="sudo apt-get update -y && sudo apt-get install libxml2-dev pkg-config -y && sudo git -C /root/ clone https://github.com/itsiprikshit/probed.git && sudo autoreconf -i /root/probed/ "))
node1.addService(pg.Execute(shell="sh", command="sudo bash -c 'cd /root/probed ; ./configure ; make'"))
node1.addService(pg.Execute(shell="sh", command="sudo bash -c 'cp /root/probed/probed /usr/local/bin/'"))

node1.addService(pg.Execute(shell="sh", command="sudo apt-get install iperf3 -y"))

node1.addService(pg.Execute(shell="sh", command="sudo bash -c 'ifconfig eno50 up'"))
node1.addService(pg.Execute(shell="sh", command="sudo bash -c 'ifconfig eno50 172.16.1.1'"))
node1.addService(pg.Execute(shell="sh", command="sudo bash -c 'ifconfig ens1f0 up'"))
node1.addService(pg.Execute(shell="sh", command="sudo bash -c 'ifconfig ens1f0 192.168.1.1'"))
node1.addService(pg.Execute(shell="sh", command="sudo bash -c 'ethtool -s ens1f0 speed 10000 duplex full autoneg off'"))


#ethtool -s ens1f0 speed 10000 duplex full autoneg off


node2.addService(pg.Execute(shell="sh", command="sudo apt-get update -y && sudo apt-get install libxml2-dev pkg-config -y && sudo git -C /root/ clone https://github.com/itsiprikshit/probed.git && sudo autoreconf -i /root/probed/ "))
node2.addService(pg.Execute(shell="sh", command="sudo bash -c 'cd /root/probed ; ./configure ; make'"))
node2.addService(pg.Execute(shell="sh", command="sudo bash -c 'cp /root/probed/probed /usr/local/bin/'"))

node2.addService(pg.Execute(shell="sh", command="sudo apt-get install iperf3 -y"))

node2.addService(pg.Execute(shell="sh", command="sudo bash -c 'ifconfig eno50 up'"))
node2.addService(pg.Execute(shell="sh", command="sudo bash -c 'ifconfig eno50 172.16.1.2'"))
node2.addService(pg.Execute(shell="sh", command="sudo bash -c 'ifconfig ens1f0 up'"))
node2.addService(pg.Execute(shell="sh", command="sudo bash -c 'ifconfig ens1f0 192.168.1.2'"))
node2.addService(pg.Execute(shell="sh", command="sudo bash -c 'ethtool -s ens1f0 speed 10000 duplex full autoneg off'"))




# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)



