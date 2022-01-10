#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-scifi-central.jarbasai=skill_scifi_central:SciFiCentralSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-scifi-central',
    version='0.0.1',
    description='ovos classic scifi horror skill plugin',
    url='https://github.com/JarbasSkills/skill-scifi-central',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_scifi_central": ""},
    package_data={'skill_scifi_central': ['locale/*', 'ui/*']},
    packages=['skill_scifi_central'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
