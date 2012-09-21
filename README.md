RasPiLEDChaser
==============

RasPiLEDMeter is a project for the [Raspberry Pi](http://raspberrypi.org) intended to provide a simple LED chaser (thinks [Knight Rider](http://en.wikipedia.org/wiki/Knight_Rider_(1982_TV_series))) to the platform.

You can have more information into “doc” folder.


Requirements
------------

* First of all : a Raspberry Pi
* LED and resistors to build the LED chaser. Assembly instructions are available at the following URL: [https://goddess-gate.com/dc2/index.php/pages/raspiledmeter.en](https://goddess-gate.com/dc2/index.php/pages/raspiledmeter.en). This is for a different project, but the assembly is the same.
* Python (with Debian / Raspbian : packages "python" and "python-dev")
* RPi.GPIO library (0.4.0a or newer) from [http://pypi.python.org/pypi/RPi.GPIO](http://pypi.python.org/pypi/RPi.GPIO)


To help you with the assembly, you may refer to the following files :

* raspiledchaser.sch : the circuit diagram to open with EAGLE
   ([http://www.cadsoft.de/freeware.htm](http://www.cadsoft.de/freeware.htm))
* You may need to download and install [Raspberry Part](https://github.com/adafruit/Fritzing-Library/blob/master/AdaFruit.fzbz) for Fritzing
* raspiledchaser.fzz : the assembly mockup to open with Fritzing
   ([http://fritzing.org/](http://fritzing.org/))

How to use RasPiLEDChaser
-------------------------

You'll first have to build the LED chaser, and plug it to the Raspberry Pi
  (check [https://goddess-gate.com/dc2/index.php/pages/raspiledmeter.en](https://goddess-gate.com/dc2/index.php/pages/raspiledmeter.en) for more information).

When you're done, just launch RasPiLEDChaser with `./raspiledchaser.sh start` as
  root user and admire the LED chaser working :-) When you want / need to stop
  it, just execute `./raspiledchaser.sh stop` as root user.

