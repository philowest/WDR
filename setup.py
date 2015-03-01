#
# Copyright 2012-2015 Marcin Plonka <mplonka@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from distutils.core import setup
import imp
import os

pathToFile = os.path.join('lib', 'common', 'wdr', '__init__.py')

setup(name='wdr',
      version=imp.load_source('wdr', pathToFile).getVersion(),
      description='Jython framework aiming for simplified WebSphere Application Server scripting',
      author='Marcin Plonka',
      author_email='mplonka@gmail.com',
      url='http://wdr.github.io/WDR/',
      package_dir={'': 'lib/common'},
      packages=['wdr'],
)