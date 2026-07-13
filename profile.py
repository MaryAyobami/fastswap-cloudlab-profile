"""
This profile instantiates 2 nodes for Fastswap(Eurosys 2020) reproduction 
https://github.com/clusterfarmem/fastswap
"""

import geni.portal as portal
import geni.rspec.pg as rspec

pc = portal.Context()

node_types = [
    ("xl170", "xl170"),
    ("c6525-25g", "c6525-25g")
]

pc.defineParameter(
    "nodeType",
    "Node type",
    portal.ParameterType.STRING, NODE_TYPES[0][0],
                    NODE_TYPES,
                    longDescription="Select the node type."
)

pc.defineParameter(
    "osImage",
    "Disk image",
    portal.ParameterType.IMAGE,
    "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU16-64-STD",
    longDescription=(
       ""
    ),
)



params = pc.bindParameters()

request = pc.makeRequestRSpec()

client = request.RawPC("client")
client.hardware_type = params.nodeType
client.disk_image = params.osImage

farmem = request.RawPC("farmem")
farmem.hardware_type = params.nodeType
farmem.disk_image = params.osImage

lan = request.LAN("interconnect")
lan.addInterface(client.addInterface("if1"))
lan.addInterface(farmem.addInterface("if1"))

pc.printRequestRSpec(request)
