import win32com.client as win

speaker_number = 0
spk = win.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item(speaker_number).GetAttribute("Name")) 
spk.Voice = vcs.Item(speaker_number)
spk.Speak("I have many projects to do, so do not waste my time")