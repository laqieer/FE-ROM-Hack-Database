import os
import csv
from xml.dom import minidom

fields = [
    "index",
    "title",
    "publisher",
    "location",
    "source",
    "language",
    "CRC32",
    "comment",
]

locations = [
    "Europe",
	"USA",
	"Germany",
	"China",
	"Spain",
	"France",
	"Italy",
	"Japan",
	"Netherlands",
	"England",
	"Denmark",
	"Finland",
	"Norway",
	"Poland",
	"Portugal",
	"Sweden",
	"Europe USA",
	"Europe USA Japan",
	"USA Japan",
	"Australia",
	"North Korea",
	"Brazil",
	"South Korea",
	"Europe Brazil",
	"Europe USA Brazil",
	"USA Brazil",
]

languages = [
    "French",
    "English (US)",
    "Chinese",
    "Danish",
    "Dutch",
    "Finland",
    "German",
    "Italian",
    "Japanese",
    "Norwegian",
    "Polish",
    "Portuguese",
    "Spanish",
    "Swedish",
    "English (UK)",
    "Portuguese (BR)",
    "Korean",
]

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class FormatError(Error):
    """Exception raised for errors in the format.

    Attributes:
        filename -- filename in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, filename):
        self.filename = filename
        self.message = "Unsupported format: " + os.path.splitext(filename)[-1][1:].upper()

    def __str__(self):
        return self.filename + " " + self.message

class ROM:
    def __init__(self, index, title, publisher, location, source, language, checksum, comment):
        self.index = index
        self.title = title
        self.publisher = publisher
        self.location = location
        self.source = source
        self.language = language
        self.checksum = checksum
        self.comment = comment


class ROMList:
    def __init__(self):
        self.roms = []

    def loadFromFile(self, filename):
        if filename.lower().endswith('.xml'):
            self.loadFromXML(filename)
        else:
            raise FormatError(filename)

    def saveToFile(self, filename):
        if filename.lower().endswith('.csv'):
            self.saveToCSV(filename)
        else:
            raise FormatError(filename)

    def loadFromXML(self, filename):
        for rom in minidom.parse(filename).getElementsByTagName('game'):
            index = rom.getElementsByTagName('releaseNumber')[0].firstChild.data
            title = rom.getElementsByTagName('title')[0].firstChild.data
            publisher = rom.getElementsByTagName('publisher')[0].firstChild.data
            location = locations[int(rom.getElementsByTagName('location')[0].firstChild.data)]
            source = rom.getElementsByTagName('sourceRom')[0].firstChild.data
            language = []
            languageCode = int(rom.getElementsByTagName('language')[0].firstChild.data)
            i = 0
            while languageCode > 0:
                if languageCode % 2 == 1:
                    language.append(languages[i])
                languageCode //= 2
                i += 1
            checksum = rom.getElementsByTagName('romCRC')[0].firstChild.data
            comment = rom.getElementsByTagName('comment')[0]
            if len(comment.childNodes) > 0:
                comment = comment.firstChild.data
            else:
                comment = ""
            self.roms.append(ROM(index, title, publisher, location, source, language, checksum, comment))

    def saveToCSV(self, filename):
        with open(filename, 'w', encoding='UTF-8-SIG') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            for rom in self.roms:
                csvwriter.writerow([rom.index, rom.title, rom.publisher, rom.location, rom.source, ' '.join(rom.language), rom.checksum, rom.comment])

