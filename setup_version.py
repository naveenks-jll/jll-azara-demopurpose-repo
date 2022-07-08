import os
import requests
organization = os.getenv("ORGANIZATION","dp-red2-org-devops")
project = os.getenv("PROJECT","AzaraDevOps")
feedId = os.getenv("ARTIFACT_FEED","JLL-AZARA-V2-PYTHON-SDKS")
packageId = os.getenv("PACKAGE_ID")
url = f"https://feeds.dev.azure.com/{organization}/{project}/_apis/Packaging/Feeds/{feedId}/Packages/{packageId}"


def inc_major(version):
    major, minor, patch = version.split('.')
    major = str(int(major) + 1)
    return ".".join([major, minor, patch])


def inc_minor(version):
    major, minor, patch = version.split('.')
    minor = str(int(minor) + 1)
    if minor[-1:] == '0':
        return inc_major(".".join([major, minor[-1:], patch]))
    return ".".join([major, minor, patch])


def inc_patch(version):
    major, minor, patch = version.split('.')
    patch = str(int(patch) + 1)
    if patch[-2:] == '00':
        return inc_minor(".".join([major, minor, patch[-2:]]))
    return ".".join([major, minor, patch])


def get_version():
    username = os.environ.get('azureusername')
    password = os.environ.get('azurepassword')
    res = requests.get(url=url,
                       auth=(username, password))
    if res.status_code != 200:
        raise Exception(f"Failed to get package version from feed, msg: {res.text}")
    res = res.json()
    version = res["versions"][0]["version"]
    return inc_patch(version)

def main():
    version = get_version()
    with open('demopurposepkg'+'/_version.py', 'w') as f:
        f.write("__version__ = '{version}'".format(version=version))

if __name__ == '__main__':
    main()
