import versioneer, os, re
versionFile = open(os.path.join("scadFiles", "progSCADversion.scad"), 'w+')

rawVersion=versioneer.get_version()

if re.match('^\d+(\.\d+)*$',rawVersion.split('+')[0]):
  sanitizedVersion=rawVersion.split('+')[0]
else:
  sanitizedVersion=0

listVersion=sanitizedVersion.split('.')
listVersion = [int(number) for number in listVersion]

gitVersion=versioneer.get_versions()['full-revisionid']

versionText = """\
progScadRawVersion="{rawVersion}"
progScadVersion="{version}"
progScadListVerion={listVersion}
prigScadGitVersion="{gitVersion}"
""".format(
  rawVersion=rawVersion,
  version=sanitizedVersion,
  listVersion=listVersion,
  gitVersion=gitVersion
)

versionFile.write(versionText)
