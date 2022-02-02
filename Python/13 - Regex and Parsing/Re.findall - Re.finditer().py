import re

vowels = "aeiou"
constants = "qwrtypsdfghjklzxcvbnm"

pattern = r"(?<=[%s])([%s]{2,})[%s]" % (constants, vowels, constants)

m = re.findall(pattern, input(), flags=re.I)
if m:
    print("\n".join(m))
else:
    print(-1)
