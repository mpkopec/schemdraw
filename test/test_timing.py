import schemdraw
from schemdraw.logic.timing import TimingDiagram


json_text = '''{ signal: [
    { name: "clk",         wave: "p.....|..." },
    { name: "Data",        wave: "x.345x|=.x", data: ["head", "body", "tail", "data"] },
    { name: "Request",     wave: "0.1..0|1.0" },
    { },
    { name: "Acknowledge", wave: "1.....|01." }
]}
'''


with schemdraw.Drawing(file='my_circuit.svg') as d:
    d += TimingDiagram.from_json(json_text, datasize=14)

