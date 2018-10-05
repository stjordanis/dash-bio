import os

fileString = "\"use strict\";\nvar shaders = {}; \n"

for fname in os.listdir('src/shaders'):
    varName = fname.strip('.glsl')
    with open(os.path.join('./src/shaders', fname), 'r') as f:
        code = ('').join(f.readlines())
        fileString += "shaders [\"{}\"] = `{}`; \n".format(varName, code)
fileString += "module.exports = {shaders};"
print(fileString)
