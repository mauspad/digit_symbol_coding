#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 22, 2021, at 11:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Digit Symbol Coding'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='\\\\storage.yale.edu\\home\\DanaSmall-CC1622-Drive\\Small_Lab\\resources, equipment and manuals\\Resources\\Psychopy Tasks\\digit_symbol_coding\\digit_symbol_coding.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_1 = visual.ImageStim(
    win=win,
    name='instructions_1', 
    image='images/instructions1.jpg', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enter = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instructions_2 = visual.ImageStim(
    win=win,
    name='instructions_2', 
    image='images/instructions2.jpg', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enter_2 = keyboard.Keyboard()

# Initialize components for Routine "practice1"
practice1Clock = core.Clock()
practiceimg1 = visual.ImageStim(
    win=win,
    name='practiceimg1', 
    image='images/practice1.jpg', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_response = keyboard.Keyboard()
incorrect = visual.ImageStim(
    win=win,
    name='incorrect', 
    image='images/practice-incorrect.jpg', mask=None,
    ori=0, pos=(0, -250), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "practice2"
practice2Clock = core.Clock()
practice_img_2 = visual.ImageStim(
    win=win,
    name='practice_img_2', 
    image='images/practice2.jpg', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_resp_2 = keyboard.Keyboard()
incorrect_2 = visual.ImageStim(
    win=win,
    name='incorrect_2', 
    image='images/practice-incorrect.jpg', mask=None,
    ori=0, pos=(0, -250), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "practice3"
practice3Clock = core.Clock()
practiceimg3 = visual.ImageStim(
    win=win,
    name='practiceimg3', 
    image='images/practice3.jpg', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_response_3 = keyboard.Keyboard()
incorrect_3 = visual.ImageStim(
    win=win,
    name='incorrect_3', 
    image='images/practice-incorrect.jpg', mask=None,
    ori=0, pos=(0, -250), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
instructions_3 = visual.ImageStim(
    win=win,
    name='instructions_3', 
    image='images/instructions3.jpg', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
enter_3 = keyboard.Keyboard()

# Initialize components for Routine "code_trials"
code_trialsClock = core.Clock()
key_resp = keyboard.Keyboard()
key = visual.ImageStim(
    win=win,
    name='key', 
    image='sin', mask=None,
    ori=0, pos=(0, -80), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
symbol = visual.ImageStim(
    win=win,
    name='symbol', 
    image='sin', mask=None,
    ori=0, pos=(0, 120), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You have completed the task :)',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
# update component parameters for each repeat
enter.keys = []
enter.rt = []
# keep track of which components have finished
instructionsComponents = [instructions_1, enter]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_1* updates
    if instructions_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_1.frameNStart = frameN  # exact frame index
        instructions_1.tStart = t  # local t and not account for scr refresh
        instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_1, 'tStartRefresh')  # time at next scr refresh
        instructions_1.setAutoDraw(True)
    
    # *enter* updates
    waitOnFlip = False
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter.frameNStart = frameN  # exact frame index
        enter.tStart = t  # local t and not account for scr refresh
        enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
        enter.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions2"-------
# update component parameters for each repeat
enter_2.keys = []
enter_2.rt = []
# keep track of which components have finished
instructions2Components = [instructions_2, enter_2]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_2* updates
    if instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_2.frameNStart = frameN  # exact frame index
        instructions_2.tStart = t  # local t and not account for scr refresh
        instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_2, 'tStartRefresh')  # time at next scr refresh
        instructions_2.setAutoDraw(True)
    
    # *enter_2* updates
    waitOnFlip = False
    if enter_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter_2.frameNStart = frameN  # exact frame index
        enter_2.tStart = t  # local t and not account for scr refresh
        enter_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter_2, 'tStartRefresh')  # time at next scr refresh
        enter_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(enter_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter_2.status == STARTED and not waitOnFlip:
        theseKeys = enter_2.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice1"-------
# update component parameters for each repeat
practice_response.keys = []
practice_response.rt = []
incorrect.setOpacity(0)
# keep track of which components have finished
practice1Components = [practiceimg1, practice_response, incorrect]
for thisComponent in practice1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "practice1"-------
while continueRoutine:
    # get current time
    t = practice1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceimg1* updates
    if practiceimg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceimg1.frameNStart = frameN  # exact frame index
        practiceimg1.tStart = t  # local t and not account for scr refresh
        practiceimg1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceimg1, 'tStartRefresh')  # time at next scr refresh
        practiceimg1.setAutoDraw(True)
    
    # *practice_response* updates
    waitOnFlip = False
    if practice_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_response.frameNStart = frameN  # exact frame index
        practice_response.tStart = t  # local t and not account for scr refresh
        practice_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_response, 'tStartRefresh')  # time at next scr refresh
        practice_response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(practice_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice_response.status == STARTED and not waitOnFlip:
        theseKeys = practice_response.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
    
    # *incorrect* updates
    if incorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        incorrect.frameNStart = frameN  # exact frame index
        incorrect.tStart = t  # local t and not account for scr refresh
        incorrect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(incorrect, 'tStartRefresh')  # time at next scr refresh
        incorrect.setAutoDraw(True)
    wrongkey = event.getKeys(keyList=['2','3'])
    if wrongkey:
        timer = core.CountdownTimer(3)
        incorrect.opacity = 1
    
    rightkey = event.getKeys(keyList=['1'])
    if rightkey:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice1"-------
for thisComponent in practice1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice2"-------
# update component parameters for each repeat
practice_resp_2.keys = []
practice_resp_2.rt = []
incorrect_2.setOpacity(0)
# keep track of which components have finished
practice2Components = [practice_img_2, practice_resp_2, incorrect_2]
for thisComponent in practice2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "practice2"-------
while continueRoutine:
    # get current time
    t = practice2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_img_2* updates
    if practice_img_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_img_2.frameNStart = frameN  # exact frame index
        practice_img_2.tStart = t  # local t and not account for scr refresh
        practice_img_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_img_2, 'tStartRefresh')  # time at next scr refresh
        practice_img_2.setAutoDraw(True)
    
    # *practice_resp_2* updates
    waitOnFlip = False
    if practice_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_resp_2.frameNStart = frameN  # exact frame index
        practice_resp_2.tStart = t  # local t and not account for scr refresh
        practice_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_resp_2, 'tStartRefresh')  # time at next scr refresh
        practice_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(practice_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = practice_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
    
    # *incorrect_2* updates
    if incorrect_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        incorrect_2.frameNStart = frameN  # exact frame index
        incorrect_2.tStart = t  # local t and not account for scr refresh
        incorrect_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(incorrect_2, 'tStartRefresh')  # time at next scr refresh
        incorrect_2.setAutoDraw(True)
    wrongkey = event.getKeys(keyList=['2','1'])
    if wrongkey:
        timer = core.CountdownTimer(3)
        incorrect_2.opacity = 1
    
    rightkey = event.getKeys(keyList=['3'])
    if rightkey:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice2"-------
for thisComponent in practice2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice3"-------
# update component parameters for each repeat
practice_response_3.keys = []
practice_response_3.rt = []
incorrect_3.setOpacity(0)
# keep track of which components have finished
practice3Components = [practiceimg3, practice_response_3, incorrect_3]
for thisComponent in practice3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "practice3"-------
while continueRoutine:
    # get current time
    t = practice3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceimg3* updates
    if practiceimg3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceimg3.frameNStart = frameN  # exact frame index
        practiceimg3.tStart = t  # local t and not account for scr refresh
        practiceimg3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceimg3, 'tStartRefresh')  # time at next scr refresh
        practiceimg3.setAutoDraw(True)
    
    # *practice_response_3* updates
    waitOnFlip = False
    if practice_response_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_response_3.frameNStart = frameN  # exact frame index
        practice_response_3.tStart = t  # local t and not account for scr refresh
        practice_response_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_response_3, 'tStartRefresh')  # time at next scr refresh
        practice_response_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(practice_response_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practice_response_3.status == STARTED and not waitOnFlip:
        theseKeys = practice_response_3.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
    
    # *incorrect_3* updates
    if incorrect_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        incorrect_3.frameNStart = frameN  # exact frame index
        incorrect_3.tStart = t  # local t and not account for scr refresh
        incorrect_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(incorrect_3, 'tStartRefresh')  # time at next scr refresh
        incorrect_3.setAutoDraw(True)
    wrongkey = event.getKeys(keyList=['1','3'])
    if wrongkey:
        timer = core.CountdownTimer(3)
        incorrect_3.opacity = 1
    
    rightkey = event.getKeys(keyList=['2'])
    if rightkey:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice3"-------
for thisComponent in practice3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions3"-------
# update component parameters for each repeat
enter_3.keys = []
enter_3.rt = []
# keep track of which components have finished
instructions3Components = [instructions_3, enter_3]
for thisComponent in instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instructions3"-------
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_3* updates
    if instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_3.frameNStart = frameN  # exact frame index
        instructions_3.tStart = t  # local t and not account for scr refresh
        instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_3, 'tStartRefresh')  # time at next scr refresh
        instructions_3.setAutoDraw(True)
    
    # *enter_3* updates
    waitOnFlip = False
    if enter_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter_3.frameNStart = frameN  # exact frame index
        enter_3.tStart = t  # local t and not account for scr refresh
        enter_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter_3, 'tStartRefresh')  # time at next scr refresh
        enter_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(enter_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter_3.status == STARTED and not waitOnFlip:
        theseKeys = enter_3.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions3"-------
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('coding.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "code_trials"-------
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    key.setImage('images/key.JPG')
    if trials.thisN == 0:
        startTime = globalClock.getTime()
    symbol.setImage(imgpath)
    # keep track of which components have finished
    code_trialsComponents = [key_resp, key, symbol]
    for thisComponent in code_trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    code_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "code_trials"-------
    while continueRoutine:
        # get current time
        t = code_trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=code_trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys.append(theseKeys.name)  # storing all keys
                key_resp.rt.append(theseKeys.rt)
                # was this 'correct'?
                if (key_resp.keys == str(corrans)) or (key_resp.keys == corrans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *key* updates
        if key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key.frameNStart = frameN  # exact frame index
            key.tStart = t  # local t and not account for scr refresh
            key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key, 'tStartRefresh')  # time at next scr refresh
            key.setAutoDraw(True)
        if globalClock.getTime() - startTime >= 90:
            trials.finished = True
            continueRoutine = False
        
        # *symbol* updates
        if symbol.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            symbol.frameNStart = frameN  # exact frame index
            symbol.tStart = t  # local t and not account for scr refresh
            symbol.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(symbol, 'tStartRefresh')  # time at next scr refresh
            symbol.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in code_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "code_trials"-------
    for thisComponent in code_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('symbol.started', symbol.tStartRefresh)
    trials.addData('symbol.stopped', symbol.tStopRefresh)
    # the Routine "code_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
