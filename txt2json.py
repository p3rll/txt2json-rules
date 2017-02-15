#! /usr/bin/python

import argparse,re,json


Version = '1.0'

# Arguments obviously...
parser = argparse.ArgumentParser(description='Text to Json converter for firewall filter rules.')
parser.add_argument('-f','--file', help='Input text file',required=True)
# parser.add_argument('-o','--output',help='Set the timeout for tests that tend to hang up',default='txt2json.out',required=False)

args = parser.parse_args()

# Output variable
# output = args.output

comment_pattern = re.compile(r'\!')
at_pattern = re.compile(r'\@\@')
pipe_pattern = re.compile(r'\|')
cleanup_pattern = re.compile(r'@@|\|\||\n')

# Input Text file
text = args.file
rules = []
filter =[]



if __name__ == '__main__':
    if args.file:
        rule_list = open(text, 'r')
        for line in rule_list:
            rules = []
            pipe_match = re.findall(pipe_pattern, line)
            comment_match = re.findall(comment_pattern, line)
            at_match = re.findall(at_pattern, line)
            output = re.sub(cleanup_pattern,'',line)
            if pipe_match:
                rules.append(output)
                filter.append('Drop')
            if comment_match:
                pass
            if at_match:
                rules.append(output)
                filter.append('Drop')
            data = dict(zip(rules, filter))
            jsondata = json.dumps(data)
            print jsondata




