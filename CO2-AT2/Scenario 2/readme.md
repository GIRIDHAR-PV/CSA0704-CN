# LAN & Multiple Access Simulation

## Network Observation & Analysis
During the simulation in Cisco Packet Tracer, replacing the switch with a hub clearly demonstrated how physical layer network devices handle traffic. When sending data through the hub, it blindly broadcasted packets to every single connected port simultaneously, causing excessive unnecessary traffic and creating a single large collision domain. In contrast, the switch maintained a MAC address table to direct frames exclusively to the intended destination device. Because switches create dedicated collision domains per port and support full-duplex communication, they eliminate packet collisions entirely, providing significantly higher throughput, security, and efficiency in modern LANs.

## Repository Contents
- `cafe_network.pkt`: Cisco Packet Tracer topology file containing the 5-PC network setup.
- `/screenshots`: Images demonstrating successful ICMP pings and the hub broadcast simulation.
