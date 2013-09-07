#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import csv
import optparse

def readPorts():
	tcp_ports = {}
	udp_ports = {} 
	try:
		with open('all_ports.csv', 'r') as fx:
			line = csv.reader(fx, delimiter='\t')
			for port, tcp, udp, descr, official in line:
				if tcp:#.strip() == 'TCP':
					tcp_port = {port.strip(): descr.strip()}
					tcp_ports.update(tcp_port)
				if udp:#.strip() == 'UDP':
					udp_port = {port.strip(): descr.strip()}
					udp_ports.update(udp_port)
	except Exception, e:	
		print "[-] Error reading file all_ports.csv: " + str(e) 
	return tcp_ports, udp_ports

def getPort(protocol, port, all_tcp_ports, all_udp_ports):
	if protocol.upper() == 'TCP' or protocol.upper() == 'ALL':
		try:
			print '[+] TCP/%s: %s'  % (port, all_tcp_ports[str(port)])
		except Exception, e:
			print '[-] TCP/%s not found.' % (port)
	if protocol.upper() == 'UDP' or protocol.upper() == 'ALL': 
		try:
			print '[+] UDP/%s: %s'  % (port, all_udp_ports[str(port)])
		except Exception, e:
			print '[-] UDP/%s not found.' % (port)

def getPortsByDescr(descr, search_ports):
	filtered_ports = list(k for k,v in search_ports.iteritems() if descr.upper() in v.upper())
	return filtered_ports

def searchDescr(protocol, descr, all_tcp_ports, all_udp_ports):
	if protocol.upper() == "TCP" or protocol.upper() == "ALL":
		matched_tcp_ports = getPortsByDescr(descr, all_tcp_ports)
		#print matched_tcp_ports
		for port in matched_tcp_ports:
			getPort(protocol, port, all_tcp_ports, all_udp_ports) 
	if protocol.upper() == "UDP" or protocol.upper() == "ALL":
		matched_udp_ports = getPortsByDescr(descr, all_udp_ports)
		#print matched_udp_ports
		for port in matched_udp_ports:
			getPort(protocol, port, all_tcp_ports, all_udp_ports) 

def main():
	parser = optparse.OptionParser(usage = '%prog -p <protocol type> -s <search string>')
	parser.add_option('-p', dest='protocol', type='string', help='specify protocol: TCP, UDP, ALL')
	parser.add_option('-s', dest='search', type='string', help='specify search string or port number')
	(options, args) = parser.parse_args()
	protocol = options.protocol
	search = options.search
	if (protocol == None) | (search == None):
		print parser.usage
		exit(0)

	tcp_ports, udp_ports = readPorts()
	port_is_number = True
	try:
		number = int(search)
		search_is_port = True
	except:
		search_is_port = False

	if search_is_port:
		getPort(protocol, search, tcp_ports, udp_ports)
	else:
		searchDescr(protocol, search, tcp_ports, udp_ports)

if __name__ == '__main__':
	main()
