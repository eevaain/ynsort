  const [solutionVarsInput, setSolutionVarsInput] = useState("i1, i2, i3, i4");
  const [constantsInput, setConstantsInput] = useState(`{
  "IA": 6,
  "Rw": 5.1,
  "Rx": 1.5,
  "Ry": 3.6,
  "Rz": 1.1
}`);
  const [equationsInput, setEquationsInput] = useState(`Rx*(i4-i2) + Rx*iz = 0
IA = i1 - i2
Rw*i1 + Ry*(i1-i3) + Rx*(i2-i4) = 0
0 + Ry*(i3-i1) + Rz*i3 = 0`);