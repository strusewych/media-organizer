import os
import re
import shutil

class Logger:
  
    def __init__(self, logFileLocation):
        self.data = []
        self.logger = open(logFileLocation, 'a')
        self.shouldLog = True
        self.shouldPrint = True
        
    def setLogFileLocation(self, logFileLocation):
        self.logger = open(logFileLocation, 'a')
        
    def setShouldJustPrint(self):
        self.shouldLog = False
        self.shouldPrint = True
      
    def setShouldJustLog(self):
        self.shouldLog = True
        self.shouldPrint = False
      
    def setShouldLogAndPrint(self):
        self.shouldLog = True
        self.shouldPrint = True
        
    def write(self, message):
        if self.shouldLog:
            self.logger.write(message)
        if self.shouldPrint:
            print message