#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-stephen-king-audiobooks.jarbasai=skill_stephen_king_audiobooks:StephenKingAudioBooksSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-stephen-king-audiobooks',
    version='0.0.1',
    description='ovos stephen king audiobooks skill plugin',
    url='https://github.com/JarbasSkills/skill-stephen-king-audiobooks',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_stephen_king_audiobooks": ""},
    package_data={'skill_stephen_king_audiobooks': ['locale/*', 'res/*', 'ui/*']},
    packages=['skill_stephen_king_audiobooks'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
