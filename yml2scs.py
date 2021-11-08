import yaml
from xml.sax.saxutils import escape

with open(input("Mic Numbers File: ")) as file:
    micNumbers = yaml.load(file, Loader=yaml.FullLoader)
# print(micNumbers)

with open(input("YAML Inupt File: ")) as file:
    scenes = yaml.load(file, Loader=yaml.FullLoader)
# print(scenes)

with open("base.scs11.txt") as file:
    base = file.read()

output = ""

for i, cue in enumerate(scenes):
    if 'actors' in cue:
        controlChanges = "\n".join(f'''
            <ControlMessage>
                <CMLogicalDev>MIDI</CMLogicalDev>
                <MSMsgType>CC</MSMsgType>
                <MSChannel>2</MSChannel>
                <MSParam1>{micNumbers[actor]}</MSParam1>
                <MSParam2>{"0" if actor in cue['actors'] else "127"}</MSParam2>
            </ControlMessage>
            ''' for actor in micNumbers.keys())
        controlChangeSubcue = f"""
        <Sub>
            <SubType>M</SubType>
            <SubDescription>Mute/Unmute Actors</SubDescription>
            <DefSubDes>1</DefSubDes>
            {controlChanges}
        </Sub>"""
    else:
        controlChangeSubcue = ""
    if 'progchange' in cue:
        programChangeSubcue = f'''
        <Sub>
            <SubType>M</SubType>
            <SubDescription>Change Scribble Strip</SubDescription>
            <DefSubDes>1</DefSubDes>
            <ControlMessage>
                <CMLogicalDev>MIDI</CMLogicalDev>
                <MSMsgType>PC</MSMsgType>
                <MSChannel>3</MSChannel>
                <MSParam1>{cue['progchange']}</MSParam1>
            </ControlMessage>
        </Sub>
            '''
    else:
        programChangeSubcue = ""
    output += f"""
    <Cue>
       <CueId>Q{i+1}</CueId>
      <Description>{escape(cue['cue'])}</Description>
        {programChangeSubcue}
        {controlChangeSubcue}
    </Cue>
    """

outputString = base.replace("{{CUES}}", output)

with open(input("Output File: ")+".scs11", "w") as file:
    file.write(outputString)