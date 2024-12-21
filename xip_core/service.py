import daemon
import logging
import signal
import sys
from typing import Optional

class XIPService:
    def __init__(self, interface_name: str, xip_address: Optional[str] = None):
        self.interface = XIPInterface(interface_name)
        self.address = XIPAddress(xip_address)
        self.running = False
        self.logger = logging.getLogger('xip_service')

    def start(self):
        self.logger.info(f"Starting XIP service on {self.interface.interface_name}")
        self.running = True
        
        # Set up signal handlers
        signal.signal(signal.SIGTERM, self.stop)
        signal.signal(signal.SIGINT, self.stop)
        
        try:
            # Bind to interface
            self.socket = self.interface.bind_xip(self.address)
            self.main_loop()
        except Exception as e:
            self.logger.error(f"Service error: {e}")
            self.stop()

    def stop(self, signum=None, frame=None):
        self.logger.info("Stopping XIP service")
        self.running = False
        if hasattr(self, 'socket'):
            self.socket.close()

    def main_loop(self):
        while self.running:
            try:
                data = self.socket.recv(65535)
                if data:
                    self.handle_packet(data)
            except Exception as e:
                self.logger.error(f"Error in main loop: {e}")

    def handle_packet(self, data: bytes):
        # Packet handling logic here
        pass