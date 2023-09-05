#!/usr/bin/env python
'''
Print markdown documentation for each nodedef in the given document.
'''

import sys, os, argparse
import MaterialX as mx

HEADERS = ('Name', 'Type', 'Default Value',
           'UI name', 'UI min', 'UI max', 'UI Soft Min', 'UI Soft Max', 'UI step', 'UI group', 'UI Advanced', 'Doc', 'Uniform')

ATTR_NAMES = ('uiname', 'uimin', 'uimax', 'uisoftmin', 'uisoftmax', 'uistep', 'uifolder', 'uiadvanced', 'doc', 'uniform' )

def main():
    parser = argparse.ArgumentParser(description="Print documentation for each nodedef in the given document.")
    parser.add_argument(dest="inputFilename", help="Filename of the input MaterialX document.")
    parser.add_argument('--docType', dest='documentType', default='md', help='Document type. Default is "md" (Markdown). Specify "html" for HTML output')
    parser.add_argument('--showInherited', default=False, action='store_true', help='Show inherited inputs. Default is False')
    opts = parser.parse_args()

    doc = mx.createDocument()
    try:
        mx.readFromXmlFile(doc, opts.inputFilename)
    except mx.ExceptionFileMissing as err:
        print(err)
        sys.exit(0)

    for nd in doc.getNodeDefs():
        # HTML output
        if opts.documentType == "html":
            print('<head><style>')
            print('table, th, td {')
            print('   border-bottom: 1px solid; border-collapse: collapse; padding: 10px;')
            print('}')
            print('</style></head>')
            print('<ul>')
            print(f'<li> <em>Nodedef</em>: {nd.getName()}')
            print(f'<li> <em>Type</em>: {nd.getType()}')
            if len(nd.getNodeGroup()) > 0:
                print(f'<li> <em>Node Group</em>: {nd.getNodeGroup()}')
            if len(nd.getVersionString()) > 0:
                print(
                    f'<li> <em>Version</em>: {nd.getVersionString()}. Is default: {nd.getDefaultVersion()}'
                )
            if len(nd.getInheritString()) > 0:
                print(f'<li> <em>Inherits From</em>: {nd.getInheritString()}')
            print('<li> <em>Doc</em>: %s\n' % nd.getAttribute('doc'))
            print('</ul>')
            print('<table><tr>')
            for h in HEADERS:
                print(f'<th>{h}</th>')
            print('</tr>')
            inputList = nd.getActiveInputs() if opts.showInherited  else nd.getInputs()
            tokenList = nd.getActiveTokens() if opts.showInherited  else nd.getTokens()
            outputList = nd.getActiveOutputs() if opts.showInherited  else nd.getOutputs()
            totalList = inputList + tokenList + outputList;
            for port in totalList:
                print('<tr>')
                infos = []
                if port in outputList:
                    infos.append(f'<em>{port.getName()}</em>')
                elif port in tokenList:
                    infos.append(port.getName())
                else:
                    infos.append(f'<b>{port.getName()}</b>')
                infos.append(port.getType())
                val = port.getValue()
                if port.getType() == "float":
                    val = round(val, 6)
                infos.append(str(val))
                infos.extend(port.getAttribute(attrname) for attrname in ATTR_NAMES)
                for info in infos:
                    print(f'<td>{info}</td>')
                print('</tr>')
            print('</table>')

        else:
            print(f'- *Nodedef*: {nd.getName()}')
            print(f'- *Type*: {nd.getType()}')
            if len(nd.getNodeGroup()) > 0:
                print(f'- *Node Group*: {nd.getNodeGroup()}')
            if len(nd.getVersionString()) > 0:
                print(
                    f'- *Version*: {nd.getVersionString()}. Is default: {nd.getDefaultVersion()}'
                )
            if len(nd.getInheritString()) > 0:
                print(f'- *Inherits From*: {nd.getInheritString()}')
            print('- *Doc*: %s\n' % nd.getAttribute('doc'))
            print('| ' + ' | '.join(HEADERS) + ' |')
            print('|' + ' ---- |' * len(HEADERS) + '')
            inputList = nd.getActiveInputs() if opts.showInherited  else nd.getInputs()
            tokenList = nd.getActiveTokens() if opts.showInherited  else nd.getTokens()
            outputList = nd.getActiveOutputs() if opts.showInherited  else nd.getOutputs()
            totalList = inputList + tokenList + outputList;
            for port in totalList:
                infos = []
                if port in outputList:
                    infos.append(f'*{port.getName()}*')
                elif port in tokenList:
                    infos.append(port.getName())
                else:
                    infos.append(f'**{port.getName()}**')
                infos.append(port.getType())
                val = port.getValue()
                if port.getType() == "float":
                    val = round(val, 6)
                infos.append(str(val))
                infos.extend(port.getAttribute(attrname) for attrname in ATTR_NAMES)
                print('| ' + " | ".join(infos) + ' |')

if __name__ == '__main__':
    main()
