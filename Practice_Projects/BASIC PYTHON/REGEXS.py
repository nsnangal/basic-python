import re
regexs=re.compile    (r'''(
(\d{3}|\(\d{3}\))?
(-|/s|.)?
\d{2}
)''',re.VERBOSE)
regexs1=regexs.finditer("123-56 mbb kjbk kjbk 878 292-33")
for match in regexs1:
    print(f'match:{match.group()} start:{match.start()}')
