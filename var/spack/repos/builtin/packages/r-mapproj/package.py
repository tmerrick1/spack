##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RMapproj(RPackage):
    """Converts latitude/longitude into projected coordinates."""

    homepage = "https://cran.r-project.org/package=mapproj"
    url      = "https://cran.r-project.org/src/contrib/mapproj_1.2-5.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/mapproj"

    version('1.2-5', '90dc27f9edb2af28e13eafdfbb808dfb')
    version('1.2-4', '10e22bde1c790e1540672f15ddcaee71')

    depends_on('r-maps@2.3-0:', type=('build', 'run'))
