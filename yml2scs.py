import yaml

with open("mic numbers.yml") as file:
    micNumbers = yaml.load(file, Loader=yaml.FullLoader)
# print(micNumbers)

with open(input("YAML Inupt File: ")) as file:
    scenes = yaml.load(file, Loader=yaml.FullLoader)
# print(scenes)

with open("base.scs11.txt") as file:
    base = file.read()

output = ""

for i, scene in enumerate(scenes):
    controlMessages = "\n".join(f'''
        <ControlMessage>
            <CMLogicalDev>MIDI</CMLogicalDev>
            <MSMsgType>CC</MSMsgType>
            <MSChannel>2</MSChannel>
            <MSParam1>{micNumbers[actor]}</MSParam1>
            <MSParam2>{"0" if actor in scene['actors'] else "127"}</MSParam2>
        </ControlMessage>
         ''' for actor in micNumbers.keys())
    output += f"""
    <Cue>
       <CueId>Q{i+1}</CueId>
      <Description>{scene['scene']}</Description>
      <Sub>
         <SubType>M</SubType>
         <SubDescription>MIDI Send</SubDescription>
         <DefSubDes>1</DefSubDes>
         {controlMessages}
      </Sub>
    </Cue>
    """

outputString = base.replace("{{CUES}}", output)

with open(input("Output File: ")+".scs11", "w") as file:
    file.write(outputString)