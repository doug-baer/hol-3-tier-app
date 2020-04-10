# hol-3-tier-app
HOL Three-Tier App scripts and essential host config files

Scripts and convenience files to support HOL 3-Tier App described (2017)
http://blogs.vmware.com/hol/2017/01/hol-three-tier-application-part-1.html

Basically, this is a multi-tier application we use in some of the VMware Hands-on Labs to demonstrate, among other things, network connectivity, microsegmentation and load balancing. 

As with anything, there are multiple ways to do this. This represents the way that worked for me.

## The Need ##
Whether you live in a cutting-edge, microservices-oriented world, or have a traditional application spread across multiple machines, the components (machines, containers, services, processes, etc.) need to communicate with one another over the network. Understanding what that looks like is important to securing the connection end-to-end. This simple application is intended to provide a starting point for learning or testing firewall and load balancing configurations to see how they affect a distributed environment.

For instruction purposes, we wanted three simple, independent parts that could be deployed, rearranged, and otherwise manipulated to illustrate many different situations that may occur in an environment. For HOL and other labs, small is usually good. Oh, and fast. It should be fast.

## The Application ##
This application consists of three operating system instances, independent VMs, each of which handles a specific task. When all of them can communicate over the network over the required ports, the client receives the requested information and can interact with that information. If there is a breakdown, not so much.

This demonstration application has been created so that each component VM is independent from the others: IP addresses can be changed and multiple instances of the web and application tier VMs can be created by cloning, renaming, and re-addressing. 

I put SSL in here because it is always a good idea to secure your web traffic, and it provides the opportunity to configure a load balancer in front of the web tier in a more realistic scenario.

## 2020 UPDATE COMING SOON ##
